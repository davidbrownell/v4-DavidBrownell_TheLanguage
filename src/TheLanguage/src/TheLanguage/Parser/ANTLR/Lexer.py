# ----------------------------------------------------------------------
# |
# |  Lexer.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-07-26 10:54:56
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Functionality to Lex TheLanguage content"""

import itertools
import sys
import threading

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, cast, Optional

import antlr4

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx
from Common_Foundation.Streams.DoneManager import DoneManager

from Common_FoundationEx import ExecuteTasks

# pylint: disable=import-error
from TheLanguage import AllErrors

from TheLanguage.Common.Errors import Error, ExceptionError, TheLanguageException
from TheLanguage.Common.Location import Location
from TheLanguage.Common.Region import Region

from TheLanguage.Parser.ANTLR.AntlrVisitor import AntlrVisitor
from TheLanguage.Parser.ANTLR.AntlrVisitorMixin import AntlrVisitorMixin

from TheLanguage.Parser.Expressions.Expression import ExpressionType
from TheLanguage.Parser.Expressions.IdentifierExpression import IdentifierType
from TheLanguage.Parser.Expressions.LeafExpression import LeafExpression
from TheLanguage.Parser.Expressions.RootExpression import RootExpression

from TheLanguage.Parser.Impl.ParseIncludeExpression import ParseIncludeExpression, ParseIncludeComponentExpression, ParseIncludeFileExpression

# ----------------------------------------------------------------------
sys.path.insert(0, str(PathEx.EnsureDir(Path(__file__).parent / "GeneratedCode")))
with ExitStack(lambda: sys.path.pop(0)):
    from TheLanguageGrammarLexer import TheLanguageGrammarLexer             # type: ignore # pylint: disable=import-error
    from TheLanguageGrammarParser import TheLanguageGrammarParser           # type: ignore # pylint: disable=import-error


# ----------------------------------------------------------------------
# |
# |  Public Types
# |
# ----------------------------------------------------------------------
class AntlrException(Exception):
    """Exceptions raises based on lexing-related errors"""

    # ----------------------------------------------------------------------
    def __init__(
        self,
        message: str,
        source: Path,
        line: int,
        column: int,
        ex: Optional[antlr4.RecognitionException],
    ):
        location = Location(line, column)

        super(AntlrException, self).__init__("{} ({} <{}>)".format(message, source, location))

        self.source                         = source
        self.location                       = location
        self.ex                             = ex


# ----------------------------------------------------------------------
DEFAULT_FILE_EXTENSIONS: list[str]          = [
    ".TheLanguage",
]


# ----------------------------------------------------------------------
# |
# |  Public Functions
# |
# ----------------------------------------------------------------------
def Lex(
    dm: DoneManager,
    workspaces: dict[
        str,                                # Workspace name
        dict[
            str,                            # Translation unit
            Callable[[], str],              # get file content
        ],
    ],
    include_roots: list[Path],
    supported_file_extensions: Optional[list[str]]=None,
    *,
    single_threaded: bool=False,
    quiet: bool=False,
    raise_if_single_error: bool=True,
) -> Optional[
    dict[
        Path,                               # Workspace root
        dict[
            str,                            # Translation unit
            Error | RootExpression,
        ],
    ]
]:
    return _LexerImpl(
        workspaces,
        [include_root.resolve() for include_root in include_roots],
        supported_file_extensions or DEFAULT_FILE_EXTENSIONS,
    ).Execute(
        dm,
        quiet=quiet,
        single_threaded=single_threaded,
        raise_if_single_error=raise_if_single_error,
    )


# ----------------------------------------------------------------------
# |
# |  Private Types
# |
# ----------------------------------------------------------------------
class _LexerImpl(object):
    # ----------------------------------------------------------------------
    def __init__(
        self,
        workspaces: dict[
            str,                            # Workspace name
            dict[
                str,                        # Translation unit
                Callable[[], str],
            ],
        ],
        include_roots: list[Path],
        supported_file_extensions: list[str],
    ):
        self.workspaces                     = workspaces
        self.include_roots                  = include_roots
        self.supported_file_extensions      = supported_file_extensions

        self._execute_state: Optional[_LexerImpl._ExecuteState]             = None

    # ----------------------------------------------------------------------
    def Execute(
        self,
        dm: DoneManager,
        *,
        quiet: bool,
        single_threaded: bool,
        raise_if_single_error: bool,
    ) -> Optional[
        dict[
            Path,                           # Workspace root
            dict[
                str,                        # Translation unit
                Error | RootExpression,
            ],
        ]
    ]:
        # Create the workspace infos for all of the input content. At the same time, ensure that
        # there are no roots nested within each other.
        nested_roots: set[Path] = set()

        # ----------------------------------------------------------------------
        def EnsureNotNested(
            path: Path,
        ) -> None:
            existing_path = next((root for root in nested_roots if PathEx.IsDescendant(path, root)), None)
            if existing_path is not None:
                raise ValueError(
                    "The path '{}' is a descendant of '{}'.".format(path.as_posix(), existing_path.as_posix()),
                )

            nested_roots.add(path)

        # ----------------------------------------------------------------------

        workspace_infos: dict[Path, _LexerImpl._WorkspaceInfo] = {}

        for workspace_name in self.workspaces.keys():
            workspace_path = Path(workspace_name).resolve()

            EnsureNotNested(workspace_path)
            workspace_infos[workspace_path] = _LexerImpl._WorkspaceInfo()

        for include_root in self.include_roots:
            EnsureNotNested(include_root)
            workspace_infos[include_root] = _LexerImpl._WorkspaceInfo()

        del nested_roots

        # ----------------------------------------------------------------------
        def OnExit():
            self._execute_state = None

        # ----------------------------------------------------------------------

        with ExitStack(OnExit):
            with ExecuteTasks.YieldQueueExecutor(
                dm,
                "Lexing...",
                quiet=quiet,
                max_num_threads=1 if single_threaded else None,
            ) as enqueue_func:
                # Create the state data used while this method is active
                self._execute_state = _LexerImpl._ExecuteState(enqueue_func, workspace_infos)

                if len(self.workspaces) == 1:
                    create_description_func = lambda w, t: t
                else:
                    create_description_func = lambda w, t: (w / t).as_posix()

                for workspace_name, translation_units in self.workspaces.items():
                    workspace_path = Path(workspace_name).resolve()
                    workspace_info = workspace_infos[workspace_path]

                    with workspace_info.results_lock:
                        for translation_unit, content_func in translation_units.items():
                            # ----------------------------------------------------------------------
                            def ThisExecuteTask(
                                on_simple_status_func: Callable[[str], None],  # pylint: disable=unused-argument
                                workspace_path: Path=workspace_path,
                                translation_unit: str=translation_unit,
                                content_func: Callable[[], str]=content_func,
                            ) -> tuple[Optional[int], ExecuteTasks.QueueExecutorTypes.FuncType]:
                                return self._ExecuteTask(
                                    workspace_path,
                                    translation_unit,
                                    content_func,
                                    is_included_file=False,
                                )

                            # ----------------------------------------------------------------------

                            workspace_info.results[translation_unit] = None

                            enqueue_func(
                                create_description_func(workspace_path, translation_unit),
                                ThisExecuteTask,
                            )

            # Capture the results
            results: dict[
                Path,                       # Workspace root
                dict[
                    str,                    # Translation unit
                    Error | RootExpression,
                ],
            ] = {}

            errors: list[Error] = []

            for workspace_root, workspace_info in workspace_infos.items():
                these_results: dict[str, Error | RootExpression] = {}

                for translation_unit, translation_unit_result in workspace_info.results.items():
                    if translation_unit_result is None:
                        return None  # pragma: no cover

                    these_results[translation_unit] = translation_unit_result

                    if isinstance(translation_unit_result, Error):
                        errors.append(translation_unit_result)

                results[workspace_root] = these_results

            dm.result = len(errors)

            if raise_if_single_error and len(errors) == 1:
                raise TheLanguageException(errors[0])

            return results

    # ----------------------------------------------------------------------
    # |
    # |  Private Types
    # |
    # ----------------------------------------------------------------------
    @dataclass
    class _WorkspaceInfo(object):
        """Information about a workspace as it is being Lexed."""

        results: dict[str, None | Error | RootExpression]   = field(init=False, default_factory=dict)
        results_lock: threading.Lock                        = field(init=False, default_factory=threading.Lock)

    # ----------------------------------------------------------------------
    @dataclass
    class _ExecuteState(object):
        enqueue_func: ExecuteTasks.QueueExecutorTypes.EnqueueFuncType
        workspace_infos: dict[Path, "_LexerImpl._WorkspaceInfo"]

    # ----------------------------------------------------------------------
    # |
    # |  Private Methods
    # |
    # ----------------------------------------------------------------------
    def _ResolveSource(
        self,
        path: Path,
        *,
        allow_file: bool,
        allow_directory: bool,
    ) -> Optional[Path]:
        path = path.resolve()

        if allow_file:
            for file_extension in self.supported_file_extensions:
                potential_path = path.parent / (path.name + file_extension)
                if potential_path.is_file():
                    return potential_path

        if allow_directory and path.is_dir():
            return path

        return None

    # ----------------------------------------------------------------------
    def _CreateIncludeExpressions(
        self,
        include_expression_region: Region,
        source: Optional[AntlrVisitorMixin.CreateIncludeExpressionsSourceInfo],
        include_items: Region | list[AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem],
    ) -> list[ParseIncludeExpression]:
        assert self._execute_state is not None

        # Resolve the data that will be used to search for content
        resolved_source: Optional[LeafExpression[Path]] = None
        traverse_from_root: Optional[bool] = None
        force_directory: Optional[bool] = None
        is_relative: Optional[bool] = None

        if source is None:
            resolved_source = LeafExpression.Create(
                ExpressionType.Unknown, # BugBug
                include_expression_region,
                Path(),
            )

            traverse_from_root = False
            force_directory = True
            is_relative = False
        else:
            resolved_source = source.filename_or_directory

            traverse_from_root = source.traverse_from_root
            force_directory = source.force_directory
            is_relative = source.is_relative

        assert resolved_source is not None
        assert traverse_from_root is not None
        assert force_directory is not None
        assert is_relative is not None

        # Get the collection of roots that will be used to search for content
        search_roots: list[Path] = []

        if not traverse_from_root:
            search_roots.append(include_expression_region.filename.parent)

        if not is_relative:
            search_roots += self._execute_state.workspace_infos.keys()

        # Search the roots
        fullpath: Optional[Path] = None
        errors: list[Error] = []

        for potential_root in search_roots:
            potential_fullpath = self._ResolveSource(
                potential_root / resolved_source.value,
                allow_file=not force_directory,
                allow_directory=True,
            )

            if potential_fullpath is not None:
                # Determine if the fullpath is outside of any workspaces. This doesn't mean
                # that there is an error yet, as the content could be found under a different
                # search path. Store the data to issue the error if nothing was found.
                if not any(root for root in self._execute_state.workspace_infos.keys() if PathEx.IsDescendant(potential_fullpath, root)):
                    errors.append(
                        AllErrors.IncludeInvalidWorkspaceRoot.Create(resolved_source.region__, potential_fullpath),
                    )
                    continue

                # Don't allow self inclusion
                if potential_fullpath == include_expression_region.filename:
                    continue

                fullpath = potential_fullpath
                break

        if fullpath is None:
            if not errors:
                if force_directory:
                    errors.append(
                        AllErrors.IncludeInvalidSourceDirectory.Create(
                            resolved_source.region__,
                            resolved_source.value,
                        ),
                    )
                else:
                    errors.append(
                        AllErrors.IncludeInvalidSourceGeneric.Create(
                            resolved_source.region__,
                            resolved_source.value,
                        ),
                    )

            assert errors
            raise TheLanguageException(errors[0])

        # Create the results
        results: list[ParseIncludeExpression] = []

        if isinstance(include_items, Region):
            # If here, we are looking at a star include. Determine what to actually include based
            # on what fullpath points to.

            if fullpath.is_dir():
                # Import all of the other files in the directory
                for child in fullpath.iterdir():
                    if not child.is_file():
                        continue

                    results.append(
                        ParseIncludeExpression.Create(
                            include_expression_region,
                            LeafExpression[Path].Create(
                                ExpressionType.Unknown,  # BugBug
                                resolved_source.region__,
                                child,
                            ),
                            ParseIncludeFileExpression.Create(include_items, child.stem),
                        ),
                    )

            elif fullpath.is_file():
                # Import all of the content in this file
                results.append(
                    ParseIncludeExpression.Create(
                        include_expression_region,
                        LeafExpression[Path].Create(
                            ExpressionType.Unknown, # BugBug
                            resolved_source.region__,
                            fullpath,
                        ),
                        ParseIncludeFileExpression.Create(include_items, fullpath.stem),
                    ),
                )

            else:
                assert False, fullpath  # pragma: no cover

        elif isinstance(include_items, list):
            assert include_items and all(isinstance(include_item, AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem) for include_item in include_items)

            if fullpath.is_dir():
                # Import files
                for include_item in include_items:
                    include_item.element_name.Validate(IdentifierType.File)
                    include_item.reference_name.Validate(IdentifierType.File)

                    potential_fullpath = self._ResolveSource(
                        fullpath / include_item.element_name.value,
                        allow_file=True,
                        allow_directory=False,
                    )

                    if potential_fullpath is None:
                        raise AllErrors.IncludeInvalidFilename.CreateAsException(
                            include_item.element_name.region__,
                            include_item.element_name.value,
                        )

                    assert include_expression_region.filename == include_item.reference_name.region__.filename
                    assert include_expression_region.begin <= include_item.reference_name.region__.end
                    assert include_item.reference_name.region__ >= include_item.element_name.region__

                    results.append(
                        ParseIncludeExpression.Create(
                            Region.CreateFromLocations(
                                include_expression_region.filename,
                                include_expression_region.begin,
                                include_item.reference_name.region__.end,
                            ),
                            LeafExpression[Path].Create(
                                ExpressionType.Unknown, # BugBug
                                include_item.element_name.region__,
                                potential_fullpath,
                            ),
                            ParseIncludeFileExpression.Create(
                                include_item.reference_name.region__,
                                include_item.reference_name.value,
                            ),
                        ),
                    )

            elif fullpath.is_file():
                # Import components
                components: list[ParseIncludeComponentExpression] = []

                for include_item in include_items:
                    include_item.element_name.Validate(IdentifierType.Component)
                    include_item.reference_name.Validate(IdentifierType.Component)

                    components.append(
                        ParseIncludeComponentExpression.Create(
                            include_item.region,
                            include_item.element_name,
                            include_item.reference_name,
                        ),
                    )

                results.append(
                    ParseIncludeExpression.Create(
                        include_expression_region,
                        LeafExpression[Path].Create(
                            ExpressionType.Unknown, # BugBug
                            resolved_source.region__,
                            fullpath,
                        ),
                        components,
                    ),
                )

            else:
                assert False, fullpath  # pragma: no cover

        else:
            assert False, include_items  # pragma: no cover

        assert results

        # Ensure that all of the included files are scheduled to be lexed
        for result in results:
            for workspace_root, workspace_info in self._execute_state.workspace_infos.items():
                if not PathEx.IsDescendant(result.filename.value, workspace_root):
                    continue

                translation_unit = Path(*result.filename.value.parts[len(workspace_root.parts):]).as_posix()

                with workspace_info.results_lock:
                    if translation_unit not in workspace_info.results:
                        # ----------------------------------------------------------------------
                        def ThisExecuteTask(
                            on_simple_status_func: Callable[[str], None],  # pylint: disable=unused-argument
                            workspace_root: Path=workspace_root,
                            translation_unit: str=translation_unit,
                            fullpath: Path=result.filename.value,
                        ):
                            # ----------------------------------------------------------------------
                            def GetContent() -> str:
                                with fullpath.open() as f:
                                    return f.read()

                            # ----------------------------------------------------------------------

                            return self._ExecuteTask(
                                workspace_root,
                                translation_unit,
                                GetContent,
                                is_included_file=True,
                            )

                        # ----------------------------------------------------------------------

                        workspace_info.results[translation_unit] = None

                        self._execute_state.enqueue_func(
                            result.filename.value.as_posix(),
                            ThisExecuteTask,
                        )

                break

        return results

    # ----------------------------------------------------------------------
    def _ExecuteTask(
        self,
        workspace_root: Path,
        translation_unit: str,
        content_func: Callable[[], str],
        *,
        is_included_file: bool,
    ) -> tuple[Optional[int], ExecuteTasks.QueueExecutorTypes.FuncType]:
        assert self._execute_state is not None

        content = content_func()

        # ----------------------------------------------------------------------
        def Impl(
            status: ExecuteTasks.Status,
        ) -> Optional[str]:
            result: None | Error | RootExpression = None

            # ----------------------------------------------------------------------
            def OnExit():
                assert result is not None
                assert self._execute_state is not None

                workspace_info = self._execute_state.workspace_infos[workspace_root]

                with workspace_info.results_lock:
                    assert workspace_info.results[translation_unit] is None, (workspace_root, translation_unit)
                    workspace_info.results[translation_unit] = result

            # ----------------------------------------------------------------------

            with ExitStack(OnExit):
                try:
                    fullpath = workspace_root / translation_unit

                    error_listener = _ErrorListener(fullpath)

                    antlr_stream = antlr4.InputStream(content)

                    lexer = TheLanguageGrammarLexer(antlr_stream)

                    # Initialize instance variables that we have explicitly added within the
                    # ANTLR grammar file.
                    lexer.CustomInit()
                    lexer.addErrorListener(error_listener)

                    tokens = antlr4.CommonTokenStream(lexer)
                    tokens.fill()

                    parser = TheLanguageGrammarParser(tokens)
                    parser.addErrorListener(error_listener)

                    ast = parser.entry_point__()
                    assert ast

                    visitor = _Visitor(
                        fullpath,
                        lambda line: cast(None, status.OnProgress(line, None)),
                        self._CreateIncludeExpressions,
                        is_included_file=is_included_file,
                    )

                    ast.accept(visitor)

                    result = visitor.root

                except AssertionError:
                    raise  # pragma: no cover

                except TheLanguageException as ex:
                    assert len(ex.errors) == 1, ex.errors
                    result = ex.errors[0]

                except AntlrException as ex:
                    result = ExceptionError.Create(ex, include_callstack=False)

                except Exception as ex:                 # pragma: no cover
                    result = ExceptionError.Create(ex)  # pragma: no cover

        # ----------------------------------------------------------------------

        return len(content.split("\n")), Impl


# ----------------------------------------------------------------------
class _ErrorListener(antlr4.DiagnosticErrorListener):
    # ----------------------------------------------------------------------
    def __init__(
        self,
        source: Path,
        *args,
        **kwargs,
    ):
        super(_ErrorListener, self).__init__(*args, **kwargs)

        self._source                        = source

    # ----------------------------------------------------------------------
    def syntaxError(
        self,
        recognizer: TheLanguageGrammarParser,      # pylint: disable=unused-argument
        offendingSymbol: antlr4.Token,      # pylint: disable=unused-argument
        line: int,
        column: int,
        msg: str,
        e: antlr4.RecognitionException,
    ):
        raise AntlrException(msg, self._source, line, column + 1, e)


# ----------------------------------------------------------------------
class _Visitor(AntlrVisitor, AntlrVisitorMixin):
    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        AntlrVisitorMixin.__init__(self, *args, **kwargs)

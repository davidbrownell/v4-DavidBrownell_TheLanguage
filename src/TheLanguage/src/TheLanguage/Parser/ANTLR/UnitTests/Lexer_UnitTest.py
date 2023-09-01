# ----------------------------------------------------------------------
# |
# |  Lexer_UnitTest.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-07 08:39:49
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Unit tests for Lexer.py"""

import re
import sys
import textwrap

from pathlib import Path
from unittest.mock import MagicMock as Mock
from typing import Callable, cast, Optional

import pytest

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx
from Common_Foundation.TestHelpers.StreamTestHelpers import DoneManager, GenerateDoneManagerAndSink

from Common_FoundationEx.SafeYaml import ToYamlString
pytest.register_assert_rewrite("Common_PythonDevelopment.TestHelpers")
from Common_PythonDevelopment.TestHelpers import CompareResultsFromFile, ResultsFilenameFormat, DEFAULT_SUFFIX as RESULT_FILE_DEFAULT_SUFFIX

# ----------------------------------------------------------------------
sys.path.insert(0, str(PathEx.EnsureDir(Path(__file__).parent.parent.parent.parent.parent)))
with ExitStack(lambda: sys.path.pop(0)):
    from TheLanguage.Parser.ANTLR.Lexer import Error, Lex, RootExpression, TheLanguageException

    from TheLanguage.Parser.Expressions.Expression import Expression

    from TheLanguage.Parser.Visitors.DictExpressionVisitor import DictExpressionVisitor

# code_coverage: include = ../Lexer.py


# ----------------------------------------------------------------------
# TODO: def TODO_test_Variables(): # TODO
# TODO:     results, output = _Test(
# TODO:         {
# TODO:             "Foo": {
# TODO:                 "Bar": textwrap.dedent(
# TODO:                     """\
# TODO:                     fo🤡
# TODO:                     💄br
# TODO:                     b🛂z
# TODO:                     💄🛂
# TODO:                     """,
# TODO:                 ),
# TODO:             },
# TODO:         },
# TODO:     )
# TODO:
# TODO:     BugBug = 10


# ----------------------------------------------------------------------
class TestIncludeExpression(object):
    # ----------------------------------------------------------------------
    class TestFileImports(object):
        # ----------------------------------------------------------------------
        def test_ComponentFromFile(self, fs):
            fs.create_file("Workspace1/Module.TheLanguage", contents="")

            results = _Test(
                textwrap.dedent(
                    """\
                    from Module import Component
                    """,
                ),
            )

            fs.pause()

            assert len(results) == 2
            _CompareResults(results["File"], suffix="-File")
            _CompareResults(results["Module.TheLanguage"], suffix="-Module")

        # ----------------------------------------------------------------------
        def test_FileFromDirectory(self, fs):
            fs.create_file("Workspace1/Path/Module.TheLanguage", contents="")

            results = _Test(
                textwrap.dedent(
                    """\
                    from Path import Module
                    """,
                ),
            )

            fs.pause()

            assert len(results) == 2
            _CompareResults(results["File"], suffix="-File")
            _CompareResults(results["Path/Module.TheLanguage"], suffix="-Module")

    # ----------------------------------------------------------------------
    class TestTrailingSlash(object):
        # ----------------------------------------------------------------------
        @staticmethod
        @pytest.fixture
        def _this_fs(fs):
            fs.create_file("Workspace1/Ambiguous.TheLanguage", contents="")
            fs.create_file("Workspace1/Ambiguous/Module.TheLanguage", contents="")

            return fs

        # ----------------------------------------------------------------------
        def test_FavorFiles(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from Ambiguous import Component
                    """,
                ),
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["File"], suffix="-File")
            _CompareResults(results["Ambiguous.TheLanguage"], suffix="-Component")

        # ----------------------------------------------------------------------
        def test_ForceDirectory(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from Ambiguous/ import Module
                    """,
                ),
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["File"], suffix="-File")
            _CompareResults(results["Ambiguous/Module.TheLanguage"], suffix="-Module")

    # ----------------------------------------------------------------------
    class TestInitialSlash(object):
        # ----------------------------------------------------------------------
        @staticmethod
        @pytest.fixture
        def _this_fs(fs):
            fs.create_file("Workspace1/Ambiguous.TheLanguage", contents="")
            fs.create_file("Workspace1/Path/Ambiguous.TheLanguage", contents="")

            return fs

        # ----------------------------------------------------------------------
        def test_FavorSameDirectory(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from Ambiguous import Component
                    """,
                ),
                "Path/File",
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["Path/File"], suffix="-File")
            _CompareResults(results["Path/Ambiguous.TheLanguage"], suffix="-Nested")

        # ----------------------------------------------------------------------
        def test_ForceRoot(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from /Ambiguous import Component
                    """,
                ),
                "Path/File",
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["Path/File"], suffix="-File")
            _CompareResults(results["Ambiguous.TheLanguage"], suffix="-Nested")

    # ----------------------------------------------------------------------
    class TestInitialDot(object):
        # ----------------------------------------------------------------------
        @staticmethod
        @pytest.fixture
        def _this_fs(fs):
            fs.create_file("Workspace1/Path/Module.TheLanguage", contents="")

            return fs

        # ----------------------------------------------------------------------
        def test_NoDot(self, _this_fs):
            with pytest.raises(
                TheLanguageException,
                match=re.escape("The filename or directory 'Module' does not exist. (C:/Workspace1/File, line 1, column 6 -> line 1, column 12)"),
            ):
                _Test(
                    textwrap.dedent(
                        """\
                        from Module import Component
                        """,
                    ),
                )

        # ----------------------------------------------------------------------
        def test_WithDotAndSlash(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from ./Path import Module
                    """,
                ),
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["File"], suffix="-File")
            _CompareResults(results["Path/Module.TheLanguage"], suffix="-Module")

        # ----------------------------------------------------------------------
        def test_WithDot(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from . import Module
                    """,
                ),
                "Path/File",
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["Path/File"], suffix="-File")
            _CompareResults(results["Path/Module.TheLanguage"], suffix="-Module")

    # ----------------------------------------------------------------------
    class TestRelative(object):
        # ----------------------------------------------------------------------
        @staticmethod
        @pytest.fixture
        def _this_fs(fs):
            fs.create_file("Workspace1/Path1/Path2/Path3/Module.TheLanguage")
            fs.create_file("Workspace1/Module.TheLanguage")

            return fs

        # ----------------------------------------------------------------------
        def test_Valid(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from ../../../Module import Component
                    """,
                ),
                "Path1/Path2/Path3/File",
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["Path1/Path2/Path3/File"], suffix="-File")
            _CompareResults(results["Module.TheLanguage"], suffix="-Module")

        # ----------------------------------------------------------------------
        def test_InvalidPath(self, _this_fs):
            with pytest.raises(
                TheLanguageException,
                match=re.escape("The filename or directory '../Does/Not/Exist' does not exist. (C:/Workspace1/Path1/Path2/Path3/File, line 1, column 6 -> line 1, column 23)"),
            ):
                _Test(
                    textwrap.dedent(
                        """\
                        from ../Does/Not/Exist import Component
                        """,
                    ),
                    "Path1/Path2/Path3/File",
                )

        # ----------------------------------------------------------------------
        def test_InvalidRoot(self, _this_fs):
            # In this test, the file exists but is not within a workspace or include root

            with pytest.raises(
                TheLanguageException,
                match=re.escape("The filename or directory 'C:/Module.TheLanguage' is not contained within a workspace or include root. (C:/Workspace1/Path1/Path2/Path3/File, line 1, column 6 -> line 1, column 24)"),
            ):
                _this_fs.create_file("Module.TheLanguage")

                _Test(
                    textwrap.dedent(
                        """\
                        from ../../../../Module import Component
                        """,
                    ),
                    "Path1/Path2/Path3/File",
                )

    # ----------------------------------------------------------------------
    class TestStarImport(object):
        # ----------------------------------------------------------------------
        @staticmethod
        @pytest.fixture
        def _this_fs(fs):
            fs.create_file("Workspace1/FileA.TheLanguage")
            fs.create_file("Workspace1/Path1/FileB.TheLanguage")

            fs.create_file("Workspace1/Path1/Path2/File1.TheLanguage")
            fs.create_file("Workspace1/Path1/Path2/File2.TheLanguage")
            fs.create_file("Workspace1/Path1/Path2/File3.TheLanguage")

            return fs

        # ----------------------------------------------------------------------
        def test_ImportViaDirectory(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from . import *
                    """,
                ),
                "Path1/Path2/File",
            )

            _this_fs.pause()

            assert len(results) == 4
            _CompareResults(results["Path1/Path2/File"], suffix="-File")
            _CompareResults(results["Path1/Path2/File1.TheLanguage"], suffix="-File1")
            _CompareResults(results["Path1/Path2/File2.TheLanguage"], suffix="-File2")
            _CompareResults(results["Path1/Path2/File3.TheLanguage"], suffix="-File3")

        # ----------------------------------------------------------------------
        def test_ImportViaFile(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    from File1 import *
                    """,
                ),
                "Path1/Path2/File",
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["Path1/Path2/File"], suffix="-File")
            _CompareResults(results["Path1/Path2/File1.TheLanguage"], suffix="-File1")

        # ----------------------------------------------------------------------
        def test_Isolated(self, _this_fs):
            results = _Test(
                textwrap.dedent(
                    """\
                    import *
                    """,
                ),
                "Path1/File",
            )

            _this_fs.pause()

            assert len(results) == 2
            _CompareResults(results["Path1/File"], suffix="-File")
            _CompareResults(results["Path1/FileB.TheLanguage"], suffix="-FileB")

    # ----------------------------------------------------------------------
    def test_IsolatedImport(self, fs):
        fs.create_file("Workspace1/Foo.TheLanguage")
        fs.create_file("Workspace1/Bar.TheLanguage")

        results = _Test(
            textwrap.dedent(
                """\
                import Foo, Bar
                """,
            ),
        )

        fs.pause()

        assert len(results) == 3
        _CompareResults(results["File"], suffix="-File")
        _CompareResults(results["Foo.TheLanguage"], suffix="-Foo")
        _CompareResults(results["Bar.TheLanguage"], suffix="-Bar")

    # ----------------------------------------------------------------------
    class TestIncludeRoots(object):
        # ----------------------------------------------------------------------
        @staticmethod
        @pytest.fixture
        def _this_fs(fs):
            fs.create_file("Workspace1/Path1/Include.TheLanguage")
            fs.create_file("Workspace2/Include.TheLanguage")
            fs.create_file("Workspace3/Path3/Include.TheLanguage")

            return fs

        # ----------------------------------------------------------------------
        def test_LocalPriority(self, _this_fs):
            results = _TestEx(
                {
                    "Workspace1": {
                        "Path1/File": textwrap.dedent(
                            """\
                            from Include import *
                            """,
                        ),
                    },
                },
                include_roots=[
                    Path("Workspace2"),
                    Path("Workspace3"),
                ],
            )[0]

            workspace1_key = Path("Workspace1").resolve()
            workspace2_key = Path("Workspace2").resolve()
            workspace3_key = Path("Workspace3").resolve()

            _this_fs.pause()

            assert len(results) == 3
            _CompareResults(results[workspace1_key]["Path1/File"], suffix="-File")
            _CompareResults(results[workspace1_key]["Path1/Include.TheLanguage"], suffix="-Include")
            assert not results[workspace2_key]
            assert not results[workspace3_key]

        # ----------------------------------------------------------------------
        def test_IncludeRootOverNested(self, _this_fs):
            results = _TestEx(
                {
                    "Workspace1": {
                        "File": textwrap.dedent(
                            """\
                            from Include import *
                            """,
                        ),
                    },
                },
                include_roots=[
                    Path("Workspace2"),
                    Path("Workspace3"),
                ],
            )[0]

            workspace1_key = Path("Workspace1").resolve()
            workspace2_key = Path("Workspace2").resolve()
            workspace3_key = Path("Workspace3").resolve()

            _this_fs.pause()

            assert len(results) == 3
            _CompareResults(results[workspace1_key]["File"], suffix="-File")
            _CompareResults(results[workspace2_key]["Include.TheLanguage"], suffix="-Include")
            assert not results[workspace3_key]

        # ----------------------------------------------------------------------
        def test_RootInclude(self, _this_fs):
            results = _TestEx(
                {
                    "Workspace1": {
                        "File": textwrap.dedent(
                            """\
                            from /Include import *
                            """,
                        ),
                    },
                },
                include_roots=[
                    Path("Workspace2"),
                    Path("Workspace3"),
                ],
            )[0]

            workspace1_key = Path("Workspace1").resolve()
            workspace2_key = Path("Workspace2").resolve()
            workspace3_key = Path("Workspace3").resolve()

            _this_fs.pause()

            assert len(results) == 3
            _CompareResults(results[workspace1_key]["File"], suffix="-File")
            _CompareResults(results[workspace2_key]["Include.TheLanguage"], suffix="-Include")
            assert not results[workspace3_key]

        # ----------------------------------------------------------------------
        def test_NestedInclude(self, _this_fs):
            results = _TestEx(
                {
                    "Workspace1": {
                        "File": textwrap.dedent(
                            """\
                            from Path3/Include import *
                            """,
                        ),
                    },
                },
                include_roots=[
                    Path("Workspace2"),
                    Path("Workspace3"),
                ],
            )[0]

            workspace1_key = Path("Workspace1").resolve()
            workspace2_key = Path("Workspace2").resolve()
            workspace3_key = Path("Workspace3").resolve()

            _this_fs.pause()

            assert len(results) == 3
            _CompareResults(results[workspace1_key]["File"], suffix="-File")
            assert not results[workspace2_key]
            _CompareResults(results[workspace3_key]["Path3/Include.TheLanguage"], suffix="-Include")

        # ----------------------------------------------------------------------
        def test_IncludeSameNameAsFile(self, _this_fs):
            # Imports should not import themselves
            _this_fs.create_file("Workspace1/Include.TheLanguage")

            results = _TestEx(
                {
                    "Workspace1": {
                        "Include.TheLanguage": textwrap.dedent(
                            """
                            from Include import *
                            """,
                        ),
                    },
                },
                include_roots=[
                    Path("Workspace2"),
                    Path("Workspace3"),
                ],
            )[0]

            workspace1_key = Path("Workspace1").resolve()
            workspace2_key = Path("Workspace2").resolve()
            workspace3_key = Path("Workspace3").resolve()

            _this_fs.pause()

            assert len(results) == 3
            _CompareResults(results[workspace1_key]["Include.TheLanguage"], suffix="-File")
            _CompareResults(results[workspace2_key]["Include.TheLanguage"], suffix="-Include")
            assert not results[workspace3_key]

        # ----------------------------------------------------------------------
        def test_NestedError(self):
            cwd = Path().resolve().as_posix()

            # Include roots nested
            with pytest.raises(
                ValueError,
                match=re.escape("The path '{cwd}/Root1/Nested' is a descendant of '{cwd}/Root1'.".format(cwd=cwd)),
            ):
                _TestEx(
                    {
                        "Workspace1": {
                            "File": "",
                        },
                    },
                    include_roots=[
                        Path("Root1"),
                        Path("Root2"),
                        Path("Root1/Nested"),
                    ],
                )

            # Workspaces nested
            with pytest.raises(
                ValueError,
                match=re.escape("The path '{cwd}/Workspace1/Nested' is a descendant of '{cwd}/Workspace1'.".format(cwd=cwd)),
            ):
                _TestEx(
                    {
                        "Workspace1": {
                            "File": "",
                        },
                        "Workspace1/Nested": {
                            "File": "",
                        },
                    },
                    [],
                )

            # Include nested in workspace
            with pytest.raises(
                ValueError,
                match=re.escape("The path '{cwd}/Workspace1/Path/Nested' is a descendant of '{cwd}/Workspace1'.".format(cwd=cwd)),
            ):
                _TestEx(
                    {
                        "Workspace1": {
                            "File": "",
                        },
                    },
                    [
                        Path("Workspace1/Path/Nested"),
                    ],
                )

    # ----------------------------------------------------------------------
    def test_ImportAlias(self, fs):
        fs.create_file("Workspace1/Foo.TheLanguage")

        results = _Test(
            textwrap.dedent(
                """
                from . import Foo as Bar
                """,
            ),
        )

        fs.pause()

        assert len(results) == 2
        _CompareResults(results["File"], suffix="-File")
        _CompareResults(results["Foo.TheLanguage"], suffix="-Foo")

    # ----------------------------------------------------------------------
    def test_VariedStyles(self, fs):
        fs.create_file("Workspace1/Foo.TheLanguage")
        fs.create_file("Workspace1/Bar.TheLanguage")
        fs.create_file("Workspace1/Baz.TheLanguage")

        results = _Test(
            textwrap.dedent(
                """\
                from . import Foo, Bar
                from . import Foo, Bar,
                from . import Foo as f, Bar as b,

                from . import (Foo)
                from . import (Foo, )

                from . import (
                    Foo
                )
                from . import (
                    Foo as F,
                    Bar as B1,
                    Baz as B2,
                )
                """,
            ),
        )

        fs.pause()

        assert len(results) == 4
        _CompareResults(results["File"], suffix="-File")
        _CompareResults(results["Foo.TheLanguage"], suffix="-Foo")
        _CompareResults(results["Bar.TheLanguage"], suffix="-Bar")
        _CompareResults(results["Baz.TheLanguage"], suffix="-Baz")

    # ----------------------------------------------------------------------
    def test_ErrorInvalidFilename(self, fs):
        fs.create_file("Workspace1/Path1/File.TheLanguage")

        with pytest.raises(
            TheLanguageException,
            match=re.escape("The filename 'InvalidFilename' does not exist. (C:/Workspace1/File, line 1, column 20 -> line 1, column 35)"),
        ):
            _Test(
                textwrap.dedent(
                    """\
                    from Path1/ import InvalidFilename
                    """,
                ),
            )

    # ----------------------------------------------------------------------
    def test_ErrorInvalidSourceDirectory(self, fs):
        with pytest.raises(
            TheLanguageException,
            match=re.escape("The directory 'InvalidPath' does not exist. (C:/Workspace1/File, line 1, column 6 -> line 1, column 18)"),
        ):
            _Test(
                textwrap.dedent(
                    """\
                    from InvalidPath/ import *
                    """,
                ),
            )

    # BugBug: Invalid file name
    # BugBug: Invalid file import
    # BugBug: Invalid file reference
    # BugBug: Invalid component
    # BugBug: Invalid component reference


# ----------------------------------------------------------------------
def test_InvalidSyntax():
    with pytest.raises(
        TheLanguageException,
        match=re.escape(
            textwrap.dedent(
                """\
                Python Exception: token recognition error at: '+' ({} <line 1, column 8>)


                """,
            ).format(
                Path(Path().resolve()) / "Workspace1" / "File",
            ),
        ),
    ):
        _Test(
            textwrap.dedent(
                """\
                from 2 + 2
                """,
            ),
        )


# ----------------------------------------------------------------------
def test_MultipleWorkspaces(fs):
    results = _TestEx(
        {
            "Workspace1": {
                "File": "",
            },
            "Workspace2": {
                "File": "",
            },
        },
        [],
    )[0]

    workspace1_key = Path("Workspace1").resolve()
    workspace2_key = Path("Workspace2").resolve()

    fs.pause()

    assert len(results) == 2
    _CompareResults(results[workspace1_key]["File"], suffix="-File1")
    _CompareResults(results[workspace2_key]["File"], suffix="-File2")


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
def _TestEx(
    content: dict[str, dict[str, str]],
    include_roots: list[Path],
    *,
    expected_result: int=0,
    debug: bool=True,
) -> tuple[dict[Path, dict[str, None | Error | RootExpression]], str]:
    dm_and_sink = iter(GenerateDoneManagerAndSink(debug=debug, expected_result=expected_result))

    callable_content: dict[str, dict[str, Callable[[], str]]] = {}

    for workspace_name, translation_units in content.items():
        workspace_callable_content: dict[str, Callable[[], str]] = {}

        for translation_unit, tu_content in translation_units.items():
            workspace_callable_content[translation_unit] = lambda tu_content=tu_content: tu_content

        callable_content[workspace_name] = workspace_callable_content

    results = Lex(
        cast(DoneManager, next(dm_and_sink)),
        callable_content,
        include_roots,
    )

    output = cast(str, next(dm_and_sink))

    return results, output


# ----------------------------------------------------------------------
def _Test(
    content: str,
    file_name: str="File",
    include_roots: Optional[list[Path]]=None,
) -> dict[str, RootExpression]:
    results, output = _TestEx(
        {
            "Workspace1": {
                file_name: content,
            },
        },
        include_roots or [],
    )

    assert len(results) == 1
    results = next(iter(results.values()))

    assert all(isinstance(result, RootExpression) for result in results.values())
    return cast(dict[str, RootExpression], results)


# ----------------------------------------------------------------------
def _CompareResults(
    expression: Expression,
    *,
    suffix: Optional[str]=RESULT_FILE_DEFAULT_SUFFIX,
):
    visitor = DictExpressionVisitor()

    expression.Accept(visitor)

    CompareResultsFromFile(
        ToYamlString(visitor.root),
        suffix=suffix,
        decorate_stem_func=lambda name: name[:-len("_UnitTest")],
        decorate_test_name_func=lambda name: name[len("test_"):],
        file_extension=".yaml",
        call_stack_offset=1,
        results_filename_format=ResultsFilenameFormat.Version2,
    )

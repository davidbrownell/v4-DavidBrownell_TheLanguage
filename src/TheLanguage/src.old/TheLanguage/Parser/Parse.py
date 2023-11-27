# ----------------------------------------------------------------------
# |
# |  Parse.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-02 06:38:02
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains functions and types used during the parsing process."""

import importlib
import os
import sys
import traceback

from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, cast, Generator, Optional, TypeVar

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx

from TheLanguage.Common.Errors import Error, ExceptionError, TheLanguageException
from TheLanguage.Common.Range import Range
from TheLanguage.Parser.AST import Leaf, Node
from TheLanguage.Parser.Expressions.Expression import Expression
from TheLanguage.Parser.Expressions.RootExpression import RootExpression


# ----------------------------------------------------------------------
# |
# |  Public Types
# |
# ----------------------------------------------------------------------
class ParseObserver(ABC):
    """Observes events generated during the parsing process."""

    # ----------------------------------------------------------------------
    # |  Public Types
    ExtractExpressionReturnType             = None | Expression | Callable[[], Expression]
    ExtractPotentialDocumentationReturnType = Optional[tuple[Leaf | Node, str]]

    # ----------------------------------------------------------------------
    # |  Public Methods
    @abstractmethod
    def ExtractExpression(
        self,
        node: Node,
    ) -> "ParseObserver.ExtractExpressionReturnType":
        raise Exception("Abstract method")  # pragma: no cover

    # ----------------------------------------------------------------------
    @abstractmethod
    def ExtractPotentialDocumentation(
        self,
        leaf_or_node: Leaf | Node,
    ) -> "ParseObserver.ExtractPotentialDocumentationReturnType":
        raise Exception("Abstract method")  # pragma: no cover


# ----------------------------------------------------------------------
# |
# |  Public Functions
# |
# ----------------------------------------------------------------------
def HasExpressionErrors(
    node: Node,
) -> bool:
    return getattr(node, _EXPRESSION_HAS_ERRORS_ATTRIBUTE_NAME, False)


# ----------------------------------------------------------------------
def GetExpressionNoThrow(
    node: Node,
) -> Optional[Expression]:
    if HasExpressionErrors(node):
        pass # BugBug

    return getattr(node, _EXPRESSION_ATTRIBUTE_NAME, None)


# ----------------------------------------------------------------------
def GetExpression(
    node: Node,
) -> Expression:
    result = GetExpressionNoThrow(node)
    assert result is not None

    return result


# ----------------------------------------------------------------------
def Parse(
    workspaces: dict[
        str,                                # Workspace name
        dict[
            str,                            # Translation unit
            Node,
        ],
    ],
    observer: ParseObserver,
    *,
    max_num_threads: Optional[int]=None,
) -> Optional[
    dict[
        str,                                # Workspace name
        dict[
            str,                            # Translation unit
            list[Error] | RootExpression,
        ],
    ],
]:
    # ----------------------------------------------------------------------
    def CreateAndExtract(
        name: tuple[str, str],
        root: Node,
    ) -> None | list[Error] | RootExpression:
        errors: list[Error] = []

        callback_funcs: list[tuple[Node, Callable[[], Any]]] = []

        for node in root.Enum(nodes_only=True):
            assert isinstance(node, Node), node

            try:
                result = observer.ExtractExpression(node)

                if result is None:
                    continue
                elif callable(result):
                    callback_funcs.append((node, result))
                elif isinstance(result, Expression):
                    _SetExpression(node, result)
                else:
                    assert False, result  # pragma: no cover

            except TheLanguageException as ex:
                errors += ex.errors

            except Exception as ex:
                errors.append(ExceptionError.Create(ex))

        for node, callback in reversed(callback_funcs):
            try:
                result = callback()

                if isinstance(result, Expression):
                    _SetExpression(node, result)
                else:
                    assert False, result  # pragma: no cover

            except TheLanguageException as ex:
                errors += ex.errors

            except Exception as ex:
                errors.append(ExceptionError.Create(ex))

        # Extract the root information
        existing_documentation: Optional[tuple[Leaf | Node, str]] = None
        expressions: list[Expression] = []

        for child in root.children:
            try:
                # Does this child have documentation?
                result = observer.ExtractPotentialDocumentation(child)
                if result is not None:
                    if existing_documentation is not None:
                        pass # BugBug errors.append()
                    else:
                        existing_documentation = result

                # Is this an expression?
                if isinstance(child, Node):
                    expression = _ExtractExpression(child)
                    if expression is not None:
                        expressions.append(expression)
                else:
                    assert False, child  # pragma: no cover

            except TheLanguageException as ex:
                errors += ex.errors

            except Exception as ex:
                errors.append(ExceptionError.Create(ex))

        if errors:
            return errors

        if existing_documentation is None:
            documentation_node = None
            documentation_info = None
        else:
            documentation_node, documentation_info = existing_documentation

        try:
            if not expressions:
                expression_node = None
                expressions = None  # type: ignore
            else:
                expression_node = root

            return RootExpression(
                [root.range, expression_node.range, documentation_node.range],
                os.path.splitext(name[1])[0],
                expressions,
                documentation_info,
            )

        except TheLanguageException as ex:
            return ex.errors

        except Exception as ex:
            return [ExceptionError.Create(ex), ]

    # ----------------------------------------------------------------------

    return _Execute(
        workspaces,
        CreateAndExtract,
        max_num_threads=max_num_threads,
    )


# ----------------------------------------------------------------------
def ValidateExpressionTypes(
    workspaces: dict[
        str,                                # Workspace name
        dict[
            str,                            # Translation unit
            RootExpression,
        ],
    ],
    configuration_values: Any, # BugBug
    *,
    include_fundamental_types: bool=True,
    max_num_threads: Optional[int]=None,
) -> Optional[
    dict[
        str,                                # Workspace name
        dict[
            str,                            # Translation unit
            list[Error] | RootExpression
        ],
    ],
]:
    mini_language_configuration_values: dict[str, Any] = {} # BugBug

    with ExitStack() as exit_stack:
        # Add all of the funamental types to the workspaces. This content will be used to validate types,
        # then removed so the workspaces appear to be the same from the caller's perspective.
        if include_fundamental_types:
            generated_code_dir = Path(__file__).parent / "FundamentalTypes" / "GeneratedCode"
            assert generated_code_dir.is_dir(), generated_code_dir

            fundamental_types: dict[str, RootExpression] = {}

            for root, _, filenames in os.walk(generated_code_dir):
                for filename in filenames:
                    fullpath = Path(root) / filename

                    if fullpath.ext != ".py":
                        continue

                    if fullpath.name == "__init__.py":
                        continue

                    sys.path.insert(0, root)
                    with ExitStack(lambda: sys.path.pop(0)):
                        mod = importlib.import_module(fullpath.stem)

                        root_expression = getattr(mod, "root_expression", None)
                        assert root_expression is not None, fullpath

                        relative_path = PathEx.CreateRelativePath(generated_code_dir, fullpath)
                        relative_path = ".".join(relative_path.parts)

                        fundamental_types[relative_path] = root_expression

            # Add the fundamental types to the workspaces collection
            assert _FUNDAMENTAL_TYPES_WORKSPACE_NAME not in workspaces
            workspaces[_FUNDAMENTAL_TYPES_WORKSPACE_NAME] = fundamental_types

            exit_stack.callback(lambda: workspaces.pop(_FUNDAMENTAL_TYPES_WORKSPACE_NAME))

        # Pass 1
        executor = PassOneVisitor.Executor(mini_language_configuration_values)

        for is_parallel, func in executor.GenerateFuncs():
            results = _Execute(
                workspaces,
                func,
                max_num_threads=max_num_threads if is_parallel else 1,
            )

            if results is None:
                return None

            # Check for errors
            error_data = _ExtractErrorsFromResults(results)
            if error_data is not None:
                return error_data  # type: ignore

            results = cast(dict[str, dict[str, RootExpression]], results)

        global_namespace = executor.global_namespace
        translation_unit_namespaces = executor.translation_unit_namespaces

        fundamental_types_namespace = global_namespace.GetChild(_FUNDAMENTAL_TYPES_WORKSPACE_NAME)
        assert not isinstance(fundamental_types_namespace, list), fundamental_types_namespace

        # Pass 2
        executor = Pass2Visitor.Executor(
            mini_language_configuration_values,
            translation_unit_namespaces,
            fundamental_types_namespace,
        )

        for is_parallel, func in executor.GenerateFuncs():
            results = _Execute(
                workspaces,
                func,
                max_num_threads=max_num_threads if is_parallel else 1,
            )

            if results is None:
                return results

            error_data = _ExtractErrorsFromResults(results)
            if error_data is not None:
                return error_data  # type: ignore

            results = cast(dict[str, dict[str, RootExpression]], results)

        # Pass 3
        # BugBug

    return workspaces  # type: ignore


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
_EXPRESSION_ATTRIBUTE_NAME                  = "expression"
_EXPRESSION_HAS_ERRORS_ATTRIBUTE_NAME       = "_has_expression_errors"

_FUNDAMENTAL_TYPES_WORKSPACE_NAME           = "___fundamental_types___"


# ----------------------------------------------------------------------
def _SetExpression(
    node: Node,
    expression: Expression,
) -> None:
    object.__setattr__(node, _EXPRESSION_ATTRIBUTE_NAME, expression)


# ----------------------------------------------------------------------
def _SetHasExpressionErrors(
    node: Node,
) -> None:
    object.__setattr__(node, _EXPRESSION_HAS_ERRORS_ATTRIBUTE_NAME, True)



# ----------------------------------------------------------------------
def _ExtractExpression(
    node: Node,
) -> Optional[Expression]:
    expression = GetExpressionNoThrow(node)
    if expression is not None:
        return expression

    child_expressions: list[Expression] = []

    for child in node.children:
        if isinstance(child, Leaf):
            continue

        child_expression = _ExtractExpression(child)
        if child_expression is not None:
            child_expressions.append(child_expression)

    if not child_expressions:
        return None

    assert len(child_expressions) == 1, child_expressions
    return child_expressions[0]


# ----------------------------------------------------------------------
def _ExtractErrorsFromResults(
    results: dict[str, dict[str, Any]],
) -> Optional[
    dict[
        str,                                # Workspace name
        dict[
            str,                            # Translation unit
            list[Error],
        ],
    ],
]:
    error_results: dict[str, dict[str, list[Error]]] = {}

    for workspace_name, translation_units in results.items():
        translation_units_errors: dict[str, list[Error]] = {}

        for translation_unit, translation_unit_results in translation_units.items():
            if (
                isinstance(translation_unit_results, list)
                and translation_unit_results
                and isinstance(translation_unit_results[0], Error)
            ):
                translation_units_errors[translation_unit] = translation_unit_results

        if translation_units_errors:
            error_results[workspace_name] = translation_units_errors

    return error_results or None


# ----------------------------------------------------------------------
_ExecuteInputType                           = TypeVar("_ExecuteInputType")
_ExecuteOutputType                          = TypeVar("_ExecuteOutputType")

def _Execute(
    workspaces: dict[
        str,                                # Workspace name
        dict[
            str,                            # Translation unit
            _ExecuteInputType,
        ],
    ],
    execute_func: Callable[
        [
            tuple[
                str,                        # Workspace name
                str,                        # Translation unit
            ],
            _ExecuteInputType,
        ],
        Optional[_ExecuteOutputType],
    ],
    *,
    max_num_threads: Optional[int]=None,
) -> Optional[
    dict[
        str,                                # Workspace name
        dict[
            str,                            # Translation unit
            _ExecuteOutputType,
        ],
    ],
]:
    # ----------------------------------------------------------------------
    def EnumInputs() -> Generator[
        tuple[
            str,                            # Workspace name
            str,                            # Translation unit
            _ExecuteInputType,
        ],
        None,
        None,
    ]:
        for workspace_name, translation_units in workspaces.items():
            for translation_unit, input in translation_units.items():
                yield workspace_name, translation_unit, input

    # ----------------------------------------------------------------------
    def Execute(
        name: tuple[str, str],              # Workspace name, Translation unit
        input_value: _ExecuteInputType,
    ) -> Optional[_ExecuteOutputType]:
        try:
            return execute_func(name, input_value)
        except Exception as ex:
            if not hasattr(ex, "fully_qualified_name"):
                object.__setattr__(ex, "fully_qualified_name", os.path.join(*name))

            raise

    # ----------------------------------------------------------------------

    with ThreadPoolExecutor(
        max_workers=max_num_threads,
    ) as executor:
        raw_results = executor.map(Execute, EnumInputs())

    results: dict[str, dict[str, _ExecuteOutputType]] = {}

    for ((workspace_name, translation_unit, _), raw_result) in zip(EnumInputs(), raw_results):
        if raw_result is None:
            return None

        results[workspace_name][translation_unit] = raw_result

    return results

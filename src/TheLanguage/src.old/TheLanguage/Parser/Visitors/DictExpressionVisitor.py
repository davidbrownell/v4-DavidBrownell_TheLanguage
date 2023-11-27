# ----------------------------------------------------------------------
# |
# |  DictExpressionVisitor.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-26 18:16:38
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the DictExpressionVisitor object"""

from contextlib import contextmanager
from functools import cached_property
from pathlib import Path
from typing import Any, Callable, Iterator, Optional

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation.Types import overridemethod

from TheLanguage.Parser.Expressions.Expression import Expression
from TheLanguage.Parser.Expressions.IdentifierExpression import IdentifierExpression
from TheLanguage.Parser.Expressions.LeafExpression import LeafExpression
from TheLanguage.Parser.Expressions.RootExpression import RootExpression

from TheLanguage.Parser.Impl.ParseIncludeExpression import ParseIncludeExpression, ParseIncludeComponentExpression

from TheLanguage.Parser.Visitors.ExpressionVisitor import ExpressionVisitor, VisitResult


# ----------------------------------------------------------------------
class DictExpressionVisitor(ExpressionVisitor):
    """Generates yaml content for a given expression and its children"""

    # ----------------------------------------------------------------------
    def __init__(
        self,
        *,
        include_class: bool=True,
        include_expression_type: bool=True,
        include_region: bool=True,
        include_disabled: bool=True,
    ):
        decorator_func: Callable[[Expression, dict[str, Any]], None] = lambda *args, **kwargs: None

        if include_disabled:
            disabled_prev_decorator_func = decorator_func

            # ----------------------------------------------------------------------
            def DecorateDisabled(expression, obj):
                obj["is_disabled__"] = expression.is_disabled__
                disabled_prev_decorator_func(expression, obj)

            # ----------------------------------------------------------------------

            decorator_func = DecorateDisabled

        if include_region:
            region_prev_decorator_func = decorator_func

            # ----------------------------------------------------------------------
            def DecorateRegion(expression, obj):
                obj["region__"] = str(expression.region__)
                region_prev_decorator_func(expression, obj)

            # ----------------------------------------------------------------------

            decorator_func = DecorateRegion

        if include_expression_type:
            expression_type_prev_decorator_func = decorator_func

            # ----------------------------------------------------------------------
            def DecorateExpressionType(expression, obj):
                obj["expression_type__"] = expression.expression_type__.name
                expression_type_prev_decorator_func(expression, obj)

            # ----------------------------------------------------------------------

            decorator_func = DecorateExpressionType

        if include_class:
            class_prev_decorator_func = decorator_func

            # ----------------------------------------------------------------------
            def DecorateClass(expression, obj):
                obj["__class__"] = type(expression).__name__
                class_prev_decorator_func(expression, obj)

            # ----------------------------------------------------------------------

            decorator_func = DecorateClass

        self._root: dict[str, Any]                      = {}
        self._object_stack: list[dict[str, Any]]        = [self._root, ]

        self._decorator_func                            = decorator_func

    # ----------------------------------------------------------------------
    @cached_property
    def root(self) -> dict[str, Any]:
        return self._root

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnExpression(
        self,
        expression: Expression,
    ) -> Iterator[VisitResult]:
        assert self._object_stack
        self._decorator_func(expression, self._object_stack[-1])

        if isinstance(expression, LeafExpression):
            value = expression.value
            if isinstance(value, Path):
                value = value.as_posix()

            self._object_stack[-1]["value"] = value

            yield VisitResult.SkipAll
            return

        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnExpressionDetails(
        self,
        expression: Expression,  # pylint: disable=unused-argument
    ) -> Iterator[VisitResult]:
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnExpressionChildren(
        self,
        expression: Expression,  # pylint: disable=unused-argument
        children_name: str,
        children: list[Expression],
    ) -> Iterator[VisitResult]:
        # Parse these items manually so that we can control how dicts are pushed and popped on
        # the object stack.
        child_results: list[dict[str, Any]] = []

        for child in children:
            self._object_stack.append({})
            child.Accept(self)
            child_results.append(self._object_stack.pop())

        assert self._object_stack
        self._object_stack[-1][children_name] = child_results

        yield VisitResult.SkipAll

    # ----------------------------------------------------------------------
    def __getattr__(
        self,
        method_name: str,
    ):
        index = method_name.find("Expression__")
        if index != -1 and index + len("Expression__") + 1 < len(method_name):
            index += len("Expression__")

            return lambda *args, **kwargs: self._OnDetailImpl(*args, **kwargs, detail_name=method_name[index:])

        return None

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnIdentifierExpression(
        self,
        expression: IdentifierExpression,
    ) -> Iterator[VisitResult]:
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnParseIncludeExpression(
        self,
        expression: ParseIncludeExpression,
    ) -> Iterator[VisitResult]:
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnParseIncludeComponentExpression(
        self,
        expression: ParseIncludeComponentExpression,
    ) -> Iterator[VisitResult]:
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnRootExpression(
        self,
        expression: RootExpression,  # pylint: disable=unused-argument
    ) -> Iterator[VisitResult]:
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    def _OnDetailImpl(
        self,
        expression_or_expressions: Expression | list[Expression],
        *,
        include_disabled: bool,
        detail_name: str,
    ) -> VisitResult:
        if isinstance(expression_or_expressions, list):
            get_result_func = lambda results: results
        else:
            get_result_func = lambda results: results[0]
            expression_or_expressions = [expression_or_expressions, ]

        results: list[Any] = []

        for expression in expression_or_expressions:
            if not include_disabled and expression.is_disabled__:
                continue

            self._object_stack.append({})
            expression.Accept(self)
            results.append(self._object_stack.pop())

        assert results
        assert self._object_stack
        self._object_stack[-1][detail_name] = get_result_func(results)

        return VisitResult.Continue

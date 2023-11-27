# ----------------------------------------------------------------------
# |
# |  ExpressionVisitor.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-01 09:44:37
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains types used with Expression visitors."""

import types

from abc import ABC, abstractmethod
from contextlib import contextmanager
from enum import auto, Flag
from typing import Iterable, Iterator, Union, TYPE_CHECKING

from Common_Foundation.Types import overridemethod

if TYPE_CHECKING:
    from TheLanguage.Parser.Expressions.Expression import Expression


# ----------------------------------------------------------------------
class VisitResult(Flag):
    """Result returned during visitation that controls the visitation of other Expressions."""

    Continue                                = 0

    SkipDetails                             = auto()
    SkipChildren                            = auto()

    Terminate                               = auto()

    # Amalgamations
    SkipAll                                 = SkipDetails | SkipChildren


# ----------------------------------------------------------------------
class ExpressionVisitor(ABC):
    """Abstract base class for a visitor that accepts Expressions."""

    # ----------------------------------------------------------------------
    @abstractmethod
    @contextmanager
    def OnExpression(
        self,
        expression: "Expression",
    ) -> Iterator[VisitResult]:
        raise Exception("Abstract method")  # pragma: no cover

    # ----------------------------------------------------------------------
    @abstractmethod
    @contextmanager
    def OnExpressionDetails(
        self,
        expression: "Expression",
    ) -> Iterator[VisitResult]:
        raise Exception("Abstract method")  # pragma: no cover

    # ----------------------------------------------------------------------
    @abstractmethod
    @contextmanager
    def OnExpressionChildren(
        self,
        expression: "Expression",
        children_name: str,
        children: Iterable["Expression"],
    ) -> Iterator[VisitResult]:
        raise Exception("Abstract method")  # pragma: no cover

    # ----------------------------------------------------------------------
    # Derived classes should implement the following methods:
    #
    #   @contextmanager On<Expression Name>(expression) -> Iterator[VisitResult]
    #   On<Expression Name>__<Detail Name>(expression_or_expressions, include_disabled) -> VisitResult
    #


# ----------------------------------------------------------------------
class ExpressionVisitorHelper(ExpressionVisitor):
    """Base class that can be used to make writing custom visitors easier."""

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnExpression(
        self,
        expression: "Expression",  # pylint: disable=unused-argument
    ) -> Iterator[VisitResult]:
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnExpressionDetails(
        self,
        expression: "Expression",  # pylint: disable=unused-argument
    ) -> Iterator[VisitResult]:
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnExpressionChildren(
        self,
        expression: "Expression",           # pylint: disable=unused-argument
        children_name: str,                 # pylint: disable=unused-argument
        children: Iterable["Expression"],   # pylint: disable=unused-argument
    ) -> Iterator[VisitResult]:
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    def __getattr__(
        self,
        method_name: str,
    ):
        if method_name.endswith("Expression"):
            return self.__class__._DefaultExpressionMethod  # pylint: disable=protected-access

        index = method_name.find("Expression__")
        if index != -1 and index + len("Expression__") + 1 < len(method_name):
            return types.MethodType(self.__class__._DefaultDetailMethod, self)  # pylint: disable=protected-access

        raise AttributeError(method_name)

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @staticmethod
    @contextmanager
    def _DefaultExpressionMethod(*args, **kwargs) -> Iterator[VisitResult]:  # pylint: disable=unused-argument
        yield VisitResult.Continue

    # ----------------------------------------------------------------------
    def _DefaultDetailMethod(
        self,
        expression_or_expressions: Union["Expression", list["Expression"]],
        *,
        include_disabled: bool,
    ) -> VisitResult:
        if isinstance(expression_or_expressions, list):
            for expression in expression_or_expressions:
                result = expression.Accept(
                    self,
                    include_disabled=include_disabled,
                )

                if result & VisitResult.Terminate:
                    return result
        else:
            result = expression_or_expressions.Accept(
                self,
                include_disabled=include_disabled,
            )

            if result & VisitResult.Terminate:
                return result

        return VisitResult.Continue

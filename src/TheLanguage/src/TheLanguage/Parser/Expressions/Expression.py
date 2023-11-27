# ----------------------------------------------------------------------
# |
# |  Expression.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-11-26 13:33:07
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the Expression and ExpressionType objects"""

from abc import ABC
from contextlib import contextmanager
from dataclasses import dataclass, fields, InitVar, field
from enum import auto, Enum
from typing import Any, Callable, Generator, Iterable, Iterator, Optional, Union

from Common_Foundation.Types import extensionmethod, overridemethod

from TheLanguage.Common.Region import Region

from TheLanguage.Parser.Visitors.ExpressionVisitor import ExpressionVisitor, ExpressionVisitorHelper, VisitResult


# ----------------------------------------------------------------------
class ExpressionType(Enum):
    """Classification of an expression"""

    # ----------------------------------------------------------------------
    # |
    # |  Public Types
    # |
    # ----------------------------------------------------------------------
    # The type is not currently known but will be determined based on the expression containing it.
    Unknown                                 = auto()

    # ----------------------------------------------------------------------
    # |  Compile-time Values
    Include                                 = auto()

    # Indicates the the Expression is applied at compile-time, but it isn't clear if this means
    # Configuration-time of TypeCustomization-time. The eventual type will be determined based on
    # the expression containing it.
    CompileTimeTemporary                    = auto()

    # The associated Expression can be used in the specification of basic compile-time types.
    Configuration                           = auto()

    # The associated Expressions can be used in the evaluation of compile-time constraints.
    TypeCustomizationTime                   = auto()

    # ----------------------------------------------------------------------
    # |  Standard Values
    Standard                                = auto()

    # ----------------------------------------------------------------------
    # |
    # |  Public Methods
    # |
    # ----------------------------------------------------------------------
    @classmethod
    def GetDominantType(
        cls,
        *expressions: "Expression",
    ) -> "ExpressionType":
        """Return the most dominant (highest value) expression type"""

        dominant_expression_type: Optional[ExpressionType] = None

        for expression in expressions:
            this_expression_type = expression.expression_type__

            if dominant_expression_type is None or this_expression_type.value > dominant_expression_type.value:
                dominant_expression_type = this_expression_type

        if dominant_expression_type is None:
            return cls.Unknown

        return dominant_expression_type

    # ----------------------------------------------------------------------
    @staticmethod
    def Compare(
        this: "ExpressionType",
        that: "ExpressionType",
    ) -> int:
        return this.value - that.value

    # ----------------------------------------------------------------------
    def __eq__(self, other) -> bool: return isinstance(other, ExpressionType) and self.__class__.Compare(self, other) == 0        # pylint: disable=multiple-statements
    def __ne__(self, other) -> bool: return not isinstance(other, ExpressionType) or self.__class__.Compare(self, other) != 0     # pylint: disable=multiple-statements
    def __lt__(self, other) -> bool: return isinstance(other, ExpressionType) and self.__class__.Compare(self, other) < 0         # pylint: disable=multiple-statements
    def __le__(self, other) -> bool: return isinstance(other, ExpressionType) and self.__class__.Compare(self, other) <= 0        # pylint: disable=multiple-statements
    def __gt__(self, other) -> bool: return isinstance(other, ExpressionType) and self.__class__.Compare(self, other) > 0         # pylint: disable=multiple-statements
    def __ge__(self, other) -> bool: return isinstance(other, ExpressionType) and self.__class__.Compare(self, other) >= 0        # pylint: disable=multiple-statements

    # ----------------------------------------------------------------------
    def IsConfiguration(self) -> bool:
        return self == ExpressionType.Configuration or self == ExpressionType.Unknown

    # ----------------------------------------------------------------------
    def IsCompileTime(self) -> bool:
        return self != ExpressionType.Standard and self != ExpressionType.Unknown


# ----------------------------------------------------------------------
@dataclass
class Expression(ABC):
    """Base class for all expressions encountered during the parsing process."""

    # ----------------------------------------------------------------------
    # |
    # |  Public Data
    # |
    # ----------------------------------------------------------------------
    expression_type__: ExpressionType
    region__: Region

    finalize: InitVar[bool]                 = field(kw_only=True, default=True)

    parent__: Optional["Expression"]        = field(init=False)

    _unique_id: Optional[tuple[Any, ...]]   = field(init=False)
    _disabled: bool                         = field(init=False)

    _finalize_func: Callable[[], None]      = field(init=False)

    # ----------------------------------------------------------------------
    # |
    # |  Public Methods
    # |
    # ----------------------------------------------------------------------
    def __post_init__(
        self,
        finalize: bool,
    ) -> None:
        self.parent__ = None

        self._unique_id = None
        self._disabled = False

        # ----------------------------------------------------------------------
        def Finalize():
            visitor = _UniqueIdVisitor(self)

            self.Accept(visitor)

            self._unique_id = visitor.unique_id

        # ----------------------------------------------------------------------

        self._finalize_func = Finalize

        if finalize:
            self._Finalize()

    # ----------------------------------------------------------------------
    @property
    def unique_id__(self) -> tuple[Any, ...]:
        assert self._unique_id is not None
        return self._unique_id

    @property
    def is_disabled__(self) -> bool:
        return self._disabled

    # ----------------------------------------------------------------------
    def Clone(self, **kwargs) -> "Expression":
        for field_value in fields(self.__class__):
            if (
                field_value.init
                and field_value.name != "finalize"
                and field_value.name not in kwargs
            ):
                kwargs[field_value.name] = getattr(self, field_value.name)

        return self.__class__(**kwargs)

    # ----------------------------------------------------------------------
    def __eq__(self, other) -> bool: return self.unique_id__ == other.unique_id__   # pylint: disable=multiple-statements
    def __ne__(self, other) -> bool: return self.unique_id__ != other.unique_id__   # pylint: disable=multiple-statements

    # ----------------------------------------------------------------------
    def Disable(self) -> None:
        assert self.is_disabled__ is False
        self._disabled = True

    # ----------------------------------------------------------------------
    def OverrideExpressionType(
        self,
        new_type: ExpressionType,
    ) -> None:
        if self.expression_type__ == ExpressionType.Unknown:
            # Literals are the only things that can be created as Unknown, so not need to
            # recurse (as there won't be any children).
            self.expression_type__ = new_type
            return

        # ----------------------------------------------------------------------
        class Visitor(ExpressionVisitorHelper):
            # ----------------------------------------------------------------------
            @staticmethod
            @overridemethod
            def OnPhrase(
                expression: Expression,
            ) -> Iterator[VisitResult]:
                if expression.expression_type__ == ExpressionType.CompileTimeTemporary:
                    expression.expression_type__ = new_type

                yield VisitResult.Continue

        # ----------------------------------------------------------------------

        self.Accept(Visitor())

    # ----------------------------------------------------------------------
    def Accept(
        self,
        visitor: ExpressionVisitor,
        *,
        include_disabled: bool=False,
    ) -> VisitResult:
        if self.is_disabled__ and not include_disabled:
            return VisitResult.Continue

        with visitor.OnExpression(self) as visit_result:
            if visit_result & VisitResult.Terminate:
                return visit_result

            if visit_result & VisitResult.SkipAll:
                return VisitResult.Continue

            method_name = "On{}".format(self.__class__.__name__)

            method = getattr(visitor, method_name, None)
            assert method is not None, method_name

            with method(self) as visit_result:
                if visit_result & VisitResult.Terminate:
                    return visit_result

                # Details
                if not visit_result & VisitResult.SkipDetails:
                    all_details = list(self._GenerateAcceptDetails())

                    if all_details:
                        with visitor.OnExpressionDetails(self) as details_visit_result:
                            if details_visit_result & VisitResult.Terminate:
                                return details_visit_result

                            if not details_visit_result & VisitResult.SkipDetails:
                                method_name_prefix = "On{}__".format(self.__class__.__name__)

                                for detail_name, detail_value in all_details:
                                    method_name = "{}{}".format(method_name_prefix, detail_name)

                                    method = getattr(visitor, method_name, None)
                                    assert method is not None, method_name

                                    detail_accept_result = method(
                                        detail_value,
                                        include_disabled=include_disabled,
                                    )

                                    if detail_accept_result & VisitResult.Terminate:
                                        return detail_accept_result

                                    if detail_accept_result & VisitResult.SkipDetails:
                                        break

                # Children
                if not visit_result & VisitResult.SkipChildren:
                    children_result = self._GetAcceptChildren()

                    if children_result:
                        children_name, children = children_result

                        with visitor.OnExpressionChildren(self, children_name, children) as children_visit_result:
                            if children_visit_result & VisitResult.Terminate:
                                return children_visit_result

                            if not children_visit_result & VisitResult.SkipChildren:
                                for child in children:
                                    child_accept_result = child.Accept(
                                        visitor,
                                        include_disabled=include_disabled,
                                    )

                                    if child_accept_result & VisitResult.Terminate:
                                        return child_accept_result

                                    if child_accept_result & VisitResult.SkipChildren:
                                        break

        return VisitResult.Continue

    # ----------------------------------------------------------------------
    # |
    # |  Protected Types
    # |
    # ----------------------------------------------------------------------
    _GenerateAcceptDetailsResultType        = Generator[
        tuple[str, Union["Expression", list["Expression"]]],
        None,
        None,
    ]

    _GetAcceptChildrenResultType            = Optional[tuple[str, Iterable["Expression"]]]

    # ----------------------------------------------------------------------
    # |
    # |  Protected Methods
    # |
    # ----------------------------------------------------------------------
    def _Finalize(self) -> None:
        self._finalize_func()

    # ----------------------------------------------------------------------
    # |
    # |  Private Methods
    # |
    # ----------------------------------------------------------------------
    @extensionmethod
    def _GetUniqueId(self) -> tuple[Any, ...]:
        raise Exception("This functionality should be implemented by derived classes when applicable ({}).".format(self.__class__))

    # ----------------------------------------------------------------------
    @extensionmethod
    def _GenerateAcceptDetails(self) -> "Expression._GenerateAcceptDetailsResultType":
        # Nothing by default
        if False:  # pylint: disable=using-constant-test
            yield

    # ----------------------------------------------------------------------
    @extensionmethod
    def _GetAcceptChildren(self) -> "Expression._GetAcceptChildrenResultType":
        # Nothing by default
        return None


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
class _UniqueIdVisitor(ExpressionVisitorHelper):
    # ----------------------------------------------------------------------
    def __init__(
        self,
        expression: Expression,
    ):
        self._target_expression                         = expression

        self._child_unique_ids: list[tuple[Any, ...]]   = []
        self._result: Optional[tuple[Any, ...]]         = None

    # ----------------------------------------------------------------------
    @property
    def unique_id(self) -> tuple[Any, ...]:
        assert self._result is not None
        return self._result

    # ----------------------------------------------------------------------
    @overridemethod
    @contextmanager
    def OnExpression(
        self,
        expression: Expression,
    ) -> Iterator[VisitResult]:
        if expression is self._target_expression:
            yield VisitResult.Continue

            if not self._child_unique_ids:
                # If here, we are looking at a terminal expression (one without children) and it
                # needs to provide its own unique id
                result = expression._GetUniqueId()  # pylint: disable=protected-access
            else:
                result = tuple(self._child_unique_ids)

            assert self._result is None
            self._result = (type(expression).__name__, ) + result

            return

        self._child_unique_ids.append(expression.unique_id__)

        # Do not parse the children of this expression as its unique id already takes that
        # information into account (however we still need to parse the details).
        yield VisitResult.SkipChildren

# ----------------------------------------------------------------------
# |
# |  RootExpression.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-01 15:22:43
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the RootExpression object"""

from dataclasses import dataclass
from typing import Any, ClassVar

from Common_Foundation.Types import overridemethod

from TheLanguage.Parser.Expressions.Expression import Expression, ExpressionType


# ----------------------------------------------------------------------
@dataclass
class RootExpression(Expression):
    """Root of all Expressions"""

    # ----------------------------------------------------------------------
    expression_type__: ClassVar[ExpressionType]         = ExpressionType.Unknown # BugBug

    children: list[Expression]

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @overridemethod
    def _GetUniqueId(self) -> tuple[Any, ...]:
        if not self.children:
            return (None, )

        return super(RootExpression, self)._GetUniqueId()

    # ----------------------------------------------------------------------
    @overridemethod
    def _GetAcceptChildren(self) -> Expression._GenerateChildrenResultType:
        return "children", self.children

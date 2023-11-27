# ----------------------------------------------------------------------
# |
# |  LeafExpression.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-07 16:18:49
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the LeafExpression object"""

from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from Common_Foundation.Types import overridemethod

from TheLanguage.Parser.Expressions.Expression import Expression


# ----------------------------------------------------------------------
LeafExpressionType                          = TypeVar("LeafExpressionType")

@dataclass
class LeafExpression(Generic[LeafExpressionType], Expression):
    """Expression with a single value member, typically used with leaves in abstract syntax trees."""

    # ----------------------------------------------------------------------
    value: LeafExpressionType

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @overridemethod
    def _GetUniqueId(self) -> tuple[Any, ...]:
        return (self.value, )

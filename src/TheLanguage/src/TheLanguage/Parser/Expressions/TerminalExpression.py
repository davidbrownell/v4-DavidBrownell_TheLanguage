# ----------------------------------------------------------------------
# |
# |  TerminalExpression.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-11-26 14:26:16
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the TerminalExpression object"""

from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from Common_Foundation.Types import overridemethod

from TheLanguage.Parser.Expressions.Expression import Expression


# ----------------------------------------------------------------------
TerminalExpressionType                      = TypeVar("TerminalExpressionType")

@dataclass
class TerminalExpression(Generic[TerminalExpressionType], Expression):
    """Expression with a single value member, typically used with leaves in an abstract syntax tree."""

    # ----------------------------------------------------------------------
    value: TerminalExpressionType

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @overridemethod
    def _GetUniqueId(self) -> tuple[Any, ...]:
        return (self.value, )

# ----------------------------------------------------------------------
# |
# |  ParseIncludeExpression.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-11-26 14:48:53
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains types used in the include process"""

from dataclasses import dataclass
from pathlib import Path
from typing import cast, ClassVar

from Common_Foundation.Types import overridemethod

from TheLanguage.Parser.Expressions.Expression import Expression, ExpressionType
from TheLanguage.Parser.Expressions.TerminalExpression import TerminalExpression


# ----------------------------------------------------------------------
@dataclass
class ParseIncludeImportItemExpression(Expression):
    """Item included as a part of an include expression"""

    # ----------------------------------------------------------------------
    expression_type__: ClassVar[ExpressionType]         = ExpressionType.Include

    name: TerminalExpression[str]
    reference_name: TerminalExpression[str]

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @overridemethod
    def _GenerateAcceptDetails(self) -> Expression._GenerateAcceptDetailsResultType:  # pragma: no cover
        yield "name", self.name
        yield "reference_name", self.reference_name


# ----------------------------------------------------------------------
@dataclass
class ParseIncludeExpression(Expression):
    """Includes content from another translation unit"""

    # ----------------------------------------------------------------------
    expression_type__: ClassVar[ExpressionType]         = ExpressionType.Include

    filename: TerminalExpression[Path]
    items: list[ParseIncludeImportItemExpression]

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @overridemethod
    def _GenerateAcceptDetails(self) -> Expression._GenerateAcceptDetailsResultType:  # pragma: no cover
        yield "filename", self.filename
        yield "items", cast(list[Expression], self.items)

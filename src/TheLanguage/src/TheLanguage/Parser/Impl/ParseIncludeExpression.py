# ----------------------------------------------------------------------
# |
# |  ParseParseIncludeExpression.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-07 16:12:05
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
from TheLanguage.Parser.Expressions.LeafExpression import LeafExpression


# ----------------------------------------------------------------------
@dataclass
class ParseIncludeFileExpression(LeafExpression[str]):
    """Contextual information associated with an include expression where the include content is a file"""

    # ----------------------------------------------------------------------
    expression_type__: ClassVar[ExpressionType]         = ExpressionType.Unknown # BugBug


# ----------------------------------------------------------------------
@dataclass
class ParseIncludeComponentExpression(Expression):
    """Specific component within a file processed as a part of an include statement"""

    # ----------------------------------------------------------------------
    expression_type__: ClassVar[ExpressionType]         = ExpressionType.Unknown # BugBug

    name: LeafExpression[str]
    reference_name: LeafExpression[str]

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @overridemethod
    def _GenerateAcceptDetails(self) -> Expression._GenerateAcceptDetailsResultType:
        yield "name", self.name
        yield "reference_name", self.reference_name


# ----------------------------------------------------------------------
@dataclass
class ParseIncludeExpression(Expression):
    """Includes content from another translation unit"""

    # ----------------------------------------------------------------------
    expression_type__: ClassVar[ExpressionType]         = ExpressionType.Unknown # BugBug

    filename: LeafExpression[Path]
    context: ParseIncludeFileExpression | list[ParseIncludeComponentExpression]

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @overridemethod
    def _GenerateAcceptDetails(self) -> Expression._GenerateAcceptDetailsResultType:  # pragma: no cover
        yield "filename", self.filename
        yield "context", self.context  # type: ignore

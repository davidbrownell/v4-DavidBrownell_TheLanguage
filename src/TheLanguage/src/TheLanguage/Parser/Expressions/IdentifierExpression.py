# ----------------------------------------------------------------------
# |
# |  IdentifierExpression.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-11-27 06:39:43
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the IdentifierExpression object"""

from dataclasses import dataclass

from TheLanguage.Parser.Expressions.TerminalExpression import TerminalExpression


# ----------------------------------------------------------------------
@dataclass
class IdentifierExpression(TerminalExpression[str]):
    """An identifier"""

    # All functionality is implemented via TerminalExpression[str],
    # but this needs to be defined as a class rather than type assignment
    # to ensure that isinstance statements work as expected.
    pass

# ----------------------------------------------------------------------
# |
# |  IdentifierExpression.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-07 11:20:40
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
from enum import auto, Enum
from typing import Optional

from Common_Foundation.Types import overridemethod

from TheLanguage.Parser.Expressions.LeafExpression import LeafExpression


# ----------------------------------------------------------------------
class IdentifierType(Enum):
    """Described the type of identifier"""

    Unknown                                 = auto()
    File                                    = auto()
    Component                               = auto()
    Function                                = auto()
    Template                                = auto()
    Type                                    = auto()
    Variable                                = auto()


# ----------------------------------------------------------------------
@dataclass
class IdentifierExpression(LeafExpression[str]):
    """Represents an identifier"""

    # ----------------------------------------------------------------------
    identifier_type: IdentifierType

    # ----------------------------------------------------------------------
    def Validate(
        self,
        explicit_identifier_type: Optional[IdentifierType]=None,
    ) -> None:
        if explicit_identifier_type is not None:
            if self.identifier_type != IdentifierType.Unknown:
                raise ValueError("'explicit_identifier_type' may only be provided with 'identifier_type' is Unknown.")

            identifier_type = explicit_identifier_type
        else:
            identifier_type = self.identifier_type

        assert identifier_type != IdentifierType.Unknown

        if identifier_type == IdentifierType.File:
            pass # BugBug
        elif identifier_type == IdentifierType.Component:
            pass # BugBug
        elif identifier_type == IdentifierType.Function:
            pass # BugBug
        elif identifier_type == IdentifierType.Template:
            pass # BugBug
        elif identifier_type == IdentifierType.Type:
            pass # BugBug
        elif identifier_type == IdentifierType.Variable:
            pass # BugBug
        else:
            assert False, identifier_type  # pragma: no cover

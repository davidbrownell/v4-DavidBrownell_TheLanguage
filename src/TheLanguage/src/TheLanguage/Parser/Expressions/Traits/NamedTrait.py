# ----------------------------------------------------------------------
# |
# |  NamedTrait.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-01 15:28:56
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the NamedTrait object"""

from dataclasses import dataclass, field

from TheLanguage.Parser.Expressions.Common.VisibilityModifier import VisibilityModifier


# ----------------------------------------------------------------------
@dataclass(frozen=True)
class NamedTrait(object):
    """Used by Expressions that add names to the active namespace."""

    # ----------------------------------------------------------------------
    name: str
    visibility: VisibilityModifier

    allow_name_to_be_duplicated__: bool     = field(init=False, default=False)

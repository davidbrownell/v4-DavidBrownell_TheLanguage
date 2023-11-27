# ----------------------------------------------------------------------
# |
# |  VisibilityModifier.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-01 15:25:21
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the VisibilityModifier object"""

from enum import auto, Enum


# ----------------------------------------------------------------------
class VisibilityModifier(Enum):
    Private                                 = auto()
    Protected                               = auto()
    Internal                                = auto()
    Public                                  = auto()

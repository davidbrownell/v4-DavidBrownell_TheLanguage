# ----------------------------------------------------------------------
# |
# |  Region.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-11-24 10:52:24
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the Region object"""

import inspect

from dataclasses import dataclass
from functools import cached_property
from pathlib import Path
from typing import Union

from TheLanguage.Common.Location import Location
from TheLanguage.Common.Range import Range


# ----------------------------------------------------------------------
@dataclass(frozen=True)
class Region(Range):
    """Range that includes source file information"""

    # ----------------------------------------------------------------------
    filename: Path

    # ----------------------------------------------------------------------
    @classmethod
    def Create(
        cls,
        filename: Path,
        begin_line: int,
        begin_column: int,
        end_line: int,
        end_column: int,
    ) -> "Region":
        return cls.CreateFromLocation(
            filename,
            Location(begin_line, begin_column),
            Location(end_line, end_column),
        )

    # ----------------------------------------------------------------------
    @classmethod
    def CreateFromLocation(
        cls,
        filename: Path,
        begin: Location,
        end: Location,
    ) -> "Region":
        return cls(begin, end, filename)

    # ----------------------------------------------------------------------
    @classmethod
    def CreateFromCode(
        cls,
        *,
        callstack_offset: int=0,
    ) -> "Region":
        frame = inspect.stack()[callstack_offset + 1][0]
        line = frame.f_lineno

        return cls(Location(line, line), Location(line, line), Path(frame.f_code.co_filename))

    # ----------------------------------------------------------------------
    def __str__(self) -> str:
        return self._string

    # ----------------------------------------------------------------------
    @staticmethod
    def Compare(
        this: "Region", # type: ignore
        that: "Region", # type: ignore
    ) -> int:
        if this.filename != that.filename:
            return -1 if this.filename < that.filename else 1

        return Range.Compare(this, that)

    # ----------------------------------------------------------------------
    def __eq__(self, other) -> bool: return isinstance(other, Region) and self.__class__.Compare(self, other) == 0        # pylint: disable=multiple-statements
    def __ne__(self, other) -> bool: return not isinstance(other, Region) or self.__class__.Compare(self, other) != 0     # pylint: disable=multiple-statements
    def __lt__(self, other) -> bool: return isinstance(other, Region) and self.__class__.Compare(self, other) < 0         # pylint: disable=multiple-statements
    def __le__(self, other) -> bool: return isinstance(other, Region) and self.__class__.Compare(self, other) <= 0        # pylint: disable=multiple-statements
    def __gt__(self, other) -> bool: return isinstance(other, Region) and self.__class__.Compare(self, other) > 0         # pylint: disable=multiple-statements
    def __ge__(self, other) -> bool: return isinstance(other, Region) and self.__class__.Compare(self, other) >= 0        # pylint: disable=multiple-statements

    # ----------------------------------------------------------------------
    def __contains__(
        self,
        location_range_or_region: Union[Location, Range, "Region"],
    ) -> bool:
        if isinstance(location_range_or_region, Region) and self.filename != location_range_or_region.filename:
            return False

        return super(Region, self).__contains__(location_range_or_region)

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @cached_property
    def _string(self) -> str:
        return "{}, {}".format(self.filename.as_posix(), super(Region, self)._string)

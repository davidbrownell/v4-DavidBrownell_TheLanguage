# ----------------------------------------------------------------------
# |
# |  Region.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-07-26 11:49:01
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

from .Range import Location, Range


# ----------------------------------------------------------------------
@dataclass(frozen=True)
class Region(Range):
    """Range within a source file"""

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
        return cls.CreateFromLocations(
            filename,
            Location(begin_line, begin_column),
            Location(end_line, end_column),
        )

    # ----------------------------------------------------------------------
    @classmethod
    def CreateFromLocations(
        cls,
        filename: Path,
        begin_location: Location,
        end_location: Location,
    ) -> "Region":
        return cls(begin_location, end_location, filename)

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
    @classmethod
    def Compare(
        cls,
        this: "Region",
        that: "Region",
    ) -> int:
        if this.filename != that.filename:
            return -1 if this.filename < that.filename else 1

        result = super(Region, cls).Compare(this, that)
        if result != 0:
            return result

        return 0

    # ----------------------------------------------------------------------
    def __eq__(self, other): return self.__class__.Compare(self, other) == 0    # pylint: disable=multiple-statements
    def __ne__(self, other): return self.__class__.Compare(self, other) != 0    # pylint: disable=multiple-statements
    def __lt__(self, other): return self.__class__.Compare(self, other) < 0     # pylint: disable=multiple-statements
    def __le__(self, other): return self.__class__.Compare(self, other) <= 0    # pylint: disable=multiple-statements
    def __gt__(self, other): return self.__class__.Compare(self, other) > 0     # pylint: disable=multiple-statements
    def __ge__(self, other): return self.__class__.Compare(self, other) >= 0    # pylint: disable=multiple-statements

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

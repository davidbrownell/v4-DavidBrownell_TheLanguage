# ----------------------------------------------------------------------
# |
# |  Range_UnitTest.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-07-26 12:43:44
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Unit tests for Location.py"""

import re
import sys

from pathlib import Path
from unittest.mock import MagicMock as Mock

import pytest

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx


# ----------------------------------------------------------------------
sys.path.insert(0, str(PathEx.EnsureDir(Path(__file__).parent.parent.parent.parent)))
with ExitStack(lambda: sys.path.pop(0)):
    from TheLanguage.Common.Range import Location, Range


# ----------------------------------------------------------------------
def test_Standard():
    begin = Location(1, 2)
    end = Location(30, 40)

    r = Range(begin, end)

    assert r.begin is begin
    assert r.end is end


# ----------------------------------------------------------------------
def test_InvalidRange():
    with pytest.raises(
        ValueError,
        match=re.escape("Invalid end"),
    ):
        Range(Location(10, 1), Location(1, 1))


# ----------------------------------------------------------------------
def test_String():
    assert str(Range(Location(1, 2), Location(3, 4))) == "Ln 1, Col 2 -> Ln 3, Col 4"


# ----------------------------------------------------------------------
def test_Compare():
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(30, 40))) == 0

    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(1, 20), Location(30, 40))) != 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 2), Location(30, 40))) != 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(25, 40))) != 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(30, 4))) != 0

    assert Range.Compare(Range(Location(1, 20), Location(30, 40)), Range(Location(10, 20), Location(30, 40))) < 0
    assert Range.Compare(Range(Location(10, 2), Location(30, 40)), Range(Location(10, 20), Location(30, 40))) < 0
    assert Range.Compare(Range(Location(10, 20), Location(25, 40)), Range(Location(10, 20), Location(30, 40))) < 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 4)), Range(Location(10, 20), Location(30, 40))) < 0

    assert Range.Compare(Range(Location(1, 20), Location(30, 40)), Range(Location(10, 20), Location(30, 40))) <= 0
    assert Range.Compare(Range(Location(10, 2), Location(30, 40)), Range(Location(10, 20), Location(30, 40))) <= 0
    assert Range.Compare(Range(Location(10, 20), Location(25, 40)), Range(Location(10, 20), Location(30, 40))) <= 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 4)), Range(Location(10, 20), Location(30, 40))) <= 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(30, 40))) <= 0

    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(1, 20), Location(30, 40))) > 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 2), Location(30, 40))) > 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(25, 40))) > 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(30, 4))) > 0

    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(1, 20), Location(30, 40))) >= 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 2), Location(30, 40))) >= 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(25, 40))) >= 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(30, 4))) >= 0
    assert Range.Compare(Range(Location(10, 20), Location(30, 40)), Range(Location(10, 20), Location(30, 40))) == 0


# ----------------------------------------------------------------------
def test_ComparisonOperators():
    assert Range(Location(10, 20), Location(30, 40)) == Range(Location(10, 20), Location(30, 40))

    assert Range(Location(10, 2), Location(30, 40)) < Range(Location(10, 20), Location(30, 40))

    assert Range(Location(10, 2), Location(30, 40)) <= Range(Location(10, 20), Location(30, 40))
    assert Range(Location(10, 20), Location(30, 40)) <= Range(Location(10, 20), Location(30, 40))

    assert Range(Location(10, 20), Location(31, 40)) > Range(Location(10, 20), Location(30, 40))

    assert Range(Location(10, 20), Location(31, 40)) >= Range(Location(10, 20), Location(30, 40))
    assert Range(Location(10, 20), Location(30, 40)) >= Range(Location(10, 20), Location(30, 40))


# ----------------------------------------------------------------------
class TestContains(object):
    # ----------------------------------------------------------------------
    def test_Location(self):
        the_range = Range(Location(10, 20), Location(30, 40))

        assert Location(10, 20) in the_range
        assert Location(30, 40) in the_range
        assert Location(10, 25) in the_range
        assert Location(22, 1) in the_range

        assert Location(10, 1) not in the_range
        assert Location(1, 1) not in the_range
        assert Location(30, 41) not in the_range
        assert Location(40, 1) not in the_range

    # ----------------------------------------------------------------------
    def test_Range(self):
        the_range = Range(Location(10, 20), Location(30, 40))

        assert Range(Location(10, 20), Location(30, 40)) in the_range
        assert Range(Location(11, 20), Location(30, 40)) in the_range
        assert Range(Location(10, 20), Location(29, 40)) in the_range
        assert Range(Location(10, 21), Location(30, 40)) in the_range
        assert Range(Location(10, 20), Location(30, 22)) in the_range
        assert Range(Location(15, 1), Location(20, 1)) in the_range

        assert Range(Location(1, 20), Location(30, 40)) not in the_range
        assert Range(Location(1, 20), Location(7, 40)) not in the_range
        assert Range(Location(1, 20), Location(35, 40)) not in the_range

        assert Range(Location(10, 20), Location(50, 40)) not in the_range
        assert Range(Location(15, 20), Location(50, 40)) not in the_range
        assert Range(Location(50, 20), Location(60, 40)) not in the_range

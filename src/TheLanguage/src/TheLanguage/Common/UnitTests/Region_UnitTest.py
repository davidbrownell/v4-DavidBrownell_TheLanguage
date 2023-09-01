# ----------------------------------------------------------------------
# |
# |  Region_UnitTest.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-07-31 15:27:35
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Unit tests for Region.py"""

import inspect
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
    from TheLanguage.Common.Region import Location, Range, Region


# ----------------------------------------------------------------------
def test_Standard():
    file_mock = Mock()
    begin = Location(1, 2)
    end = Location(3, 4)

    r = Region(begin, end, file_mock)

    assert r.begin is begin
    assert r.end is end
    assert r.filename is file_mock


# ----------------------------------------------------------------------
def test_Create():
    file_mock = Mock()

    r = Region.Create(file_mock, 1, 2, 3, 4)

    assert r.filename is file_mock
    assert r.begin.line == 1
    assert r.begin.column == 2
    assert r.end.line == 3
    assert r.end.column == 4


# ----------------------------------------------------------------------
def test_CreateFromCode():
    frame = inspect.stack()[0][0]
    line = frame.f_lineno
    filename = Path(frame.f_code.co_filename)

    r = Region.CreateFromCode()

    expected_line = line + 3 # The call to CreateFromCode in this function is 3 lines below the call to inspect.stack()

    assert r.filename == filename
    assert r.begin.line == expected_line
    assert r.end.line == expected_line


# ----------------------------------------------------------------------
def test_InvalidRange():
    with pytest.raises(
        ValueError,
        match=re.escape("Invalid end"),
    ):
        Region(Location(10, 1), Location(1, 1), Mock())


# ----------------------------------------------------------------------
def test_String():
    assert str(Region(Location(1, 2), Location(3, 4), Path("the_filename"))) == "the_filename <Ln 1, Col 2 -> Ln 3, Col 4>"


# ----------------------------------------------------------------------
def test_Compare():
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) == 0

    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename1")), Region(Location(10, 20), Location(30, 40), Path("filename2"))) != 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(1, 20), Location(30, 40), Path("filename"))) != 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 2), Location(30, 40), Path("filename"))) != 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(25, 40), Path("filename"))) != 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 4), Path("filename"))) != 0

    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename0")), Region(Location(10, 20), Location(30, 40), Path("filename1"))) < 0
    assert Region.Compare(Region(Location(1, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) < 0
    assert Region.Compare(Region(Location(10, 2), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) < 0
    assert Region.Compare(Region(Location(10, 20), Location(25, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) < 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 4), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) < 0

    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename0")), Region(Location(10, 20), Location(30, 40), Path("filename1"))) <= 0
    assert Region.Compare(Region(Location(1, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) <= 0
    assert Region.Compare(Region(Location(10, 2), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) <= 0
    assert Region.Compare(Region(Location(10, 20), Location(25, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) <= 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 4), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) <= 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) <= 0

    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename1")), Region(Location(10, 20), Location(30, 40), Path("filename0"))) > 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(1, 20), Location(30, 40), Path("filename"))) > 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 2), Location(30, 40), Path("filename"))) > 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(25, 40), Path("filename"))) > 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 4), Path("filename"))) > 0

    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename1")), Region(Location(10, 20), Location(30, 40), Path("filename0"))) >= 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(1, 20), Location(30, 40), Path("filename"))) >= 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 2), Location(30, 40), Path("filename"))) >= 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(25, 40), Path("filename"))) >= 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 4), Path("filename"))) >= 0
    assert Region.Compare(Region(Location(10, 20), Location(30, 40), Path("filename")), Region(Location(10, 20), Location(30, 40), Path("filename"))) == 0


# ----------------------------------------------------------------------
def test_ComparisonOperators():
    assert Region(Location(10, 20), Location(30, 40), Path("filename")) == Region(Location(10, 20), Location(30, 40), Path("filename"))

    assert Region(Location(10, 2), Location(30, 40), Path("filename")) < Region(Location(10, 20), Location(30, 40), Path("filename"))
    assert Region(Location(10, 20), Location(10, 20), Path("filename0")) < Region(Location(10, 20), Location(10, 20), Path("filename1"))

    assert Region(Location(10, 2), Location(30, 40), Path("filename")) <= Region(Location(10, 20), Location(30, 40), Path("filename"))
    assert Region(Location(10, 20), Location(30, 40), Path("filename")) <= Region(Location(10, 20), Location(30, 40), Path("filename"))
    assert Region(Location(10, 20), Location(10, 20), Path("filename")) <= Region(Location(10, 20), Location(30, 40), Path("FILENAME"))

    assert Region(Location(10, 20), Location(31, 40), Path("filename")) > Region(Location(10, 20), Location(30, 40), Path("filename"))
    assert Region(Location(10, 20), Location(10, 20), Path("FILENAME1")) > Region(Location(10, 20), Location(10, 20), Path("filename0"))

    assert Region(Location(10, 20), Location(31, 40), Path("filename")) >= Region(Location(10, 20), Location(30, 40), Path("filename"))
    assert Region(Location(10, 20), Location(30, 40), Path("filename")) >= Region(Location(10, 20), Location(30, 40), Path("filename"))
    assert Region(Location(10, 20), Location(10, 20), Path("FILENAME")) >= Region(Location(10, 20), Location(10, 20), Path("filename"))


# ----------------------------------------------------------------------
class TestContains(object):
    # ----------------------------------------------------------------------
    def test_Location(self):
        the_range = Region(Location(10, 20), Location(30, 40), Path("filename"))

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
        the_range = Region(Location(10, 20), Location(30, 40), Path("filename"))

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

    # ----------------------------------------------------------------------
    def test_Region(self):
        the_range = Region(Location(10, 20), Location(30, 40), Path("filename"))

        assert Region(Location(10, 20), Location(11, 12), Path("filename")) in the_range
        assert Region(Location(10, 20), Location(11, 12), Path("filename1")) not in the_range

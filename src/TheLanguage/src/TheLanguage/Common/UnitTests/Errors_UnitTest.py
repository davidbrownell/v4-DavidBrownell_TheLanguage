# ----------------------------------------------------------------------
# |
# |  Errors_UnitTest.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-03 06:52:21
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Unit tests for Errors.py"""

import re
import sys

from enum import auto, Enum
from pathlib import Path
from unittest.mock import MagicMock as Mock

import pytest

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx


# ----------------------------------------------------------------------
sys.path.insert(0, str(PathEx.EnsureDir(Path(__file__).parent.parent.parent.parent)))
with ExitStack(lambda: sys.path.pop(0)):
    from TheLanguage.Common.Errors import *


# ----------------------------------------------------------------------
class MyEnum(Enum):
    A                                       = auto()
    B                                       = auto()
    C                                       = auto()


# ----------------------------------------------------------------------
MySingleLineError                           = CreateErrorType("Str: {s}; Path: {p}; List: {l}; Enum: {e}", s=str, p=Path, l=list[int], e=MyEnum)


# ----------------------------------------------------------------------
def test_Construct():
    region_mock = Mock()

    e = Error.Create("Hello", region_mock)

    assert e.message == "Hello"
    assert e.regions == [region_mock, ]


# ----------------------------------------------------------------------
def test_ConstructMultipleRegions():
    region_mock = Mock()

    e = Error.Create("world", [region_mock, region_mock])

    assert e.message == "world"
    assert e.regions == [region_mock, region_mock]


# ----------------------------------------------------------------------
def test_CreateAsException():
    region_mock = Mock()

    ex = Error.CreateAsException("!!!", region_mock)

    assert len(ex.errors) == 1
    assert ex.errors[0].message == "!!!"
    assert ex.errors[0].regions == [region_mock, ]


# ----------------------------------------------------------------------
def test_SingleLineStr():
    e = MySingleLineError.Create(
        Region.Create(Path("filename1"), 1, 2, 3, 4),
        "string value",
        Path("file value"),
        [10, 20, 30],
        MyEnum.C,
    )

    assert str(e) == "Str: string value; Path: file value; List: '10', '20', '30'; Enum: C (filename1, line 1, column 2 -> line 3, column 4)"


# ----------------------------------------------------------------------
def test_MultipleRegionsStr():
    e = MySingleLineError.Create(
        [
            Region.Create(Path("filename1"), 1, 2, 3, 4),
            Region.Create(Path("filename2"), 11, 22, 33, 44),
        ],
        "string value",
        Path("file value"),
        [10, 20, 30],
        MyEnum.C,
    )

    assert str(e) == textwrap.dedent(
        """\
        Str: string value; Path: file value; List: '10', '20', '30'; Enum: C

            - filename1, line 1, column 2 -> line 3, column 4
            - filename2, line 11, column 22 -> line 33, column 44
        """,
    )


# ----------------------------------------------------------------------
def test_MultilineStr():
    e = Error(
        textwrap.dedent(
            """\
            Line 1
            Line 2
            """,
        ),
        Region.Create(Path("filenameA"), 1, 22, 333, 4444),
    )

    assert str(e) == textwrap.dedent(
        """\
        Line 1
        Line 2

            - filenameA, line 1, column 22 -> line 333, column 4444
        """,
    )

# ----------------------------------------------------------------------
# |
# |  TheLanguageException_UnitTest.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-07-26 12:47:10
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Unit tests for TheLanguageException.py"""

import sys
import textwrap

from enum import auto, Enum
from pathlib import Path
from unittest.mock import MagicMock as Mock

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx


# ----------------------------------------------------------------------
sys.path.insert(0, str(PathEx.EnsureDir(Path(__file__).parent.parent.parent.parent)))
with ExitStack(lambda: sys.path.pop(0)):
    from TheLanguage.Common.TheLanguageException import TheLanguageException, CreateExceptionType, Region


# ----------------------------------------------------------------------
def test_StrSingleLine():
    Exception1 = CreateExceptionType("This is a test")

    # Single Range
    assert str(Exception1(Region.Create(Path("filename1"), 1, 2, 3, 4))) == textwrap.dedent(
        """\
        This is a test (filename1 <Ln 1, Col 2 -> Ln 3, Col 4>)
        """,
    ).rstrip()

    # Multiple Range
    assert str(
        Exception1(
            [
                Region.Create(Path("filename2"), 10, 20, 30, 40),
                Region.Create(Path("filename3"), 100, 200, 300, 400),
            ],
        ),
    ) == textwrap.dedent(
        """\
        This is a test

            - filename2 <Ln 10, Col 20 -> Ln 30, Col 40>
            - filename3 <Ln 100, Col 200 -> Ln 300, Col 400>
        """,
    )


# ----------------------------------------------------------------------
def test_StrMultiLine():
    Exception2 = CreateExceptionType("This is\na test.")

    # Single Range
    assert str(Exception2(Region.Create(Path("filename1"), 1, 2, 3, 4))) == textwrap.dedent(
        """\
        This is
        a test.

            - filename1 <Ln 1, Col 2 -> Ln 3, Col 4>
        """,
    )

    # Multiple Range
    assert str(
        Exception2(
            [
                Region.Create(Path("filename2"), 10, 20, 30, 40),
                Region.Create(Path("filename3"), 100, 200, 300, 400),
            ],
        ),
    ) == textwrap.dedent(
        """\
        This is
        a test.

            - filename2 <Ln 10, Col 20 -> Ln 30, Col 40>
            - filename3 <Ln 100, Col 200 -> Ln 300, Col 400>
        """,
    )


# ----------------------------------------------------------------------
def test_CreateExceptionTypeBasic():
    assert str(CreateExceptionType("Hello {world}", world=str)(
        Region.Create(Path("filenameA"), 1, 2, 3, 4),
        "WORLD",
    )) == textwrap.dedent(
        """\
        Hello WORLD (filenameA <Ln 1, Col 2 -> Ln 3, Col 4>)
        """,
    ).rstrip()


# ----------------------------------------------------------------------
def test_CreateExceptionTypeMultipleArgs():
    assert str(CreateExceptionType("Hello {world} x{times}", world=str, times=int)(
        Region.Create(Path("filenameA"), 1, 2, 3, 4),
        "wOrLd",
        2,
    )) == textwrap.dedent(
        """\
        Hello wOrLd x2 (filenameA <Ln 1, Col 2 -> Ln 3, Col 4>)
        """,
    ).rstrip()


# ----------------------------------------------------------------------
def test_CreateExceptionTypeList():
    assert str(CreateExceptionType("List: {l}", l=list[str])(
        Region.Create(Path("filenameA"), 1, 2, 3, 4),
        ["one", "two", "three"],
    )) == textwrap.dedent(
        """\
        List: 'one', 'two', 'three' (filenameA <Ln 1, Col 2 -> Ln 3, Col 4>)
        """,
    ).rstrip()


# ----------------------------------------------------------------------
def test_CreateExceptionTypeEnum():
    # ----------------------------------------------------------------------
    class MyEnum(Enum):
        A = auto()
        B = auto()

    # ----------------------------------------------------------------------

    assert str(CreateExceptionType("Enum: {value}", value=MyEnum)(
        Region.Create(Path("filename"), 1, 22, 333, 4444),
        MyEnum.B,
    )) == textwrap.dedent(
        """\
        Enum: B (filename <Ln 1, Col 22 -> Ln 333, Col 4444>)
        """,
    ).rstrip()


# ----------------------------------------------------------------------
def test_CreateMethod():
    ex = CreateExceptionType("value: {v}", v=int).Create(
        Region.Create(Path("filename"), 10, 20, 30, 40),
        12,
    )

    assert ex.v == 12

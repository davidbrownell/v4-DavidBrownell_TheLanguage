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
def test_BugBug():
    try:
        try:
            try:
                s = "foo"
                s.does_not_exist()
            except:
                raise
        except:
            raise
    except Exception as ex:
        print(ExceptionError.Create(ex))
    assert False

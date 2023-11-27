# ----------------------------------------------------------------------
# |
# |  Errors.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-11-24 11:24:30
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains functionality associated with errors and Exceptions."""

import re
import textwrap
import traceback

from dataclasses import dataclass, field, InitVar, make_dataclass
from enum import Enum
from functools import singledispatch
from io import StringIO
from pathlib import Path
from typing import Type as PythonType

from Common_Foundation import TextwrapEx

from TheLanguage.Common.Region import Location, Region



# ----------------------------------------------------------------------
# |
# |  Public Types
# |
# ----------------------------------------------------------------------
@dataclass(frozen=True)
class Error(object):
    """Base class for all errors generated within TheLanguage"""

    # ----------------------------------------------------------------------
    message: str

    region_or_regions: InitVar[Region | list[Region]]
    regions: list[Region]                   = field(init=False)

    # ----------------------------------------------------------------------
    def __post_init__(
        self,
        region_or_regions: Region | list[Region],
    ) -> None:
        regions: list[Region] = []

        if isinstance(region_or_regions, list):
            regions = region_or_regions
        else:
            regions.append(region_or_regions)

        object.__setattr__(self, "regions", regions)

    # ----------------------------------------------------------------------
    @classmethod
    def Create(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    # ----------------------------------------------------------------------
    @classmethod
    def CreateAsException(cls, *args, **kwargs) -> "TheLanguageException":
        return TheLanguageException(cls.Create(*args, **kwargs))

    # ----------------------------------------------------------------------
    def __str__(self) -> str:
        if len(self.regions) == 1 and "\n" not in self.message:
            return "{} ({})".format(self.message, self.regions[0])

        return textwrap.dedent(
            """\
            {}

            {}
            """,
        ).format(
            self.message.rstrip(),
            "\n".join("    - {}".format(region) for region in self.regions),
        )


# ----------------------------------------------------------------------
@dataclass(frozen=True)
class ExceptionError(Error):
    """Errors based on a python Exception"""

    # ----------------------------------------------------------------------
    ex: Exception

    # ----------------------------------------------------------------------
    @classmethod
    def Create(
        cls,
        ex: Exception,
        *,
        include_callstack: bool=True,
    ) -> "ExceptionError":
        regions: list[Region] = []

        if include_callstack:
            # I haven't been able to find a reliable way to get the exception's callstack so it is being
            # parsed manually here. There has got to be a better way to do this.
            sink = StringIO()

            traceback.print_exception(ex, file=sink)
            sink_str = sink.getvalue()

            regex = re.compile(r"^\s*File \"(?P<filename>.+?)\", line (?P<line>\d+),.+$", re.MULTILINE)

            for line in sink_str.splitlines():
                match = regex.match(line)
                if not match:
                    continue

                line_number = int(match.group("line"))

                regions.append(
                    Region(
                        Location(line_number, 1),
                        Location(line_number, 1),
                        Path(match.group("filename")),
                    ),
                )

            regions.reverse()

        header = "Python Exception: "

        return ExceptionError(
            "{}{}".format(
                header,
                TextwrapEx.Indent(
                    str(ex),
                    len(header),
                    skip_first_line=True,
                ),
            ),
            regions,
            ex,
        )


# ----------------------------------------------------------------------
@dataclass(frozen=True)
class TheLanguageException(Exception):
    """Exception raised by functionality in TheLanguage"""

    # ----------------------------------------------------------------------
    error: InitVar[Error]
    errors: list[Error]                     = field(init=False)

    # ----------------------------------------------------------------------
    def __post_init__(
        self,
        error: Error,
    ):
        super(TheLanguageException, self).__init__(str(error))

        object.__setattr__(self, "errors", [error, ])


# ----------------------------------------------------------------------
# |
# |  Public Functions
# |
# ----------------------------------------------------------------------
def CreateErrorType(
    message_template: str,
    **args: PythonType,
) -> PythonType[Error]:
    dynamic_fields_class = make_dataclass(
        "DynamicFields",
        args.items(),
        bases=(Error, ),
        frozen=True,
    )

    # ----------------------------------------------------------------------
    @dataclass(frozen=True)
    class NewError(dynamic_fields_class):  # type: ignore
        # ----------------------------------------------------------------------
        message: str                        = field(init=False)

        # ----------------------------------------------------------------------
        def __post_init__(self, *args, **kwargs):
            super(NewError, self).__post_init__(*args, **kwargs)

            object.__setattr__(
                self,
                "message",
                message_template.format(
                    **{k: _ArgToString(v) for k, v in self.__dict__.items()},
                ),
            )

    # ----------------------------------------------------------------------

    return NewError


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
@singledispatch
def _ArgToString(value) -> str:
    return str(value)


# ----------------------------------------------------------------------
@_ArgToString.register
def _(
    value: str,
) -> str:
    return value


# ----------------------------------------------------------------------
@_ArgToString.register
def _(
    value: Path,
) -> str:
    return value.as_posix()


# ----------------------------------------------------------------------
@_ArgToString.register
def _(
    value: list,
) -> str:
    return ", ".join("'{}'".format(_ArgToString(v)) for v in value)


# ----------------------------------------------------------------------
@_ArgToString.register
def _(
    value: Enum,
) -> str:
    return value.name

# ----------------------------------------------------------------------
# |
# |  AntlrVisitorMixin.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-06 13:14:44
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the AntlrVisitorMixin object."""

import sys

from dataclasses import dataclass, field
from functools import cached_property
from pathlib import Path
from typing import Any, Callable, cast, Optional, Protocol

import antlr4

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx

from TheLanguage.AllErrors import *

from TheLanguage.Common.Range import Location, Range
from TheLanguage.Common.Region import Location, Region

from TheLanguage.Parser.Expressions.Expression import Expression
from TheLanguage.Parser.Expressions.IdentifierExpression import IdentifierExpression
from TheLanguage.Parser.Expressions.LeafExpression import LeafExpression
from TheLanguage.Parser.Expressions.RootExpression import RootExpression

from TheLanguage.Parser.Impl.ParseIncludeExpression import ParseIncludeExpression

# ----------------------------------------------------------------------
sys.path.insert(0, str(PathEx.EnsureDir(Path(__file__).parent / "GeneratedCode")))
with ExitStack(lambda: sys.path.pop(0)):
    from TheLanguageGrammarParser import TheLanguageGrammarParser           # type: ignore # pylint: disable=import-error
    from TheLanguageGrammarVisitor import TheLanguageGrammarVisitor         # type: ignore # pylint: disable=import-error


# ----------------------------------------------------------------------
class AntlrVisitorMixin(object):
    """Common functionality that does not change when ANTLR visitors are regenerated based on grammar changes."""

    # ----------------------------------------------------------------------
    # |
    # |  Public Types
    # |
    # ----------------------------------------------------------------------
    @dataclass(frozen=True)
    class CreateIncludeExpressionsSourceInfo(object):
        filename_or_directory: LeafExpression[Path]

        traverse_from_root: bool            = field(kw_only=True, default=False)  # True if source begins with slash
        force_directory: bool               = field(kw_only=True, default=False)  # True if source ends with slash
        is_relative: bool                   = field(kw_only=True, default=False)  # True if source contains ".." or "."

    # ----------------------------------------------------------------------
    @dataclass(frozen=True)
    class CreateIncludeExpressionsIncludeItem(object):
        region: Region

        element_name: IdentifierExpression
        reference_name: IdentifierExpression

    # ----------------------------------------------------------------------
    class CreateIncludeExpressionsFuncType(Protocol):
        def __call__(
            self,
            include_expression_region: Region,
            source: Optional["AntlrVisitorMixin.CreateIncludeExpressionsSourceInfo"],
            include_items: (
                Region                                                              # The item was '*'
                | list["AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem"]     # Items explicitly included
            ),
        ) -> list[ParseIncludeExpression]:
            ...  # pragma: no cover

    # ----------------------------------------------------------------------
    # |
    # |  Public Methods
    # |
    # ----------------------------------------------------------------------
    def __init__(
        self,
        filename: Path,
        on_progress_func: Callable[[int], None],
        create_include_statements_func: "AntlrVisitorMixin.CreateIncludeExpressionsFuncType",
        *,
        is_included_file: bool,
    ):
        self.filename                                   = filename
        self.is_included_file                           = is_included_file

        self._on_progress_func                          = on_progress_func
        self._create_include_statements_func            = create_include_statements_func

        self._current_line: int                         = 0
        self._stack: list[Any]                          = []

    # ----------------------------------------------------------------------
    @cached_property
    def root(self) -> RootExpression:
        if not self._stack:
            region = Region(Location(1, 1), Location(1, 1), self.filename)
        else:
            region = self._stack[0].region__

        return RootExpression.Create(region, self._stack)

    # ----------------------------------------------------------------------
    def CreateRegion(
        self,
        ctx: antlr4.ParserRuleContext,
    ) -> Range:
        assert isinstance(ctx.start, antlr4.Token), ctx.start
        assert isinstance(ctx.stop, antlr4.Token), ctx.stop

        if ctx.stop.type == TheLanguageGrammarParser.DEDENT:
            stop_line = ctx.stop.line
            stop_col = ctx.stop.column

        elif (
            ctx.stop.type == TheLanguageGrammarParser.NEWLINE
            and ctx.stop.text == "newLine"
        ):
            if ctx.stop.line == ctx.start.line:
                # This is the scenario where the statement is followed by a dedent followed by another
                # statement. We don't want the range of this item to overlap with the range of the next
                # item, so use the values as they are, even though it means that a statement that
                # terminates with a newline will not have that newline here.
                stop_line = ctx.stop.line
                stop_col = ctx.stop.column
            else:
                stop_line = ctx.stop.line
                stop_col = ctx.stop.column if ctx.stop.column == 0 else ctx.start.column

        else:
            content = ctx.stop.text
            stop_line = ctx.stop.line

            lines = content.split("\n")

            if ctx.stop.type == TheLanguageGrammarParser.NEWLINE:
                assert content.startswith("\n"), content
                assert len(lines) == 2, lines

            stop_col = len(lines[-1])

            if stop_line == ctx.stop.line:
                stop_col += ctx.stop.column

            stop_line += len(lines) - 1

        self._OnProgress(stop_line)

        return Region(
            Location(ctx.start.line, ctx.start.column + 1),
            Location(stop_line, stop_col + 1),
            self.filename,
        )

    # ----------------------------------------------------------------------
    # |
    # |  Protected Methods
    # |
    # ----------------------------------------------------------------------
    def _GetParent(self) -> Optional[Expression]:
        return self._stack[-1] if self._stack else None

    # ----------------------------------------------------------------------
    def _GetChildren(self, ctx) -> list[Any]:
        prev_num_stack_items = len(self._stack)

        cast(TheLanguageGrammarVisitor, self).visitChildren(ctx)

        results = self._stack[prev_num_stack_items:]

        del self._stack[prev_num_stack_items:]

        return results

    # ----------------------------------------------------------------------
    def _OnProgress(
        self,
        end_line: int,
    ) -> None:
        if end_line > self._current_line:
            self._current_line = end_line
            self._on_progress_func(self._current_line)
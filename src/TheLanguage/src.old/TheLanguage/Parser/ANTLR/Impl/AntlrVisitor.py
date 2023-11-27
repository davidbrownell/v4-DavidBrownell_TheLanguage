# ----------------------------------------------------------------------
# |
# |  AntlrVisitor.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-06 13:40:48
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains the AntlrVisitor object"""

import sys

from dataclasses import dataclass
from pathlib import Path

import antlr4

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx
from Common_Foundation.Types import overridemethod

from TheLanguage.Parser.ANTLR.Impl.AntlrVisitorMixin import AntlrVisitorMixin
from TheLanguage.Parser.Expressions.Expression import ExpressionType
from TheLanguage.Parser.Expressions.IdentifierExpression import IdentifierExpression
from TheLanguage.Parser.Expressions.LeafExpression import LeafExpression

# ----------------------------------------------------------------------
sys.path.insert(0, str(PathEx.EnsureDir(Path(__file__).parent.parent / "GeneratedCode")))
with ExitStack(lambda: sys.path.pop(0)):
    from TheLanguageGrammarParser import TheLanguageGrammarParser           # type: ignore # pylint: disable=import-error
    from TheLanguageGrammarVisitor import TheLanguageGrammarVisitor         # type: ignore # pylint: disable=import-error


# ----------------------------------------------------------------------
class AntlrVisitor(TheLanguageGrammarVisitor):
    # ----------------------------------------------------------------------
    # |  Common
    # ----------------------------------------------------------------------
    @overridemethod
    def visitIdentifier(self, ctx:TheLanguageGrammarParser.IdentifierContext):
        self._stack.append(
            IdentifierExpression.Create(
                ExpressionType.Unknown,
                self.CreateRegion(ctx),
                ctx.IDENTIFIER().symbol.text,
            ),
        )

    # ----------------------------------------------------------------------
    # |  Expressions
    # ----------------------------------------------------------------------
    @overridemethod
    def visitInclude_expression(self, ctx:TheLanguageGrammarParser.Include_expressionContext):
        children = self._GetChildren(ctx)
        assert len(children) >= 1, children

        if isinstance(children[0], AntlrVisitorMixin.CreateIncludeExpressionsSourceInfo):
            source_expression = children.pop(0)
        else:
            source_expression = None

        if len(children) == 1 and isinstance(children[0], LeafExpression):
            assert children[0].value == "*", children

            include_items = children[0].region__
        else:
            assert all(isinstance(child, AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem) for child in children), children

            include_items = children

        self._stack += self._create_include_statements_func(
            self.CreateRegion(ctx),
            source_expression,
            include_items,
        )

    # ----------------------------------------------------------------------
    @overridemethod
    def visitInclude_expression_source(self, ctx:TheLanguageGrammarParser.Include_expression_sourceContext):
        path_components: list[str] = []

        is_relative = (
            isinstance(ctx.children[0], antlr4.TerminalNode)
            and ctx.children[0].symbol.text in [".", "./"]
        )

        children = self._GetChildren(ctx)
        for child in children:
            if isinstance(child, str):
                assert child == "..", child

                path_components.append(child)
                is_relative = True

            elif isinstance(child, IdentifierExpression):
                AntlrVisitorMixin.ValidateAsFileOrDirectory(child)
                path_components.append(child.value)

            else:
                assert False, child  # pragma: no cover

        filename_or_directory = Path(*path_components)

        # ----------------------------------------------------------------------
        def IsSlash(
            child_index: int,
        ) -> bool:
            return (
                isinstance(ctx.children[child_index], antlr4.TerminalNode)
                and ctx.children[child_index].symbol.text == "/"
            )

        # ----------------------------------------------------------------------

        self._stack.append(
            AntlrVisitorMixin.CreateIncludeExpressionsSourceInfo(
                LeafExpression[Path](
                    ExpressionType.Unknown, # BugBug
                    self.CreateRegion(ctx),
                    filename_or_directory,
                ),
                traverse_from_root=IsSlash(0),
                force_directory=IsSlash(-1),
                is_relative=is_relative,
            ),
        )

    # ----------------------------------------------------------------------
    @overridemethod
    def visitInclude_expression_source_parent_dir(self, ctx:TheLanguageGrammarParser.Include_expression_source_parent_dirContext):
        self._stack.append("..")

    # ----------------------------------------------------------------------
    @overridemethod
    def visitInclude_expression_star(self, ctx:TheLanguageGrammarParser.Include_expression_starContext):
        self._stack.append(
            LeafExpression[str](
                ExpressionType.Unknown, # BugBug: Use of Unknown Expression type
                self.CreateRegion(ctx),
                "*",
            ),
        )

    # ----------------------------------------------------------------------
    @overridemethod
    def visitInclude_expression_element(self, ctx:TheLanguageGrammarParser.Include_expression_elementContext):
        children = self._GetChildren(ctx)

        num_children = len(children)
        assert 1 <= num_children <= 2, children

        assert isinstance(children[0], IdentifierExpression), children[0]
        element_name = children[0]

        if num_children > 1:
            assert isinstance(children[1], IdentifierExpression), children
            reference_name = children[1]
        else:
            reference_name = element_name # BugBug element_name.Clone()

        self._stack.append(
            AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem(
                self.CreateRegion(ctx),
                element_name,
                reference_name,
            ),
        )


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
@dataclass(frozen=True)
class _IncludeSource(object):
    from_source: Path
    force_directory: bool

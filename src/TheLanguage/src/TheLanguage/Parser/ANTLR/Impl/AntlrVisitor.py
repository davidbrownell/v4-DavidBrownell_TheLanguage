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

from dataclasses import dataclass, field
from pathlib import Path
from typing import cast, Optional

import antlr4

from Common_Foundation.ContextlibEx import ExitStack
from Common_Foundation import PathEx
from Common_Foundation.Types import overridemethod

from TheLanguage.Common.Region import Region

from TheLanguage.Parser.ANTLR.Impl.AntlrVisitorMixin import AntlrVisitorMixin

from TheLanguage.Parser.Expressions.Expression import ExpressionType
from TheLanguage.Parser.Expressions.IdentifierExpression import IdentifierExpression
from TheLanguage.Parser.Expressions.TerminalExpression import TerminalExpression

# ----------------------------------------------------------------------
sys.path.insert(0, str(PathEx.EnsureDir(Path(__file__).parent.parent / "GeneratedCode")))
with ExitStack(lambda: sys.path.pop(0)):
    from TheLanguageGrammarParser import TheLanguageGrammarParser           # type: ignore # pylint: disable=import-error
    from TheLanguageGrammarVisitor import TheLanguageGrammarVisitor         # type: ignore # pylint: disable=import-error


# ----------------------------------------------------------------------
class AntlrVisitor(AntlrVisitorMixin, TheLanguageGrammarVisitor):
    """Implements functionality based on the code generated by ANTLR"""

    # ----------------------------------------------------------------------
    # |  Common
    # ----------------------------------------------------------------------
    @overridemethod
    def visitIdentifier(self, ctx:TheLanguageGrammarParser.IdentifierContext):
        self._stack.append(
            IdentifierExpression(
                ExpressionType.Unknown,
                self.CreateRegion(ctx),
                ctx.IDENTIFIER().symbol.text,
            ),
        )

    # ----------------------------------------------------------------------
    # |  Expressions
    # ----------------------------------------------------------------------
    def visitImport_expression(self, ctx:TheLanguageGrammarParser.Import_expressionContext):
        data = _ImportExpressionData()

        self._stack.append(data)
        with ExitStack(self._stack.pop):
            self.visitChildren(ctx)

        if not data.from_components:
            data.from_components.append(
                TerminalExpression[str](
                    ExpressionType.Include,
                    self.CreateRegion(ctx),
                    ".",
                ),
            )

            assert data.from_directory_slash is None
            data.from_directory_slash = data.from_components[-1].Clone()

        # Validate the components
        path_components: list[str] = []
        processing_relative_paths = True

        for component in data.from_components:
            if component.value == ".":
                if path_components:
                    assert False, "BugBug 1"

            elif component.value == "..":
                if not processing_relative_paths:
                    assert False, "BugBug 2"

            else:
                processing_relative_paths = False

                AntlrVisitorMixin.ValidateAsFileOrDirectory(cast(IdentifierExpression, component))

            path_components.append(component.value)

        if data.from_directory_slash:
            for import_item in data.import_items:
                AntlrVisitorMixin.ValidateAsFileOrDirectory(import_item.element_name)
                AntlrVisitorMixin.ValidateAsFileOrDirectory(import_item.reference_name)

        from_info = AntlrVisitorMixin.CreateIncludeExpressionsFromInfo(
            TerminalExpression[Path](

                Region(
                    data.from_components[0].begin,
                    data.from_components[-1].end,
                    data.from_components[0].filename,
                ),
                Path(*path_components),
            )






        # BugBug: Process data

    # ----------------------------------------------------------------------
    def visitImport_expression_from_workspace_slash(self, ctx:TheLanguageGrammarParser.Import_expression_from_workspace_slashContext):
        cast(_ImportExpressionData, self._stack[-1]).from_workspace_slash = TerminalExpression[str](
            ExpressionType.Include,
            self.CreateRegion(ctx),
            "BugBug",
        )

    # ----------------------------------------------------------------------
    def visitImport_expression_from_component(self, ctx:TheLanguageGrammarParser.Import_expression_from_componentContext):
        children = self._GetChildren(ctx)
        assert len(children) == 1, len(children)

        cast(_ImportExpressionData, self._stack[-1]).from_components.append(children[0])

    # ----------------------------------------------------------------------
    def visitImport_expression_from_directory_slash(self, ctx:TheLanguageGrammarParser.Import_expression_from_directory_slashContext):
        cast(_ImportExpressionData, self._stack[-1]).from_directory_slash = TerminalExpression[str](
            ExpressionType.Include,
            self.CreateRegion(ctx),
            "BugBug",
        )

    # ----------------------------------------------------------------------
    def visitImport_expression_import_star(self, ctx:TheLanguageGrammarParser.Import_expression_import_starContext):
        cast(_ImportExpressionData, self._stack[-1]).import_star = TerminalExpression[str](
            ExpressionType.Include,
            self.CreateRegion(ctx),
            "BugBug",
        )

    # ----------------------------------------------------------------------
    def visitImport_expression_import_element(self, ctx:TheLanguageGrammarParser.Import_expression_import_elementContext):
        children = self._GetChildren(ctx)
        assert len(children) in [1, 2], len(children)

        element_name = children[0]

        if len(children) > 1:
            reference_name = children[1]
        else:
            reference_name = IdentifierExpression(
                element_name.expression_type__,
                element_name.region__,
                element_name.value,
            )

        cast(_ImportExpressionData, self._stack[-1]).import_items.append(
            AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem(
                self.CreateRegion(ctx),
                element_name,
                reference_name,
            ),
        )


# ----------------------------------------------------------------------
# |
# |  Private Types
# |
# ----------------------------------------------------------------------
@dataclass
class _ImportExpressionData(object):
    """Data populated when parsing import expressions"""

    # ----------------------------------------------------------------------
    from_workspace_slash: Optional[TerminalExpression[str]]                     = field(init=False, default=None)
    from_components: list[TerminalExpression[str]]                              = field(init=False, default_factory=list)
    from_directory_slash: Optional[TerminalExpression[str]]                     = field(init=False, default=None)

    import_star: Optional[TerminalExpression[str]]                              = field(init=False, default=None)
    import_items: list[AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem]   = field(init=False, default_factory=list)




    # BugBug @overridemethod
    # BugBug def visitInclude_expression(self, ctx:TheLanguageGrammarParser.Include_expressionContext):
    # BugBug     children = self._GetChildren(ctx)
    # BugBug     assert len(children) >= 1, children
    # BugBug
    # BugBug     if isinstance(children[0], AntlrVisitorMixin.CreateIncludeExpressionsFromInfo):
    # BugBug         from_expression = children.pop(0)
    # BugBug     else:
    # BugBug         from_expression = None
    # BugBug
    # BugBug     if len(children) == 1 and isinstance(children[0], TerminalExpression):
    # BugBug         assert children[0].value == "*", children
    # BugBug
    # BugBug         include_items = children[0].region__
    # BugBug     else:
    # BugBug         assert all(isinstance(child, AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem) for child in children), children
    # BugBug
    # BugBug         include_items = children
    # BugBug
    # BugBug     self._stack += self._create_include_statements_func(
    # BugBug         self.CreateRegion(ctx),
    # BugBug         from_expression,
    # BugBug         include_items,
    # BugBug     )
    # BugBug
    # BugBug # ----------------------------------------------------------------------
    # BugBug @overridemethod
    # BugBug def visitInclude_expression_source(self, ctx:TheLanguageGrammarParser.Include_expression_sourceContext):
    # BugBug     children = self._GetChildren(ctx)
    # BugBug     assert children
    # BugBug
    # BugBug     path_components: list[str] = []
    # BugBug     is_relative: Optional[Region] = None
    # BugBug     is_directory: Optional[Region] = None
    # BugBug     is_root: Optional[Region] = None
    # BugBug
    # BugBug     if len(children) == 1 and children[0].value == ".":
    # BugBug         is_relative = children[0].region__
    # BugBug         is_directory = children[0].region__
    # BugBug     else:
    # BugBug         if children[0].value == "./":
    # BugBug             is_relative = children[0].region__
    # BugBug             child_index_start = 1
    # BugBug         elif children[0].value == "/":
    # BugBug             is_root = children[0].region__
    # BugBug             child_index_start = 1
    # BugBug         else:
    # BugBug             child_index_start = 0
    # BugBug
    # BugBug         if len(children) > 1 and children[-1].value == "/":
    # BugBug             is_directory = children[-1].region__
    # BugBug             child_index_end = -2
    # BugBug         else:
    # BugBug             child_index_end = -1
    # BugBug
    # BugBug         for child in children[child_index_start:child_index_end]:
    # BugBug             if child.value != "..":
    # BugBug                 AntlrVisitorMixin.ValidateAsFileOrDirectory(child)
    # BugBug
    # BugBug             path_components.append(child.value)
    # BugBug
    # BugBug     filename_or_directory = Path(*path_components)
    # BugBug
    # BugBug     self._stack.append(
    # BugBug         AntlrVisitorMixin.CreateIncludeExpressionsFromInfo(
    # BugBug             TerminalExpression[Path](
    # BugBug                 ExpressionType.Include,
    # BugBug                 self.CreateRegion(ctx),
    # BugBug                 filename_or_directory,
    # BugBug             ),
    # BugBug             traverse_from_root=is_root,
    # BugBug             is_directory=is_directory,
    # BugBug             is_relative=is_relative,
    # BugBug         ),
    # BugBug     )
    # BugBug
    # BugBug # ----------------------------------------------------------------------
    # BugBug @overridemethod
    # BugBug def visitInclude_expression_source_working_dir(self, ctx:TheLanguageGrammarParser.Include_expression_source_working_dirContext):
    # BugBug     self._stack.append(
    # BugBug         TerminalExpression[str](
    # BugBug             ExpressionType.Include,
    # BugBug             self.CreateRegion(ctx),
    # BugBug             ctx.symbol.text,
    # BugBug         ),
    # BugBug     )
    # BugBug
    # BugBug # ----------------------------------------------------------------------
    # BugBug @overridemethod
    # BugBug def visitInclude_expression_source_dir_prefix(self, ctx:TheLanguageGrammarParser.Include_expression_source_dir_prefixContext):
    # BugBug     children = self._GetChildren(ctx)
    # BugBug     assert len(children) == 1
    # BugBug
    # BugBug     self._stack.append(
    # BugBug         TerminalExpression[str](
    # BugBug             ExpressionType.Include,
    # BugBug             self.CreateRegion(children[0]),
    # BugBug             children[0].symbol.text,
    # BugBug         ),
    # BugBug     )
    # BugBug
    # BugBug # ----------------------------------------------------------------------
    # BugBug @overridemethod
    # BugBug def visitInclude_expression_source_parent_dir(self, ctx:TheLanguageGrammarParser.Include_expression_source_parent_dirContext):
    # BugBug     self._stack.append(
    # BugBug         TerminalExpression[str](
    # BugBug             ExpressionType.Include,
    # BugBug             self.CreateRegion(ctx),
    # BugBug             ctx.symbol.text,
    # BugBug         ),
    # BugBug     )
    # BugBug
    # BugBug # ----------------------------------------------------------------------
    # BugBug @overridemethod
    # BugBug def visitInclude_expression_source_trailing_slash(self, ctx:TheLanguageGrammarParser.Include_expression_source_trailing_slashContext):
    # BugBug     self._stack.append(
    # BugBug         TerminalExpression[str](
    # BugBug             ExpressionType.Include,
    # BugBug             self.CreateRegion(ctx),
    # BugBug             self.symbol.text,
    # BugBug         ),
    # BugBug     )
    # BugBug
    # BugBug # ----------------------------------------------------------------------
    # BugBug @overridemethod
    # BugBug def visitInclude_expression_star(self, ctx:TheLanguageGrammarParser.Include_expression_starContext):
    # BugBug     self._stack.append(
    # BugBug         TerminalExpression[str](
    # BugBug             ExpressionType.Include,
    # BugBug             self.CreateRegion(ctx),
    # BugBug             ctx.symbol.text,
    # BugBug         ),
    # BugBug     )
    # BugBug
    # BugBug # ----------------------------------------------------------------------
    # BugBug @overridemethod
    # BugBug def visitInclude_expression_element(self, ctx:TheLanguageGrammarParser.Include_expression_elementContext):
    # BugBug     children = self._GetChildren(ctx)
    # BugBug
    # BugBug     num_children = len(children)
    # BugBug     assert 1 <= num_children <= 2, children
    # BugBug
    # BugBug     assert isinstance(children[0], IdentifierExpression), children[0]
    # BugBug     element_name = children[0]
    # BugBug
    # BugBug     if num_children > 1:
    # BugBug         assert isinstance(children[1], IdentifierExpression), children
    # BugBug         reference_name = children[1]
    # BugBug     else:
    # BugBug         reference_name = element_name # BugBug element_name.Clone()
    # BugBug
    # BugBug     self._stack.append(
    # BugBug         AntlrVisitorMixin.CreateIncludeExpressionsIncludeItem(
    # BugBug             self.CreateRegion(ctx),
    # BugBug             element_name,
    # BugBug             reference_name,
    # BugBug         ),
    # BugBug     )

# Generated from C:\Code\GitHub\davidbrownell\DavidBrownell\TheLanguage\src\TheLanguage\src\TheLanguage\Parser\ANTLR\Grammar\TheLanguageGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TheLanguageGrammarParser import TheLanguageGrammarParser
else:
    from TheLanguageGrammarParser import TheLanguageGrammarParser

# This class defines a complete generic visitor for a parse tree produced by TheLanguageGrammarParser.

class TheLanguageGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TheLanguageGrammarParser#entry_point__.
    def visitEntry_point__(self, ctx:TheLanguageGrammarParser.Entry_point__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#identifier.
    def visitIdentifier(self, ctx:TheLanguageGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#expression__.
    def visitExpression__(self, ctx:TheLanguageGrammarParser.Expression__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#include_expression.
    def visitInclude_expression(self, ctx:TheLanguageGrammarParser.Include_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#include_expression_source.
    def visitInclude_expression_source(self, ctx:TheLanguageGrammarParser.Include_expression_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#include_expression_source__.
    def visitInclude_expression_source__(self, ctx:TheLanguageGrammarParser.Include_expression_source__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#include_expression_source_parent_dir.
    def visitInclude_expression_source_parent_dir(self, ctx:TheLanguageGrammarParser.Include_expression_source_parent_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#include_expression_star.
    def visitInclude_expression_star(self, ctx:TheLanguageGrammarParser.Include_expression_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#include_expression_items__.
    def visitInclude_expression_items__(self, ctx:TheLanguageGrammarParser.Include_expression_items__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#include_expression_grouped_items__.
    def visitInclude_expression_grouped_items__(self, ctx:TheLanguageGrammarParser.Include_expression_grouped_items__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#include_expression_element.
    def visitInclude_expression_element(self, ctx:TheLanguageGrammarParser.Include_expression_elementContext):
        return self.visitChildren(ctx)



del TheLanguageGrammarParser
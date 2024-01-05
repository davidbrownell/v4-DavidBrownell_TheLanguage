# Generated from C:\Code\GitHub\davidbrownell\DavidBrownell\TheLanguage\src\TheLanguage\src\TheLanguage\Parser\ANTLR\TheLanguageGrammar.g4 by ANTLR 4.13.0
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


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression.
    def visitImport_expression(self, ctx:TheLanguageGrammarParser.Import_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_from__.
    def visitImport_expression_from__(self, ctx:TheLanguageGrammarParser.Import_expression_from__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_from_workspace_slash.
    def visitImport_expression_from_workspace_slash(self, ctx:TheLanguageGrammarParser.Import_expression_from_workspace_slashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_from_component.
    def visitImport_expression_from_component(self, ctx:TheLanguageGrammarParser.Import_expression_from_componentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_from_directory_slash.
    def visitImport_expression_from_directory_slash(self, ctx:TheLanguageGrammarParser.Import_expression_from_directory_slashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_import__.
    def visitImport_expression_import__(self, ctx:TheLanguageGrammarParser.Import_expression_import__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_import_star.
    def visitImport_expression_import_star(self, ctx:TheLanguageGrammarParser.Import_expression_import_starContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_import_grouped_items__.
    def visitImport_expression_import_grouped_items__(self, ctx:TheLanguageGrammarParser.Import_expression_import_grouped_items__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_import_items__.
    def visitImport_expression_import_items__(self, ctx:TheLanguageGrammarParser.Import_expression_import_items__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguageGrammarParser#import_expression_import_element.
    def visitImport_expression_import_element(self, ctx:TheLanguageGrammarParser.Import_expression_import_elementContext):
        return self.visitChildren(ctx)



del TheLanguageGrammarParser
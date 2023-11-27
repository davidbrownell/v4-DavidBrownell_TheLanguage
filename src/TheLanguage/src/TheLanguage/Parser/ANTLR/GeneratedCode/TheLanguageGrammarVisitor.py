# Generated from C:\Code\v4\DavidBrownell\TheLanguage\src\TheLanguage\src\TheLanguage\Parser\ANTLR\TheLanguageGrammar.g4 by ANTLR 4.13.0
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



del TheLanguageGrammarParser
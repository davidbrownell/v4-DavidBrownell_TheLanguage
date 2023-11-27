# Generated from C:\Code\v4\DavidBrownell\TheLanguage\src\TheLanguage\src\TheLanguage\Parser\ANTLR\TheLanguageGrammar.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,29,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,5,0,10,8,0,10,0,12,
        0,13,9,0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,26,0,11,1,0,0,0,2,22,1,0,0,0,4,24,
        1,0,0,0,6,26,1,0,0,0,8,10,5,3,0,0,9,8,1,0,0,0,10,13,1,0,0,0,11,9,
        1,0,0,0,11,12,1,0,0,0,12,17,1,0,0,0,13,11,1,0,0,0,14,16,3,4,2,0,
        15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,20,1,
        0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,23,5,12,0,0,23,
        3,1,0,0,0,24,25,3,6,3,0,25,5,1,0,0,0,26,27,5,1,0,0,27,7,1,0,0,0,
        2,11,17
    ]

class TheLanguageGrammarParser ( Parser ):

    grammarFileName = "TheLanguageGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'BugBug'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'['", "']'", 
                     "'from'", "'import'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "HORIZONTAL_WHITESPACE", 
                      "NEWLINE", "NESTED_NEWLINE", "LINE_CONTINUATION", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "INCLUDE_FROM", 
                      "INCLUDE_IMPORT", "IDENTIFIER", "INDENT", "DEDENT" ]

    RULE_entry_point__ = 0
    RULE_identifier = 1
    RULE_expression__ = 2
    RULE_include_expression = 3

    ruleNames =  [ "entry_point__", "identifier", "expression__", "include_expression" ]

    EOF = Token.EOF
    T__0=1
    HORIZONTAL_WHITESPACE=2
    NEWLINE=3
    NESTED_NEWLINE=4
    LINE_CONTINUATION=5
    LPAREN=6
    RPAREN=7
    LBRACK=8
    RBRACK=9
    INCLUDE_FROM=10
    INCLUDE_IMPORT=11
    IDENTIFIER=12
    INDENT=13
    DEDENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Entry_point__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TheLanguageGrammarParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TheLanguageGrammarParser.NEWLINE)
            else:
                return self.getToken(TheLanguageGrammarParser.NEWLINE, i)

        def expression__(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TheLanguageGrammarParser.Expression__Context)
            else:
                return self.getTypedRuleContext(TheLanguageGrammarParser.Expression__Context,i)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_entry_point__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry_point__" ):
                return visitor.visitEntry_point__(self)
            else:
                return visitor.visitChildren(self)




    def entry_point__(self):

        localctx = TheLanguageGrammarParser.Entry_point__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entry_point__)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 8
                self.match(TheLanguageGrammarParser.NEWLINE)
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 14
                self.expression__()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(TheLanguageGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TheLanguageGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = TheLanguageGrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(TheLanguageGrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include_expression(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expressionContext,0)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_expression__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression__" ):
                return visitor.visitExpression__(self)
            else:
                return visitor.visitChildren(self)




    def expression__(self):

        localctx = TheLanguageGrammarParser.Expression__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression__)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.include_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_include_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_expression" ):
                return visitor.visitInclude_expression(self)
            else:
                return visitor.visitChildren(self)




    def include_expression(self):

        localctx = TheLanguageGrammarParser.Include_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_include_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(TheLanguageGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






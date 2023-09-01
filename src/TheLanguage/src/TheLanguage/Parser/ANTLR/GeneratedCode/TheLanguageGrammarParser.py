# Generated from C:\Code\GitHub\davidbrownell\DavidBrownell\TheLanguage\src\TheLanguage\src\TheLanguage\Parser\ANTLR\TheLanguageGrammar.g4 by ANTLR 4.13.0
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
        4,1,20,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,
        1,3,3,3,43,8,3,1,3,1,3,1,3,1,3,3,3,49,8,3,1,3,4,3,52,8,3,11,3,12,
        3,53,1,4,1,4,3,4,58,8,4,1,4,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,
        1,4,3,4,69,8,4,3,4,71,8,4,1,5,1,5,3,5,75,8,5,1,6,1,6,1,7,1,7,1,8,
        1,8,1,8,5,8,84,8,8,10,8,12,8,87,9,8,1,8,3,8,90,8,8,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,3,10,99,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,
        18,20,0,1,1,0,2,3,103,0,25,1,0,0,0,2,36,1,0,0,0,4,38,1,0,0,0,6,42,
        1,0,0,0,8,70,1,0,0,0,10,74,1,0,0,0,12,76,1,0,0,0,14,78,1,0,0,0,16,
        80,1,0,0,0,18,91,1,0,0,0,20,95,1,0,0,0,22,24,5,9,0,0,23,22,1,0,0,
        0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,31,1,0,0,0,27,25,
        1,0,0,0,28,30,3,4,2,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,
        31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,0,0,1,35,1,1,0,
        0,0,36,37,5,18,0,0,37,3,1,0,0,0,38,39,3,6,3,0,39,5,1,0,0,0,40,41,
        5,16,0,0,41,43,3,8,4,0,42,40,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,
        44,48,5,17,0,0,45,49,3,14,7,0,46,49,3,18,9,0,47,49,3,16,8,0,48,45,
        1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,51,1,0,0,0,50,52,5,9,0,0,
        51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,7,1,0,
        0,0,55,71,5,1,0,0,56,58,7,0,0,0,57,56,1,0,0,0,57,58,1,0,0,0,58,59,
        1,0,0,0,59,64,3,10,5,0,60,61,5,3,0,0,61,63,3,10,5,0,62,60,1,0,0,
        0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,68,1,0,0,0,66,64,
        1,0,0,0,67,69,5,3,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,
        70,55,1,0,0,0,70,57,1,0,0,0,71,9,1,0,0,0,72,75,3,2,1,0,73,75,3,12,
        6,0,74,72,1,0,0,0,74,73,1,0,0,0,75,11,1,0,0,0,76,77,5,4,0,0,77,13,
        1,0,0,0,78,79,5,5,0,0,79,15,1,0,0,0,80,85,3,20,10,0,81,82,5,6,0,
        0,82,84,3,20,10,0,83,81,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,
        1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,88,90,5,6,0,0,89,88,1,0,0,0,
        89,90,1,0,0,0,90,17,1,0,0,0,91,92,5,12,0,0,92,93,3,16,8,0,93,94,
        5,13,0,0,94,19,1,0,0,0,95,98,3,2,1,0,96,97,5,7,0,0,97,99,3,2,1,0,
        98,96,1,0,0,0,98,99,1,0,0,0,99,21,1,0,0,0,13,25,31,42,48,53,57,64,
        68,70,74,85,89,98
    ]

class TheLanguageGrammarParser ( Parser ):

    grammarFileName = "TheLanguageGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'./'", "'/'", "'..'", "'*'", "','", 
                     "'as'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'from'", "'import'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "HORIZONTAL_WHITESPACE", "NEWLINE", "NESTED_NEWLINE", 
                      "LINE_CONTINUATION", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "INCLUDE_FROM", "INCLUDE_IMPORT", "IDENTIFIER", 
                      "INDENT", "DEDENT" ]

    RULE_entry_point__ = 0
    RULE_identifier = 1
    RULE_expression__ = 2
    RULE_include_expression = 3
    RULE_include_expression_source = 4
    RULE_include_expression_source__ = 5
    RULE_include_expression_source_parent_dir = 6
    RULE_include_expression_star = 7
    RULE_include_expression_items__ = 8
    RULE_include_expression_grouped_items__ = 9
    RULE_include_expression_element = 10

    ruleNames =  [ "entry_point__", "identifier", "expression__", "include_expression", 
                   "include_expression_source", "include_expression_source__", 
                   "include_expression_source_parent_dir", "include_expression_star", 
                   "include_expression_items__", "include_expression_grouped_items__", 
                   "include_expression_element" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    HORIZONTAL_WHITESPACE=8
    NEWLINE=9
    NESTED_NEWLINE=10
    LINE_CONTINUATION=11
    LPAREN=12
    RPAREN=13
    LBRACK=14
    RBRACK=15
    INCLUDE_FROM=16
    INCLUDE_IMPORT=17
    IDENTIFIER=18
    INDENT=19
    DEDENT=20

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 22
                self.match(TheLanguageGrammarParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 28
                self.expression__()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
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
            self.state = 36
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
            self.state = 38
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

        def INCLUDE_IMPORT(self):
            return self.getToken(TheLanguageGrammarParser.INCLUDE_IMPORT, 0)

        def include_expression_star(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expression_starContext,0)


        def include_expression_grouped_items__(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expression_grouped_items__Context,0)


        def include_expression_items__(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expression_items__Context,0)


        def INCLUDE_FROM(self):
            return self.getToken(TheLanguageGrammarParser.INCLUDE_FROM, 0)

        def include_expression_source(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expression_sourceContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TheLanguageGrammarParser.NEWLINE)
            else:
                return self.getToken(TheLanguageGrammarParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 40
                self.match(TheLanguageGrammarParser.INCLUDE_FROM)
                self.state = 41
                self.include_expression_source()


            self.state = 44
            self.match(TheLanguageGrammarParser.INCLUDE_IMPORT)
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.state = 45
                self.include_expression_star()
                pass
            elif token in [12]:
                self.state = 46
                self.include_expression_grouped_items__()
                pass
            elif token in [18]:
                self.state = 47
                self.include_expression_items__()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.match(TheLanguageGrammarParser.NEWLINE)
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_expression_sourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include_expression_source__(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TheLanguageGrammarParser.Include_expression_source__Context)
            else:
                return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expression_source__Context,i)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_include_expression_source

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_expression_source" ):
                return visitor.visitInclude_expression_source(self)
            else:
                return visitor.visitChildren(self)




    def include_expression_source(self):

        localctx = TheLanguageGrammarParser.Include_expression_sourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_include_expression_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 55
                self.match(TheLanguageGrammarParser.T__0)
                pass
            elif token in [2, 3, 4, 18]:
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==3:
                    self.state = 56
                    _la = self._input.LA(1)
                    if not(_la==2 or _la==3):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 59
                self.include_expression_source__()
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 60
                        self.match(TheLanguageGrammarParser.T__2)
                        self.state = 61
                        self.include_expression_source__() 
                    self.state = 66
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 67
                    self.match(TheLanguageGrammarParser.T__2)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_expression_source__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.IdentifierContext,0)


        def include_expression_source_parent_dir(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expression_source_parent_dirContext,0)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_include_expression_source__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_expression_source__" ):
                return visitor.visitInclude_expression_source__(self)
            else:
                return visitor.visitChildren(self)




    def include_expression_source__(self):

        localctx = TheLanguageGrammarParser.Include_expression_source__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_include_expression_source__)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.identifier()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.include_expression_source_parent_dir()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_expression_source_parent_dirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_include_expression_source_parent_dir

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_expression_source_parent_dir" ):
                return visitor.visitInclude_expression_source_parent_dir(self)
            else:
                return visitor.visitChildren(self)




    def include_expression_source_parent_dir(self):

        localctx = TheLanguageGrammarParser.Include_expression_source_parent_dirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_include_expression_source_parent_dir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(TheLanguageGrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_expression_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_include_expression_star

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_expression_star" ):
                return visitor.visitInclude_expression_star(self)
            else:
                return visitor.visitChildren(self)




    def include_expression_star(self):

        localctx = TheLanguageGrammarParser.Include_expression_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_include_expression_star)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(TheLanguageGrammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_expression_items__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def include_expression_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TheLanguageGrammarParser.Include_expression_elementContext)
            else:
                return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expression_elementContext,i)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_include_expression_items__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_expression_items__" ):
                return visitor.visitInclude_expression_items__(self)
            else:
                return visitor.visitChildren(self)




    def include_expression_items__(self):

        localctx = TheLanguageGrammarParser.Include_expression_items__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_include_expression_items__)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.include_expression_element()
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.match(TheLanguageGrammarParser.T__5)
                    self.state = 82
                    self.include_expression_element() 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 88
                self.match(TheLanguageGrammarParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_expression_grouped_items__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(TheLanguageGrammarParser.LPAREN, 0)

        def include_expression_items__(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Include_expression_items__Context,0)


        def RPAREN(self):
            return self.getToken(TheLanguageGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_include_expression_grouped_items__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_expression_grouped_items__" ):
                return visitor.visitInclude_expression_grouped_items__(self)
            else:
                return visitor.visitChildren(self)




    def include_expression_grouped_items__(self):

        localctx = TheLanguageGrammarParser.Include_expression_grouped_items__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_include_expression_grouped_items__)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(TheLanguageGrammarParser.LPAREN)
            self.state = 92
            self.include_expression_items__()
            self.state = 93
            self.match(TheLanguageGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Include_expression_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TheLanguageGrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(TheLanguageGrammarParser.IdentifierContext,i)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_include_expression_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInclude_expression_element" ):
                return visitor.visitInclude_expression_element(self)
            else:
                return visitor.visitChildren(self)




    def include_expression_element(self):

        localctx = TheLanguageGrammarParser.Include_expression_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_include_expression_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.identifier()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 96
                self.match(TheLanguageGrammarParser.T__6)
                self.state = 97
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






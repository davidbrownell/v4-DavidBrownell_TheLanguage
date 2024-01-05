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
        4,1,19,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,
        1,1,1,1,1,2,1,2,1,3,1,3,3,3,47,8,3,1,3,1,3,1,3,4,3,52,8,3,11,3,12,
        3,53,1,4,3,4,57,8,4,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,4,
        3,4,68,8,4,1,5,1,5,1,6,1,6,1,6,3,6,75,8,6,1,7,1,7,1,8,1,8,1,8,3,
        8,82,8,8,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,93,8,11,
        10,11,12,11,96,9,11,1,11,3,11,99,8,11,1,12,1,12,1,12,3,12,104,8,
        12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,106,0,29,1,
        0,0,0,2,40,1,0,0,0,4,42,1,0,0,0,6,46,1,0,0,0,8,56,1,0,0,0,10,69,
        1,0,0,0,12,74,1,0,0,0,14,76,1,0,0,0,16,81,1,0,0,0,18,83,1,0,0,0,
        20,85,1,0,0,0,22,89,1,0,0,0,24,100,1,0,0,0,26,28,5,8,0,0,27,26,1,
        0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,35,1,0,0,0,31,
        29,1,0,0,0,32,34,3,4,2,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,
        0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,
        0,0,0,40,41,5,17,0,0,41,3,1,0,0,0,42,43,3,6,3,0,43,5,1,0,0,0,44,
        45,5,15,0,0,45,47,3,8,4,0,46,44,1,0,0,0,46,47,1,0,0,0,47,48,1,0,
        0,0,48,49,5,16,0,0,49,51,3,16,8,0,50,52,5,8,0,0,51,50,1,0,0,0,52,
        53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,7,1,0,0,0,55,57,3,10,5,
        0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,63,3,12,6,0,59,60,
        5,1,0,0,60,62,3,12,6,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,
        63,64,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,66,68,3,14,7,0,67,66,1,
        0,0,0,67,68,1,0,0,0,68,9,1,0,0,0,69,70,5,1,0,0,70,11,1,0,0,0,71,
        75,5,2,0,0,72,75,5,3,0,0,73,75,3,2,1,0,74,71,1,0,0,0,74,72,1,0,0,
        0,74,73,1,0,0,0,75,13,1,0,0,0,76,77,5,1,0,0,77,15,1,0,0,0,78,82,
        3,18,9,0,79,82,3,20,10,0,80,82,3,22,11,0,81,78,1,0,0,0,81,79,1,0,
        0,0,81,80,1,0,0,0,82,17,1,0,0,0,83,84,5,4,0,0,84,19,1,0,0,0,85,86,
        5,11,0,0,86,87,3,22,11,0,87,88,5,12,0,0,88,21,1,0,0,0,89,94,3,24,
        12,0,90,91,5,5,0,0,91,93,3,24,12,0,92,90,1,0,0,0,93,96,1,0,0,0,94,
        92,1,0,0,0,94,95,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,97,99,5,5,0,
        0,98,97,1,0,0,0,98,99,1,0,0,0,99,23,1,0,0,0,100,103,3,2,1,0,101,
        102,5,6,0,0,102,104,3,2,1,0,103,101,1,0,0,0,103,104,1,0,0,0,104,
        25,1,0,0,0,12,29,35,46,53,56,63,67,74,81,94,98,103
    ]

class TheLanguageGrammarParser ( Parser ):

    grammarFileName = "TheLanguageGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "'.'", "'..'", "'*'", "','", "'as'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'from'", "'import'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "HORIZONTAL_WHITESPACE", 
                      "NEWLINE", "NESTED_NEWLINE", "LINE_CONTINUATION", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "INCLUDE_FROM", 
                      "INCLUDE_IMPORT", "IDENTIFIER", "INDENT", "DEDENT" ]

    RULE_entry_point__ = 0
    RULE_identifier = 1
    RULE_expression__ = 2
    RULE_import_expression = 3
    RULE_import_expression_from__ = 4
    RULE_import_expression_from_workspace_slash = 5
    RULE_import_expression_from_component = 6
    RULE_import_expression_from_directory_slash = 7
    RULE_import_expression_import__ = 8
    RULE_import_expression_import_star = 9
    RULE_import_expression_import_grouped_items__ = 10
    RULE_import_expression_import_items__ = 11
    RULE_import_expression_import_element = 12

    ruleNames =  [ "entry_point__", "identifier", "expression__", "import_expression", 
                   "import_expression_from__", "import_expression_from_workspace_slash", 
                   "import_expression_from_component", "import_expression_from_directory_slash", 
                   "import_expression_import__", "import_expression_import_star", 
                   "import_expression_import_grouped_items__", "import_expression_import_items__", 
                   "import_expression_import_element" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    HORIZONTAL_WHITESPACE=7
    NEWLINE=8
    NESTED_NEWLINE=9
    LINE_CONTINUATION=10
    LPAREN=11
    RPAREN=12
    LBRACK=13
    RBRACK=14
    INCLUDE_FROM=15
    INCLUDE_IMPORT=16
    IDENTIFIER=17
    INDENT=18
    DEDENT=19

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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 26
                self.match(TheLanguageGrammarParser.NEWLINE)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 32
                self.expression__()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
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
            self.state = 40
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

        def import_expression(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expressionContext,0)


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
            self.state = 42
            self.import_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE_IMPORT(self):
            return self.getToken(TheLanguageGrammarParser.INCLUDE_IMPORT, 0)

        def import_expression_import__(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_import__Context,0)


        def INCLUDE_FROM(self):
            return self.getToken(TheLanguageGrammarParser.INCLUDE_FROM, 0)

        def import_expression_from__(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_from__Context,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TheLanguageGrammarParser.NEWLINE)
            else:
                return self.getToken(TheLanguageGrammarParser.NEWLINE, i)

        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression" ):
                return visitor.visitImport_expression(self)
            else:
                return visitor.visitChildren(self)




    def import_expression(self):

        localctx = TheLanguageGrammarParser.Import_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_import_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 44
                self.match(TheLanguageGrammarParser.INCLUDE_FROM)
                self.state = 45
                self.import_expression_from__()


            self.state = 48
            self.match(TheLanguageGrammarParser.INCLUDE_IMPORT)
            self.state = 49
            self.import_expression_import__()
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.match(TheLanguageGrammarParser.NEWLINE)
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_expression_from__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_expression_from_component(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TheLanguageGrammarParser.Import_expression_from_componentContext)
            else:
                return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_from_componentContext,i)


        def import_expression_from_workspace_slash(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_from_workspace_slashContext,0)


        def import_expression_from_directory_slash(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_from_directory_slashContext,0)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression_from__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_from__" ):
                return visitor.visitImport_expression_from__(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_from__(self):

        localctx = TheLanguageGrammarParser.Import_expression_from__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_import_expression_from__)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 55
                self.import_expression_from_workspace_slash()


            self.state = 58
            self.import_expression_from_component()
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    self.match(TheLanguageGrammarParser.T__0)
                    self.state = 60
                    self.import_expression_from_component() 
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 66
                self.import_expression_from_directory_slash()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_expression_from_workspace_slashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression_from_workspace_slash

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_from_workspace_slash" ):
                return visitor.visitImport_expression_from_workspace_slash(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_from_workspace_slash(self):

        localctx = TheLanguageGrammarParser.Import_expression_from_workspace_slashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_import_expression_from_workspace_slash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(TheLanguageGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_expression_from_componentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.IdentifierContext,0)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression_from_component

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_from_component" ):
                return visitor.visitImport_expression_from_component(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_from_component(self):

        localctx = TheLanguageGrammarParser.Import_expression_from_componentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_import_expression_from_component)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(TheLanguageGrammarParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(TheLanguageGrammarParser.T__2)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.identifier()
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


    class Import_expression_from_directory_slashContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression_from_directory_slash

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_from_directory_slash" ):
                return visitor.visitImport_expression_from_directory_slash(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_from_directory_slash(self):

        localctx = TheLanguageGrammarParser.Import_expression_from_directory_slashContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_import_expression_from_directory_slash)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(TheLanguageGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_expression_import__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_expression_import_star(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_import_starContext,0)


        def import_expression_import_grouped_items__(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_import_grouped_items__Context,0)


        def import_expression_import_items__(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_import_items__Context,0)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression_import__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_import__" ):
                return visitor.visitImport_expression_import__(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_import__(self):

        localctx = TheLanguageGrammarParser.Import_expression_import__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_import_expression_import__)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.import_expression_import_star()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.import_expression_import_grouped_items__()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.import_expression_import_items__()
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


    class Import_expression_import_starContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression_import_star

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_import_star" ):
                return visitor.visitImport_expression_import_star(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_import_star(self):

        localctx = TheLanguageGrammarParser.Import_expression_import_starContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_import_expression_import_star)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(TheLanguageGrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_expression_import_grouped_items__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(TheLanguageGrammarParser.LPAREN, 0)

        def import_expression_import_items__(self):
            return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_import_items__Context,0)


        def RPAREN(self):
            return self.getToken(TheLanguageGrammarParser.RPAREN, 0)

        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression_import_grouped_items__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_import_grouped_items__" ):
                return visitor.visitImport_expression_import_grouped_items__(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_import_grouped_items__(self):

        localctx = TheLanguageGrammarParser.Import_expression_import_grouped_items__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_import_expression_import_grouped_items__)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(TheLanguageGrammarParser.LPAREN)
            self.state = 86
            self.import_expression_import_items__()
            self.state = 87
            self.match(TheLanguageGrammarParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_expression_import_items__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_expression_import_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TheLanguageGrammarParser.Import_expression_import_elementContext)
            else:
                return self.getTypedRuleContext(TheLanguageGrammarParser.Import_expression_import_elementContext,i)


        def getRuleIndex(self):
            return TheLanguageGrammarParser.RULE_import_expression_import_items__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_import_items__" ):
                return visitor.visitImport_expression_import_items__(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_import_items__(self):

        localctx = TheLanguageGrammarParser.Import_expression_import_items__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_import_expression_import_items__)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.import_expression_import_element()
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 90
                    self.match(TheLanguageGrammarParser.T__4)
                    self.state = 91
                    self.import_expression_import_element() 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 97
                self.match(TheLanguageGrammarParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_expression_import_elementContext(ParserRuleContext):
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
            return TheLanguageGrammarParser.RULE_import_expression_import_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_expression_import_element" ):
                return visitor.visitImport_expression_import_element(self)
            else:
                return visitor.visitChildren(self)




    def import_expression_import_element(self):

        localctx = TheLanguageGrammarParser.Import_expression_import_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_import_expression_import_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.identifier()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 101
                self.match(TheLanguageGrammarParser.T__5)
                self.state = 102
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






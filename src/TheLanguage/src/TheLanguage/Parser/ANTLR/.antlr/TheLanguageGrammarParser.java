// Generated from c:\Code\GitHub\davidbrownell\DavidBrownell\TheLanguage\src\TheLanguage\src\TheLanguage\Parser\ANTLR\TheLanguageGrammar.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TheLanguageGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, HORIZONTAL_WHITESPACE=8, 
		NEWLINE=9, NESTED_NEWLINE=10, LINE_CONTINUATION=11, LPAREN=12, RPAREN=13, 
		LBRACK=14, RBRACK=15, INCLUDE_FROM=16, INCLUDE_IMPORT=17, IDENTIFIER=18, 
		INDENT=19, DEDENT=20;
	public static final int
		RULE_entry_point__ = 0, RULE_identifier = 1, RULE_expression__ = 2, RULE_include_expression = 3, 
		RULE_include_expression_source = 4, RULE_include_expression_source__ = 5, 
		RULE_include_expression_source_parent_dir = 6, RULE_include_expression_star = 7, 
		RULE_include_expression_items__ = 8, RULE_include_expression_grouped_items__ = 9, 
		RULE_include_expression_element = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"entry_point__", "identifier", "expression__", "include_expression", 
			"include_expression_source", "include_expression_source__", "include_expression_source_parent_dir", 
			"include_expression_star", "include_expression_items__", "include_expression_grouped_items__", 
			"include_expression_element"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "'./'", "'/'", "'..'", "'*'", "','", "'as'", null, null, 
			null, null, "'('", "')'", "'['", "']'", "'from'", "'import'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "HORIZONTAL_WHITESPACE", 
			"NEWLINE", "NESTED_NEWLINE", "LINE_CONTINUATION", "LPAREN", "RPAREN", 
			"LBRACK", "RBRACK", "INCLUDE_FROM", "INCLUDE_IMPORT", "IDENTIFIER", "INDENT", 
			"DEDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "TheLanguageGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TheLanguageGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class Entry_point__Context extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(TheLanguageGrammarParser.EOF, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(TheLanguageGrammarParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(TheLanguageGrammarParser.NEWLINE, i);
		}
		public List<Expression__Context> expression__() {
			return getRuleContexts(Expression__Context.class);
		}
		public Expression__Context expression__(int i) {
			return getRuleContext(Expression__Context.class,i);
		}
		public Entry_point__Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entry_point__; }
	}

	public final Entry_point__Context entry_point__() throws RecognitionException {
		Entry_point__Context _localctx = new Entry_point__Context(_ctx, getState());
		enterRule(_localctx, 0, RULE_entry_point__);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(22);
				match(NEWLINE);
				}
				}
				setState(27);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==INCLUDE_FROM || _la==INCLUDE_IMPORT) {
				{
				{
				setState(28);
				expression__();
				}
				}
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(34);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(TheLanguageGrammarParser.IDENTIFIER, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expression__Context extends ParserRuleContext {
		public Include_expressionContext include_expression() {
			return getRuleContext(Include_expressionContext.class,0);
		}
		public Expression__Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression__; }
	}

	public final Expression__Context expression__() throws RecognitionException {
		Expression__Context _localctx = new Expression__Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_expression__);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(38);
			include_expression();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_expressionContext extends ParserRuleContext {
		public TerminalNode INCLUDE_IMPORT() { return getToken(TheLanguageGrammarParser.INCLUDE_IMPORT, 0); }
		public Include_expression_starContext include_expression_star() {
			return getRuleContext(Include_expression_starContext.class,0);
		}
		public Include_expression_grouped_items__Context include_expression_grouped_items__() {
			return getRuleContext(Include_expression_grouped_items__Context.class,0);
		}
		public Include_expression_items__Context include_expression_items__() {
			return getRuleContext(Include_expression_items__Context.class,0);
		}
		public TerminalNode INCLUDE_FROM() { return getToken(TheLanguageGrammarParser.INCLUDE_FROM, 0); }
		public Include_expression_sourceContext include_expression_source() {
			return getRuleContext(Include_expression_sourceContext.class,0);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(TheLanguageGrammarParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(TheLanguageGrammarParser.NEWLINE, i);
		}
		public Include_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_expression; }
	}

	public final Include_expressionContext include_expression() throws RecognitionException {
		Include_expressionContext _localctx = new Include_expressionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_include_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INCLUDE_FROM) {
				{
				setState(40);
				match(INCLUDE_FROM);
				setState(41);
				include_expression_source();
				}
			}

			setState(44);
			match(INCLUDE_IMPORT);
			setState(48);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				{
				setState(45);
				include_expression_star();
				}
				break;
			case LPAREN:
				{
				setState(46);
				include_expression_grouped_items__();
				}
				break;
			case IDENTIFIER:
				{
				setState(47);
				include_expression_items__();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(51); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(50);
				match(NEWLINE);
				}
				}
				setState(53); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==NEWLINE );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_expression_sourceContext extends ParserRuleContext {
		public List<Include_expression_source__Context> include_expression_source__() {
			return getRuleContexts(Include_expression_source__Context.class);
		}
		public Include_expression_source__Context include_expression_source__(int i) {
			return getRuleContext(Include_expression_source__Context.class,i);
		}
		public Include_expression_sourceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_expression_source; }
	}

	public final Include_expression_sourceContext include_expression_source() throws RecognitionException {
		Include_expression_sourceContext _localctx = new Include_expression_sourceContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_include_expression_source);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				{
				setState(55);
				match(T__0);
				}
				break;
			case T__1:
			case T__2:
			case T__3:
			case IDENTIFIER:
				{
				{
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1 || _la==T__2) {
					{
					setState(56);
					_la = _input.LA(1);
					if ( !(_la==T__1 || _la==T__2) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(59);
				include_expression_source__();
				setState(64);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(60);
						match(T__2);
						setState(61);
						include_expression_source__();
						}
						} 
					}
					setState(66);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
				}
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__2) {
					{
					setState(67);
					match(T__2);
					}
				}

				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_expression_source__Context extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public Include_expression_source_parent_dirContext include_expression_source_parent_dir() {
			return getRuleContext(Include_expression_source_parent_dirContext.class,0);
		}
		public Include_expression_source__Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_expression_source__; }
	}

	public final Include_expression_source__Context include_expression_source__() throws RecognitionException {
		Include_expression_source__Context _localctx = new Include_expression_source__Context(_ctx, getState());
		enterRule(_localctx, 10, RULE_include_expression_source__);
		try {
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				identifier();
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 2);
				{
				setState(73);
				include_expression_source_parent_dir();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_expression_source_parent_dirContext extends ParserRuleContext {
		public Include_expression_source_parent_dirContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_expression_source_parent_dir; }
	}

	public final Include_expression_source_parent_dirContext include_expression_source_parent_dir() throws RecognitionException {
		Include_expression_source_parent_dirContext _localctx = new Include_expression_source_parent_dirContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_include_expression_source_parent_dir);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_expression_starContext extends ParserRuleContext {
		public Include_expression_starContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_expression_star; }
	}

	public final Include_expression_starContext include_expression_star() throws RecognitionException {
		Include_expression_starContext _localctx = new Include_expression_starContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_include_expression_star);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_expression_items__Context extends ParserRuleContext {
		public List<Include_expression_elementContext> include_expression_element() {
			return getRuleContexts(Include_expression_elementContext.class);
		}
		public Include_expression_elementContext include_expression_element(int i) {
			return getRuleContext(Include_expression_elementContext.class,i);
		}
		public Include_expression_items__Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_expression_items__; }
	}

	public final Include_expression_items__Context include_expression_items__() throws RecognitionException {
		Include_expression_items__Context _localctx = new Include_expression_items__Context(_ctx, getState());
		enterRule(_localctx, 16, RULE_include_expression_items__);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			include_expression_element();
			setState(85);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(81);
					match(T__5);
					setState(82);
					include_expression_element();
					}
					} 
				}
				setState(87);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(88);
				match(T__5);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_expression_grouped_items__Context extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(TheLanguageGrammarParser.LPAREN, 0); }
		public Include_expression_items__Context include_expression_items__() {
			return getRuleContext(Include_expression_items__Context.class,0);
		}
		public TerminalNode RPAREN() { return getToken(TheLanguageGrammarParser.RPAREN, 0); }
		public Include_expression_grouped_items__Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_expression_grouped_items__; }
	}

	public final Include_expression_grouped_items__Context include_expression_grouped_items__() throws RecognitionException {
		Include_expression_grouped_items__Context _localctx = new Include_expression_grouped_items__Context(_ctx, getState());
		enterRule(_localctx, 18, RULE_include_expression_grouped_items__);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(LPAREN);
			setState(92);
			include_expression_items__();
			setState(93);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Include_expression_elementContext extends ParserRuleContext {
		public List<IdentifierContext> identifier() {
			return getRuleContexts(IdentifierContext.class);
		}
		public IdentifierContext identifier(int i) {
			return getRuleContext(IdentifierContext.class,i);
		}
		public Include_expression_elementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_include_expression_element; }
	}

	public final Include_expression_elementContext include_expression_element() throws RecognitionException {
		Include_expression_elementContext _localctx = new Include_expression_elementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_include_expression_element);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			identifier();
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__6) {
				{
				setState(96);
				match(T__6);
				setState(97);
				identifier();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26g\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\3\2\7\2\32\n\2\f\2\16\2\35\13\2\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2"+
		"\3\2\3\3\3\3\3\4\3\4\3\5\3\5\5\5-\n\5\3\5\3\5\3\5\3\5\5\5\63\n\5\3\5\6"+
		"\5\66\n\5\r\5\16\5\67\3\6\3\6\5\6<\n\6\3\6\3\6\3\6\7\6A\n\6\f\6\16\6D"+
		"\13\6\3\6\5\6G\n\6\5\6I\n\6\3\7\3\7\5\7M\n\7\3\b\3\b\3\t\3\t\3\n\3\n\3"+
		"\n\7\nV\n\n\f\n\16\nY\13\n\3\n\5\n\\\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3"+
		"\f\5\fe\n\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\3\3\2\4\5\2i\2\33\3"+
		"\2\2\2\4&\3\2\2\2\6(\3\2\2\2\b,\3\2\2\2\nH\3\2\2\2\fL\3\2\2\2\16N\3\2"+
		"\2\2\20P\3\2\2\2\22R\3\2\2\2\24]\3\2\2\2\26a\3\2\2\2\30\32\7\13\2\2\31"+
		"\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34!\3\2\2\2\35\33"+
		"\3\2\2\2\36 \5\6\4\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\""+
		"$\3\2\2\2#!\3\2\2\2$%\7\2\2\3%\3\3\2\2\2&\'\7\24\2\2\'\5\3\2\2\2()\5\b"+
		"\5\2)\7\3\2\2\2*+\7\22\2\2+-\5\n\6\2,*\3\2\2\2,-\3\2\2\2-.\3\2\2\2.\62"+
		"\7\23\2\2/\63\5\20\t\2\60\63\5\24\13\2\61\63\5\22\n\2\62/\3\2\2\2\62\60"+
		"\3\2\2\2\62\61\3\2\2\2\63\65\3\2\2\2\64\66\7\13\2\2\65\64\3\2\2\2\66\67"+
		"\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\t\3\2\2\29I\7\3\2\2:<\t\2\2\2;:\3"+
		"\2\2\2;<\3\2\2\2<=\3\2\2\2=B\5\f\7\2>?\7\5\2\2?A\5\f\7\2@>\3\2\2\2AD\3"+
		"\2\2\2B@\3\2\2\2BC\3\2\2\2CF\3\2\2\2DB\3\2\2\2EG\7\5\2\2FE\3\2\2\2FG\3"+
		"\2\2\2GI\3\2\2\2H9\3\2\2\2H;\3\2\2\2I\13\3\2\2\2JM\5\4\3\2KM\5\16\b\2"+
		"LJ\3\2\2\2LK\3\2\2\2M\r\3\2\2\2NO\7\6\2\2O\17\3\2\2\2PQ\7\7\2\2Q\21\3"+
		"\2\2\2RW\5\26\f\2ST\7\b\2\2TV\5\26\f\2US\3\2\2\2VY\3\2\2\2WU\3\2\2\2W"+
		"X\3\2\2\2X[\3\2\2\2YW\3\2\2\2Z\\\7\b\2\2[Z\3\2\2\2[\\\3\2\2\2\\\23\3\2"+
		"\2\2]^\7\16\2\2^_\5\22\n\2_`\7\17\2\2`\25\3\2\2\2ad\5\4\3\2bc\7\t\2\2"+
		"ce\5\4\3\2db\3\2\2\2de\3\2\2\2e\27\3\2\2\2\17\33!,\62\67;BFHLW[d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
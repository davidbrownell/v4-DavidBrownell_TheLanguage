// Generated from c:\Code\GitHub\davidbrownell\DavidBrownell\TheLanguage\src\TheLanguage\src\TheLanguage\Parser\ANTLR\TheLanguageGrammar.g4 by ANTLR 4.9.2


from antlr_denter.DenterHelper import DenterHelper
from TheLanguageGrammarParser import TheLanguageGrammarParser


import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TheLanguageGrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, HORIZONTAL_WHITESPACE=8, 
		NEWLINE=9, NESTED_NEWLINE=10, LINE_CONTINUATION=11, LPAREN=12, RPAREN=13, 
		LBRACK=14, RBRACK=15, INCLUDE_FROM=16, INCLUDE_IMPORT=17, IDENTIFIER=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "HORIZONTAL_WHITESPACE", 
			"NEWLINE", "NESTED_NEWLINE", "LINE_CONTINUATION", "LPAREN", "RPAREN", 
			"LBRACK", "RBRACK", "INCLUDE_FROM", "INCLUDE_IMPORT", "IDENTIFIER"
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
			"LBRACK", "RBRACK", "INCLUDE_FROM", "INCLUDE_IMPORT", "IDENTIFIER"
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



	def CustomInit(self):
	    self._nested_pair_ctr = 0


	class TheLanguageGrammarDenter(DenterHelper):
	    def __init__(self, lexer, newline_token, indent_token, dedent_token):
	        super().__init__(newline_token, indent_token, dedent_token, should_ignore_eof=False)

	        self.lexer: TheLanguageGrammarLexer = lexer

	    def pull_token(self):
	        return super(TheLanguageGrammarLexer, self.lexer).nextToken()

	def nextToken(self):
	    if not hasattr(self, "_denter"):
	        self._denter = self.__class__.TheLanguageGrammarDenter(
	            self,
	            TheLanguageGrammarParser.NEWLINE,
	            TheLanguageGrammarParser.INDENT,
	            TheLanguageGrammarParser.DEDENT,
	        )

	    return self._denter.next_token()


	public TheLanguageGrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "TheLanguageGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 11:
			LPAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 12:
			RPAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 13:
			LBRACK_action((RuleContext)_localctx, actionIndex);
			break;
		case 14:
			RBRACK_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void LPAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			self._nested_pair_ctr += 1
			break;
		}
	}
	private void RPAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			self._nested_pair_ctr -= 1
			break;
		}
	}
	private void LBRACK_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			self._nested_pair_ctr += 1
			break;
		}
	}
	private void RBRACK_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			self._nested_pair_ctr -= 1
			break;
		}
	}
	@Override
	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 8:
			return NEWLINE_sempred((RuleContext)_localctx, predIndex);
		case 9:
			return NESTED_NEWLINE_sempred((RuleContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean NEWLINE_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return self._nested_pair_ctr == 0;
		}
		return true;
	}
	private boolean NESTED_NEWLINE_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return self._nested_pair_ctr != 0;
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24\u0095\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3"+
		"\7\3\b\3\b\3\b\3\t\6\t:\n\t\r\t\16\t;\3\t\3\t\3\n\5\nA\n\n\3\n\3\n\3\n"+
		"\7\nF\n\n\f\n\16\nI\13\n\3\13\5\13L\n\13\3\13\3\13\3\13\7\13Q\n\13\f\13"+
		"\16\13T\13\13\3\13\3\13\3\f\3\f\5\fZ\n\f\3\f\3\f\7\f^\n\f\f\f\16\fa\13"+
		"\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3"+
		"\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\7\23~"+
		"\n\23\f\23\16\23\u0081\13\23\3\23\3\23\7\23\u0085\n\23\f\23\16\23\u0088"+
		"\13\23\3\23\5\23\u008b\n\23\3\23\5\23\u008e\n\23\3\23\7\23\u0091\n\23"+
		"\f\23\16\23\u0094\13\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13"+
		"\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\3\2\3\4\2\13\13\"\"\4\u0095"+
		"\2%\2%\2,\2,\2\62\2;\2C\2\\\2c\2|\2\u00ab\2\u00ab\2\u00b0\2\u00b0\2\u203e"+
		"\2\u203e\2\u204b\2\u204b\2\u2124\2\u2124\2\u213b\2\u213b\2\u2196\2\u219b"+
		"\2\u21ab\2\u21ac\2\u231c\2\u231d\2\u232a\2\u232a\2\u23d1\2\u23d1\2\u23eb"+
		"\2\u23f5\2\u23fa\2\u23fc\2\u24c4\2\u24c4\2\u25ac\2\u25ad\2\u25b8\2\u25b8"+
		"\2\u25c2\2\u25c2\2\u25fd\2\u2600\2\u2602\2\u2606\2\u2610\2\u2610\2\u2613"+
		"\2\u2613\2\u2616\2\u2617\2\u261a\2\u261a\2\u261f\2\u261f\2\u2622\2\u2622"+
		"\2\u2624\2\u2625\2\u2628\2\u2628\2\u262c\2\u262c\2\u2630\2\u2631\2\u263a"+
		"\2\u263c\2\u2642\2\u2642\2\u2644\2\u2644\2\u264a\2\u2655\2\u2662\2\u2662"+
		"\2\u2665\2\u2665\2\u2667\2\u2668\2\u266a\2\u266a\2\u267d\2\u267d\2\u2681"+
		"\2\u2681\2\u2694\2\u2699\2\u269b\2\u269b\2\u269d\2\u269e\2\u26a2\2\u26a3"+
		"\2\u26ac\2\u26ad\2\u26b2\2\u26b3\2\u26bf\2\u26c0\2\u26c6\2\u26c7\2\u26ca"+
		"\2\u26ca\2\u26d0\2\u26d1\2\u26d3\2\u26d3\2\u26d5\2\u26d6\2\u26eb\2\u26ec"+
		"\2\u26f2\2\u26f7\2\u26f9\2\u26fc\2\u26ff\2\u26ff\2\u2704\2\u2704\2\u2707"+
		"\2\u2707\2\u270a\2\u270f\2\u2711\2\u2711\2\u2714\2\u2714\2\u2716\2\u2716"+
		"\2\u2718\2\u2718\2\u271f\2\u271f\2\u2723\2\u2723\2\u272a\2\u272a\2\u2735"+
		"\2\u2736\2\u2746\2\u2746\2\u2749\2\u2749\2\u274e\2\u274e\2\u2750\2\u2750"+
		"\2\u2755\2\u2757\2\u2759\2\u2759\2\u2765\2\u2766\2\u2797\2\u2799\2\u27a3"+
		"\2\u27a3\2\u27b2\2\u27b2\2\u27c1\2\u27c1\2\u2936\2\u2937\2\u2b07\2\u2b09"+
		"\2\u2b1d\2\u2b1e\2\u2b52\2\u2b52\2\u2b57\2\u2b57\2\u3032\2\u3032\2\u303f"+
		"\2\u303f\2\u3299\2\u3299\2\u329b\2\u329b\2\uf006\3\uf006\3\uf0d1\3\uf0d1"+
		"\3\uf172\3\uf173\3\uf180\3\uf181\3\uf190\3\uf190\3\uf193\3\uf19c\3\uf1e8"+
		"\3\uf201\3\uf203\3\uf204\3\uf21c\3\uf21c\3\uf231\3\uf231\3\uf234\3\uf23c"+
		"\3\uf252\3\uf253\3\uf302\3\uf323\3\uf326\3\uf395\3\uf398\3\uf399\3\uf39b"+
		"\3\uf39d\3\uf3a0\3\uf3f2\3\uf3f5\3\uf3f7\3\uf3f9\3\uf4ff\3\uf501\3\uf53f"+
		"\3\uf54b\3\uf550\3\uf552\3\uf569\3\uf571\3\uf572\3\uf575\3\uf57c\3\uf589"+
		"\3\uf589\3\uf58c\3\uf58f\3\uf592\3\uf592\3\uf597\3\uf598\3\uf5a6\3\uf5a7"+
		"\3\uf5aa\3\uf5aa\3\uf5b3\3\uf5b4\3\uf5be\3\uf5be\3\uf5c4\3\uf5c6\3\uf5d3"+
		"\3\uf5d5\3\uf5de\3\uf5e0\3\uf5e3\3\uf5e3\3\uf5e5\3\uf5e5\3\uf5ea\3\uf5ea"+
		"\3\uf5f1\3\uf5f1\3\uf5f5\3\uf5f5\3\uf5fc\3\uf651\3\uf682\3\uf6c7\3\uf6cd"+
		"\3\uf6d4\3\uf6e2\3\uf6e7\3\uf6eb\3\uf6eb\3\uf6ed\3\uf6ee\3\uf6f2\3\uf6f2"+
		"\3\uf6f5\3\uf6fa\3\uf912\3\uf93c\3\uf93e\3\uf940\3\uf942\3\uf947\3\uf949"+
		"\3\uf94e\3\uf952\3\uf96d\3\uf982\3\uf999\3\uf9c2\3\uf9c2\3\uf9d2\3\uf9e8"+
		"\3\u0096\2%\2%\2,\2,\2\62\2;\2C\2\\\2a\2a\2c\2|\2\u00ab\2\u00ab\2\u00b0"+
		"\2\u00b0\2\u203e\2\u203e\2\u204b\2\u204b\2\u2124\2\u2124\2\u213b\2\u213b"+
		"\2\u2196\2\u219b\2\u21ab\2\u21ac\2\u231c\2\u231d\2\u232a\2\u232a\2\u23d1"+
		"\2\u23d1\2\u23eb\2\u23f5\2\u23fa\2\u23fc\2\u24c4\2\u24c4\2\u25ac\2\u25ad"+
		"\2\u25b8\2\u25b8\2\u25c2\2\u25c2\2\u25fd\2\u2600\2\u2602\2\u2606\2\u2610"+
		"\2\u2610\2\u2613\2\u2613\2\u2616\2\u2617\2\u261a\2\u261a\2\u261f\2\u261f"+
		"\2\u2622\2\u2622\2\u2624\2\u2625\2\u2628\2\u2628\2\u262c\2\u262c\2\u2630"+
		"\2\u2631\2\u263a\2\u263c\2\u2642\2\u2642\2\u2644\2\u2644\2\u264a\2\u2655"+
		"\2\u2662\2\u2662\2\u2665\2\u2665\2\u2667\2\u2668\2\u266a\2\u266a\2\u267d"+
		"\2\u267d\2\u2681\2\u2681\2\u2694\2\u2699\2\u269b\2\u269b\2\u269d\2\u269e"+
		"\2\u26a2\2\u26a3\2\u26ac\2\u26ad\2\u26b2\2\u26b3\2\u26bf\2\u26c0\2\u26c6"+
		"\2\u26c7\2\u26ca\2\u26ca\2\u26d0\2\u26d1\2\u26d3\2\u26d3\2\u26d5\2\u26d6"+
		"\2\u26eb\2\u26ec\2\u26f2\2\u26f7\2\u26f9\2\u26fc\2\u26ff\2\u26ff\2\u2704"+
		"\2\u2704\2\u2707\2\u2707\2\u270a\2\u270f\2\u2711\2\u2711\2\u2714\2\u2714"+
		"\2\u2716\2\u2716\2\u2718\2\u2718\2\u271f\2\u271f\2\u2723\2\u2723\2\u272a"+
		"\2\u272a\2\u2735\2\u2736\2\u2746\2\u2746\2\u2749\2\u2749\2\u274e\2\u274e"+
		"\2\u2750\2\u2750\2\u2755\2\u2757\2\u2759\2\u2759\2\u2765\2\u2766\2\u2797"+
		"\2\u2799\2\u27a3\2\u27a3\2\u27b2\2\u27b2\2\u27c1\2\u27c1\2\u2936\2\u2937"+
		"\2\u2b07\2\u2b09\2\u2b1d\2\u2b1e\2\u2b52\2\u2b52\2\u2b57\2\u2b57\2\u3032"+
		"\2\u3032\2\u303f\2\u303f\2\u3299\2\u3299\2\u329b\2\u329b\2\uf006\3\uf006"+
		"\3\uf0d1\3\uf0d1\3\uf172\3\uf173\3\uf180\3\uf181\3\uf190\3\uf190\3\uf193"+
		"\3\uf19c\3\uf1e8\3\uf201\3\uf203\3\uf204\3\uf21c\3\uf21c\3\uf231\3\uf231"+
		"\3\uf234\3\uf23c\3\uf252\3\uf253\3\uf302\3\uf323\3\uf326\3\uf395\3\uf398"+
		"\3\uf399\3\uf39b\3\uf39d\3\uf3a0\3\uf3f2\3\uf3f5\3\uf3f7\3\uf3f9\3\uf4ff"+
		"\3\uf501\3\uf53f\3\uf54b\3\uf550\3\uf552\3\uf569\3\uf571\3\uf572\3\uf575"+
		"\3\uf57c\3\uf589\3\uf589\3\uf58c\3\uf58f\3\uf592\3\uf592\3\uf597\3\uf598"+
		"\3\uf5a6\3\uf5a7\3\uf5aa\3\uf5aa\3\uf5b3\3\uf5b4\3\uf5be\3\uf5be\3\uf5c4"+
		"\3\uf5c6\3\uf5d3\3\uf5d5\3\uf5de\3\uf5e0\3\uf5e3\3\uf5e3\3\uf5e5\3\uf5e5"+
		"\3\uf5ea\3\uf5ea\3\uf5f1\3\uf5f1\3\uf5f5\3\uf5f5\3\uf5fc\3\uf651\3\uf682"+
		"\3\uf6c7\3\uf6cd\3\uf6d4\3\uf6e2\3\uf6e7\3\uf6eb\3\uf6eb\3\uf6ed\3\uf6ee"+
		"\3\uf6f2\3\uf6f2\3\uf6f5\3\uf6fa\3\uf912\3\uf93c\3\uf93e\3\uf940\3\uf942"+
		"\3\uf947\3\uf949\3\uf94e\3\uf952\3\uf96d\3\uf982\3\uf999\3\uf9c2\3\uf9c2"+
		"\3\uf9d2\3\uf9e8\3\u00a0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2"+
		"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25"+
		"\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7,\3\2\2"+
		"\2\t.\3\2\2\2\13\61\3\2\2\2\r\63\3\2\2\2\17\65\3\2\2\2\219\3\2\2\2\23"+
		"@\3\2\2\2\25K\3\2\2\2\27W\3\2\2\2\31d\3\2\2\2\33g\3\2\2\2\35j\3\2\2\2"+
		"\37m\3\2\2\2!p\3\2\2\2#u\3\2\2\2%\177\3\2\2\2\'(\7\60\2\2(\4\3\2\2\2)"+
		"*\7\60\2\2*+\7\61\2\2+\6\3\2\2\2,-\7\61\2\2-\b\3\2\2\2./\7\60\2\2/\60"+
		"\7\60\2\2\60\n\3\2\2\2\61\62\7,\2\2\62\f\3\2\2\2\63\64\7.\2\2\64\16\3"+
		"\2\2\2\65\66\7c\2\2\66\67\7u\2\2\67\20\3\2\2\28:\t\2\2\298\3\2\2\2:;\3"+
		"\2\2\2;9\3\2\2\2;<\3\2\2\2<=\3\2\2\2=>\b\t\2\2>\22\3\2\2\2?A\7\17\2\2"+
		"@?\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\7\f\2\2CG\6\n\2\2DF\t\2\2\2ED\3\2\2\2"+
		"FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\24\3\2\2\2IG\3\2\2\2JL\7\17\2\2KJ\3\2"+
		"\2\2KL\3\2\2\2LM\3\2\2\2MN\7\f\2\2NR\6\13\3\2OQ\t\2\2\2PO\3\2\2\2QT\3"+
		"\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2UV\b\13\2\2V\26\3\2\2\2"+
		"WY\7^\2\2XZ\7\17\2\2YX\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[_\7\f\2\2\\^\t\2\2"+
		"\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2a_\3\2\2\2bc\b\f"+
		"\2\2c\30\3\2\2\2de\7*\2\2ef\b\r\3\2f\32\3\2\2\2gh\7+\2\2hi\b\16\4\2i\34"+
		"\3\2\2\2jk\7]\2\2kl\b\17\5\2l\36\3\2\2\2mn\7_\2\2no\b\20\6\2o \3\2\2\2"+
		"pq\7h\2\2qr\7t\2\2rs\7q\2\2st\7o\2\2t\"\3\2\2\2uv\7k\2\2vw\7o\2\2wx\7"+
		"r\2\2xy\7q\2\2yz\7t\2\2z{\7v\2\2{$\3\2\2\2|~\7a\2\2}|\3\2\2\2~\u0081\3"+
		"\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\177\3"+
		"\2\2\2\u0082\u0086\t\3\2\2\u0083\u0085\t\4\2\2\u0084\u0083\3\2\2\2\u0085"+
		"\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u008a\3\2"+
		"\2\2\u0088\u0086\3\2\2\2\u0089\u008b\7A\2\2\u008a\u0089\3\2\2\2\u008a"+
		"\u008b\3\2\2\2\u008b\u008d\3\2\2\2\u008c\u008e\7#\2\2\u008d\u008c\3\2"+
		"\2\2\u008d\u008e\3\2\2\2\u008e\u0092\3\2\2\2\u008f\u0091\7a\2\2\u0090"+
		"\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2"+
		"\2\2\u0093&\3\2\2\2\u0094\u0092\3\2\2\2\17\2;@GKRY_\177\u0086\u008a\u008d"+
		"\u0092\7\2\3\2\3\r\2\3\16\3\3\17\4\3\20\5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
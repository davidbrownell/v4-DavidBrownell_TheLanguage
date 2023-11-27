// ----------------------------------------------------------------------
// |
// |  TheLanguageGrammar.g4
// |
// |  David Brownell <db@DavidBrownell.com>
// |      2023-11-24 12:23:55
// |
// ----------------------------------------------------------------------
// |
// |  Copyright David Brownell 2023
// |  Distributed under the Boost Software License, Version 1.0. See
// |  accompanying file LICENSE_1_0.txt or copy at
// |  http://www.boost.org/LICENSE_1_0.txt.
// |
// ----------------------------------------------------------------------
grammar TheLanguageGrammar;

// ----------------------------------------------------------------------
tokens { INDENT, DEDENT }

@lexer::header {

from antlr_denter.DenterHelper import DenterHelper
from TheLanguageGrammarParser import TheLanguageGrammarParser

}

@lexer::members {

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
}

// ----------------------------------------------------------------------
// |
// |  Lexer Rules
// |
// ----------------------------------------------------------------------
HORIZONTAL_WHITESPACE:                      [ \t]+ -> channel(HIDDEN);

// ----------------------------------------------------------------------
// Newlines nested within paired brackets brackets are safe to ignore, but newlines outside of paired
// brackets are meaningful.
NEWLINE:                                    '\r'? '\n' {self._nested_pair_ctr == 0}? [ \t]*;
NESTED_NEWLINE:                             '\r'? '\n' {self._nested_pair_ctr != 0}? [ \t]* -> channel(HIDDEN);

LINE_CONTINUATION:                          '\\' '\r'? '\n' [ \t]* -> channel(HIDDEN);

LPAREN:                                     '(' {self._nested_pair_ctr += 1};
RPAREN:                                     ')' {self._nested_pair_ctr -= 1};
LBRACK:                                     '[' {self._nested_pair_ctr += 1};
RBRACK:                                     ']' {self._nested_pair_ctr -= 1};

// ----------------------------------------------------------------------
// The following statements are used to differentiate between tokens lexed within an include statement
// (less restrictive) and tokens lexed outside of an include statement (more restrictive).
INCLUDE_FROM:                               'from';
INCLUDE_IMPORT:                             'import';

// ----------------------------------------------------------------------
// TODO: We really want this to be any char that isn't defined elsewhere (not just emojis)
IDENTIFIER:                                 '_'* [a-zA-Z\p{Emoji}][a-zA-Z0-9_\p{Emoji}]* '?'? '!'? '_'*;

// ----------------------------------------------------------------------
// |
// |  Parser Rules
// |
// ----------------------------------------------------------------------
// Note that any rule with a '__' suffix represents a non-binding rule (meaning a rule without
// backing code only here for organizational purposes).

entry_point__:                              NEWLINE* expression__* EOF;

// ----------------------------------------------------------------------
// |  Common
identifier:                                 IDENTIFIER;

// ----------------------------------------------------------------------
// |  Expressions
expression__:                               (
    include_expression
);

// BugBug // Import variations:
// BugBug //
// BugBug //   Module Imports:
// BugBug //     import (<filenamme>[ as <alias>])+
// BugBug //     from [/]<dir>[/<subdirs][/] import (<filename>[as <alias>])+
// BugBug //     from [/]<dir>[/<subdirs>][/] import *
// BugBug //
// BugBug //   Component Imports:
// BugBug //     from [[/]<dir>[/<subdirs>]/]<filename> import (<component>[as <alias>])+
// BugBug //     from [[/]<dir>[/<subdirs>]/]<filename> import *
// BugBug
include_expression:                         (INCLUDE_FROM include_expression_source)? INCLUDE_IMPORT (include_expression_star | include_expression_grouped_items__ | include_expression_items__) NEWLINE+;

include_expression_source:                  (
                                                '.'
                                                | (('./' | '/')? include_expression_source__ ('/' include_expression_source__)* '/'?)
                                            );

include_expression_source__:                identifier | include_expression_source_parent_dir;
include_expression_source_parent_dir:       '..';

include_expression_star:                    '*';
include_expression_items__:                 include_expression_element (',' include_expression_element)* ','?;
include_expression_grouped_items__:         LPAREN include_expression_items__ RPAREN;
include_expression_element:                 identifier ('as' identifier)?;

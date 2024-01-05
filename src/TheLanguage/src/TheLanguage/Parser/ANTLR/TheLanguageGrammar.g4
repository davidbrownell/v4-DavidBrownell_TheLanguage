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
    import_expression
);

// Import variations:
//
// import *                                                                 # All files that are siblings of the current file
// import <filename stems>
// import <filename stem>
// from . import *                                                          # All files that are siblings of the current file
// from . import <filename stems>
// from . import <filename stem>
// from <relative path to dir>/ import *                                    # All files within the specified directory
// from <relative path to dir>/ import <filename stems>
// from <relative path to dir>/ import <filename stem>
// from <relative path to file> import *                                    # All public exports in the specified file
// from <relative path to file> import <components>
// from <relative path to file> import <component>
// from /<WorkspaceName>[/<relative path to dir>]/ import *                 # All files within the specified directory
// from /<WorkspaceName>[/<relative path to dir>]/ import <filename stems>
// from /<WorkspaceName>[/<relative path to dir>]/ import <filename stem>
// from /<WorkspaceName>[/<relative path to file] import *                  # All public exports in the specified file
// from /<WorkspaceName>[/<relative path to file] import <components>
// from /<WorkspaceName>[/<relative path to file] import <component>
//
import_expression:                          (
                                                (INCLUDE_FROM import_expression_from__)?
                                                INCLUDE_IMPORT import_expression_import__
                                                NEWLINE+
                                            );

import_expression_from__:                   (
                                                import_expression_from_workspace_slash?
                                                import_expression_from_component
                                                ('/' import_expression_from_component)*
                                                import_expression_from_directory_slash?
                                            );

import_expression_from_workspace_slash:     '/';
import_expression_from_component:           '.' | '..' | identifier;
import_expression_from_directory_slash:     '/';

import_expression_import__:                 import_expression_import_star | import_expression_import_grouped_items__ | import_expression_import_items__;
import_expression_import_star:              '*';
import_expression_import_grouped_items__:   LPAREN import_expression_import_items__ RPAREN;
import_expression_import_items__:           import_expression_import_element (',' import_expression_import_element)* ','?;
import_expression_import_element:           identifier ('as' identifier)?;

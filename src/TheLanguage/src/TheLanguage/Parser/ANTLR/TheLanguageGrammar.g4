// ----------------------------------------------------------------------
// |
// |  TheLanguageGrammar.g4
// |
// |  David Brownell <db@DavidBrownell.com>
// |      2023-07-25 10:40:02
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
// TODO: We really want this to be any char that isn't defined elsewhere
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
    // BugBug identifier_expression
    include_expression
);

// BugBug identifier_expression:                      identifier NEWLINE+; // BugBug: This isn't a real expression

// Import variations:
//
//   Module Imports:
//     import (<filenamme>[ as <alias>])+
//     from [/]<dir>[/<subdirs][/] import (<filename>[as <alias>])+
//     from [/]<dir>[/<subdirs>][/] import *
//
//   Component Imports:
//     from [[/]<dir>[/<subdirs>]/]<filename> import (<component>[as <alias>])+
//     from [[/]<dir>[/<subdirs>]/]<filename> import *

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





// BugBug: LPAREN:                                     '(' {self._nested_pair_ctr += 1};
// BugBug: RPAREN:                                     ')' {self._nested_pair_ctr -= 1};
// BugBug: LBRACK:                                     '[' {self._nested_pair_ctr += 1};
// BugBug: RBRACK:                                     ']' {self._nested_pair_ctr -= 1};
// BugBug:
// BugBug: // ----------------------------------------------------------------------
// BugBug: // The following statements are used to differentiate between tokens lexed within an include statement
// BugBug: // (less restrictive) and tokens lexed outside of an include statement (more restrictive).
// BugBug: INCLUDE_FROM:                               'from' {self._lexing_include_filename = True};
// BugBug: INCLUDE_IMPORT:                             'import' {self._lexing_include_filename = False};
// BugBug:
// BugBug: // This is an overly-restrictive definition of what constitutes a valid filename, but erring on the side of caution.
// BugBug: INCLUDE_FILENAME:                           [a-zA-Z0-9_\-./]+ {self._lexing_include_filename}?;
// BugBug:
// BugBug: // ----------------------------------------------------------------------
// BugBug: MULTI_LINE_COMMENT:                         '#/' .*? '/#' -> skip;
// BugBug: SINGLE_LINE_COMMENT:                        '#' ~[\r\n]* -> skip;
// BugBug:
// BugBug: HORIZONTAL_WHITESPACE:                      [ \t]+ -> channel(HIDDEN);
// BugBug:
// BugBug: NUMBER:                                     '-'? [0-9]* '.' [0-9]+;
// BugBug: INTEGER:                                    '-'? [0-9]+;
// BugBug: IDENTIFIER:                                 [_@$&]? '_'* [a-zA-Z][a-zA-Z0-9_\-]*;
// BugBug:
// BugBug: DOUBLE_QUOTE_STRING:                        UNTERMINATED_DOUBLE_QUOTE_STRING '"';
// BugBug: UNTERMINATED_DOUBLE_QUOTE_STRING:           '"' ('\\"' | '\\\\' | ~'"')*?;
// BugBug:
// BugBug: SINGLE_QUOTE_STRING:                        UNTERMINATED_SINGLE_QUOTE_STRING '\'';
// BugBug: UNTERMINATED_SINGLE_QUOTE_STRING:           '\'' ('\\\'' | '\\\\' | ~'\'')*?;
// BugBug:
// BugBug: TRIPLE_DOUBLE_QUOTE_STRING:                 UNTERMINATED_TRIPLE_DOUBLE_QUOTE_STRING '"""';
// BugBug: UNTERMINATED_TRIPLE_DOUBLE_QUOTE_STRING:    '"""' .*?;
// BugBug:
// BugBug: TRIPLE_SINGLE_QUOTE_STRING:                 UNTERMINATED_TRIPLE_SINGLE_QUOTE_STRING '\'\'\'';
// BugBug: UNTERMINATED_TRIPLE_SINGLE_QUOTE_STRING:    '\'\'\'' .*?;
// BugBug:
// BugBug: // ----------------------------------------------------------------------
// BugBug: // |
// BugBug: // |  Parser Rules
// BugBug: // |
// BugBug: // ----------------------------------------------------------------------
// BugBug: // Note that any rule with a '__' suffix represents a non-binding rule (meaning a rule without
// BugBug: // backing code only here for organizational purposes).
// BugBug:
// BugBug: entry_point__:                              NEWLINE* header_statement__* body_statement__* EOF;
// BugBug:
// BugBug: // ----------------------------------------------------------------------
// BugBug: // |  Common
// BugBug: identifier:                                 IDENTIFIER;
// BugBug:
// BugBug: metadata_clause:                            '{' (metadata_clause_single_line__ | metadata_clause_multi_line__) '}';
// BugBug: metadata_clause_single_line__:              'pass' | (metadata_clause_item (',' metadata_clause_item)* ','?);
// BugBug: metadata_clause_multi_line__:               INDENT (
// BugBug:                                                 ('pass' NEWLINE+)
// BugBug:                                                 | (metadata_clause_item ','? NEWLINE+)+
// BugBug:                                             ) DEDENT;
// BugBug: metadata_clause_item:                       identifier ':' expression__;
// BugBug:
// BugBug: cardinality_clause:                         (
// BugBug:                                                 cardinality_clause_optional
// BugBug:                                                 | cardinality_clause_zero_or_more
// BugBug:                                                 | cardinality_clause_one_or_more
// BugBug:                                                 | cardinality_clause_fixed
// BugBug:                                                 | cardinality_clause_range__
// BugBug:                                             );
// BugBug:
// BugBug: cardinality_clause_optional:                '?';
// BugBug: cardinality_clause_zero_or_more:            '*';
// BugBug: cardinality_clause_one_or_more:             '+';
// BugBug: cardinality_clause_fixed:                   LBRACK integer_expression RBRACK;
// BugBug: cardinality_clause_range__:                 LBRACK integer_expression ',' integer_expression RBRACK;
// BugBug:
// BugBug: // ----------------------------------------------------------------------
// BugBug: // |  Expressions
// BugBug: expression__:                               (
// BugBug:                                                 number_expression
// BugBug:                                                 | integer_expression
// BugBug:                                                 | true_expression
// BugBug:                                                 | false_expression
// BugBug:                                                 | none_expression
// BugBug:                                                 | string_expression
// BugBug:                                                 | list_expression
// BugBug:                                                 | tuple_expression
// BugBug:                                             );
// BugBug:
// BugBug: number_expression:                          NUMBER;
// BugBug: integer_expression:                         INTEGER;
// BugBug: true_expression:                            'y' | 'Y' | 'yes' | 'Yes' | 'YES' | 'true' | 'True' | 'TRUE' | 'on' | 'On' | 'ON';
// BugBug: false_expression:                           'n' | 'N' | 'no' | 'No' | 'NO' | 'false' | 'False' | 'FALSE' | 'off' | 'Off' | 'OFF';
// BugBug: none_expression:                            'None';
// BugBug:
// BugBug: string_expression:                          DOUBLE_QUOTE_STRING | SINGLE_QUOTE_STRING | UNTERMINATED_DOUBLE_QUOTE_STRING | UNTERMINATED_SINGLE_QUOTE_STRING | TRIPLE_DOUBLE_QUOTE_STRING | TRIPLE_SINGLE_QUOTE_STRING;
// BugBug:
// BugBug: list_expression:                            LBRACK (expression__ (',' expression__)* ','?)? RBRACK;
// BugBug:
// BugBug: tuple_expression:                           LPAREN (tuple_expression_single_item__ | tuple_expression_multi_item__) RPAREN;
// BugBug: tuple_expression_single_item__:             expression__ ',';
// BugBug: tuple_expression_multi_item__:              expression__ (',' expression__)+ ','?;
// BugBug:
// BugBug: // ----------------------------------------------------------------------
// BugBug: // |  Statements
// BugBug:
// BugBug: // Header Statement
// BugBug: header_statement__:                         include_expression;
// BugBug:
// BugBug: include_expression:                          (INCLUDE_FROM include_expression_source)? INCLUDE_IMPORT (include_expression_star | include_expression_grouped_items__ | include_expression_items__) NEWLINE+;
// BugBug: include_expression_source:                 INCLUDE_FILENAME;
// BugBug: include_expression_star:                     '*';
// BugBug: include_expression_items__:                  include_expression_element (',' include_expression_element)* ','?;
// BugBug: include_expression_grouped_items__:          LPAREN include_expression_items__ RPAREN;
// BugBug: include_expression_element:                  identifier ('as' identifier)?;
// BugBug:
// BugBug: // Body Statements
// BugBug: body_statement__:                           (
// BugBug:                                                 parse_structure_statement
// BugBug:                                                 | parse_structure_simplified_statement
// BugBug:                                                 | parse_item_statement
// BugBug:                                                 | extension_statement
// BugBug:                                             );
// BugBug:
// BugBug: extension_statement:                        identifier LPAREN (
// BugBug:                                                 (
// BugBug:                                                     (
// BugBug:                                                         (extension_statement_positional_args ',' extension_statement_keyword_args)
// BugBug:                                                         | extension_statement_positional_args
// BugBug:                                                         | extension_statement_keyword_args
// BugBug:                                                     )
// BugBug:                                                     ','?
// BugBug:                                                 )?
// BugBug:                                             ) RPAREN NEWLINE+;
// BugBug:
// BugBug: extension_statement_positional_args:        expression__ (',' expression__)*;
// BugBug: extension_statement_keyword_args:           extension_statement_keyword_arg (',' extension_statement_keyword_arg)*;
// BugBug: extension_statement_keyword_arg:            identifier '=' expression__;
// BugBug:
// BugBug: parse_item_statement:                       identifier ':' parse_type NEWLINE+;
// BugBug:
// BugBug: parse_structure_statement:                  (
// BugBug:                                                 identifier
// BugBug:                                                     (':' (parse_structure_statement_base_grouped_items__ | parse_structure_statement_base_items__))?
// BugBug:                                                 '->'
// BugBug:                                                 INDENT (
// BugBug:                                                     ('pass' NEWLINE+)
// BugBug:                                                     | body_statement__+
// BugBug:                                                 ) DEDENT
// BugBug:                                                 (
// BugBug:                                                     (
// BugBug:                                                         (cardinality_clause NEWLINE* metadata_clause)
// BugBug:                                                         | metadata_clause
// BugBug:                                                         | cardinality_clause
// BugBug:                                                     )
// BugBug:                                                     NEWLINE+
// BugBug:                                                 )?
// BugBug:                                             );
// BugBug:
// BugBug: parse_structure_statement_base_items__:           parse_type (',' parse_type)* ','?;
// BugBug: parse_structure_statement_base_grouped_items__:   LPAREN parse_structure_statement_base_items__ RPAREN;
// BugBug:
// BugBug: parse_structure_simplified_statement:       identifier metadata_clause NEWLINE+;
// BugBug:
// BugBug: // ----------------------------------------------------------------------
// BugBug: // |  Types
// BugBug: parse_type:                                 (
// BugBug:                                                 parse_tuple_type
// BugBug:                                                 | parse_variant_type
// BugBug:                                                 | parse_identifier_type
// BugBug:                                             ) cardinality_clause? metadata_clause?;
// BugBug:
// BugBug: parse_identifier_type:                      parse_identifier_type_global? identifier ('.' identifier)* parse_identifier_type_item?;
// BugBug: parse_identifier_type_global:               '::';
// BugBug: parse_identifier_type_item:                 '::item';
// BugBug:
// BugBug: parse_tuple_type:                           LPAREN (parse_tuple_type_single_item__ | parse_tuple_type_multi_item__) RPAREN;
// BugBug: parse_tuple_type_single_item__:             parse_type ',';
// BugBug: parse_tuple_type_multi_item__:              parse_type (',' parse_type)+ ','?;
// BugBug:
// BugBug: parse_variant_type:                         LPAREN parse_type ('|' parse_type)* '|' parse_type RPAREN;
// BugBug:

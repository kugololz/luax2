%{
#include <stdio.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);
extern int yylineno;
extern char *yytext;
%}

%union {
    int intval;
    char *str;
}

%token AND BREAK DO ELSE ELSEIF END FALSE FOR FUNCTION IF IN LOCAL NIL NOT OR REPEAT RETURN THEN TRUE UNTIL WHILE PRINT
%token <str> IDENTIFIER STRING
%token <intval> NUMBER
%token EQ NEQ LEQ GEQ CONCAT

%left OR
%left AND
%left '<' '>' LEQ GEQ EQ NEQ
%left '+' '-'
%left '*' '/' '%'
%right '^'
%right NOT

%%

start:
    program
;

program:
    statement_list
;

statement_list:
    statement
    | statement_list statement
;

statement:
    if_statement
    | WHILE expression DO statement_list END
    | REPEAT statement_list UNTIL expression
    | FOR IDENTIFIER '=' expression ',' expression optional_expression DO statement_list END
    | FUNCTION IDENTIFIER '(' parameter_list ')' block END
    | LOCAL IDENTIFIER local_assignment opt_semi
    | IDENTIFIER '=' expression opt_semi
    | PRINT '(' expression ')' opt_semi
    | RETURN expression opt_semi
    | BREAK opt_semi
;

if_statement:
    IF expression THEN statement_list END
    | IF expression THEN statement_list elseif_clauses END
    | IF expression THEN statement_list elseif_clauses ELSE statement_list END
    | IF expression THEN statement_list ELSE statement_list END
;

elseif_clauses:
    ELSEIF expression THEN statement_list elseif_clauses
    | ELSEIF expression THEN statement_list
;

local_assignment:
    '=' expression
    | /* empty */
;

opt_semi:
    ';'
    | /* empty */
;

optional_expression:
    ',' expression
    | /* empty */
;

parameter_list:
    IDENTIFIER
    | parameter_list ',' IDENTIFIER
    | /* empty */
;

block:
    statement_list
;

expression:
    expression '+' expression
    | expression '-' expression
    | expression '*' expression
    | expression '/' expression
    | expression '%' expression
    | expression '^' expression
    | expression '<' expression
    | expression '>' expression
    | expression LEQ expression
    | expression GEQ expression
    | expression EQ expression
    | expression NEQ expression
    | expression AND expression
    | expression OR expression
    | NOT expression
    | IDENTIFIER
    | NUMBER
    | STRING
    | '(' expression ')'
    | function_call
;

function_call:
    IDENTIFIER '(' argument_list ')'
;

argument_list:
    expression
    | argument_list ',' expression
    | /* empty */
;

%%

int main(void) {
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    if (yytext[0] == '\0') {
        fprintf(stderr, "Error: %s at end of input on line %d\n", s, yylineno);
    } else {
        fprintf(stderr, "Error: %s at '%s' on line %d\n", s, yytext, yylineno);
    }
}

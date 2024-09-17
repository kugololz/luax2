%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "y.tab.h"

void yyerror(const char *s);
%}

DIGIT      [0-9]
ID         [a-zA-Z_][a-zA-Z0-9_]*
NUMBER     {DIGIT}+(\.[0-9]*)?([eE][-+]?{DIGIT}+)?
STRING     \"([^\\\n]|(\\.))*?\"

%%

"and"       { return AND; }
"break"     { return BREAK; }
"do"        { return DO; }
"else"      { return ELSE; }
"elseif"    { return ELSEIF; }
"end"       { return END; }
"false"     { return FALSE; }
"for"       { return FOR; }
"function"  { return FUNCTION; }
"if"        { return IF; }
"in"        { return IN; }
"local"     { return LOCAL; }
"nil"       { return NIL; }
"not"       { return NOT; }
"or"        { return OR; }
"repeat"    { return REPEAT; }
"return"    { return RETURN; }
"then"      { return THEN; }
"true"      { return TRUE; }
"until"     { return UNTIL; }
"while"     { return WHILE; }
"print"     { return PRINT; }

"="         { return '='; }
"=="        { return EQ; }
"~="        { return NEQ; }
"<="        { return LEQ; }
">="        { return GEQ; }
"<"         { return '<'; }
">"         { return '>'; }
"+"         { return '+'; }
"-"         { return '-'; }
"*"         { return '*'; }
"/"         { return '/'; }
"%"         { return '%'; }
"^"         { return '^'; }
"("         { return '('; }
")"         { return ')'; }
"{"         { return '{'; }
"}"         { return '}'; }
"["         { return '['; }
"]"         { return ']'; }
";"         { return ';'; }
","         { return ','; }
":"         { return ':'; }
"."         { return '.'; }
".. "       { return CONCAT; }

"--".*                           { }
"--\[\["([^]]|\][^]])*"\]\]"     { }

{NUMBER}    { yylval.intval = atoi(yytext); return NUMBER; }
{ID}        { yylval.str = strdup(yytext); return IDENTIFIER; }
{STRING}    { yylval.str = strdup(yytext); return STRING; }
[ \t\r]+    { }
\n          { yylineno++; } 

.           { printf("Unexpected character: %s\n", yytext); }

%%

int yywrap(void) { return 1; }
                
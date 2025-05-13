%{
#include <stdio.h>
#include <string.h>
%}

%option noyywrap
%option caseless

DIGIT      [0-9]
ID         [a-zA-Z_][a-zA-Z0-9_]*
NUM        {DIGIT}+
WS         [ \t\r\n]+

%%

"int"                  { printf("%s --> [Keyword]\n", yytext); }
"float"|"double"|"char"|"return" { printf("%s --> [Keyword]\n", yytext); }
"printf"               { printf("%s --> [Function Name]\n", yytext); }

{ID}                   { printf("%s --> [Identifier]\n", yytext); }
{NUM}                  { printf("%s --> [Number]\n", yytext); }

"="                    { printf("%s --> [Assignment Operator]\n", yytext); }
"+"|"-"|"*"|"/"        { printf("%s --> [Arithmetic Operator]\n", yytext); }
"=="|"!="              { printf("%s --> [Relational Operator]\n", yytext); }

";"                    { printf("%s --> [Semicolon]\n", yytext); }
","                    { printf("%s --> [Comma]\n", yytext); }
"("                    { printf("%s --> [Opening Parenthesis]\n", yytext); }
")"                    { printf("%s --> [Closing Parenthesis]\n", yytext); }
"\""                   { printf("%s --> [Double Quote]\n", yytext); }

{WS}                   { /* Ignore whitespace */ }

.                      { printf("%s --> [Unknown or Unhandled Character]\n", yytext); }

%%

int main() {
    char input[] = "{\nint total =100;\nint i=10;\nprintf(\"The value of total and i is : %d, %d\", total, i);\n}";
    YY_BUFFER_STATE buffer = yy_scan_string(input);
    yylex();
    yy_delete_buffer(buffer);
    return 0;
}

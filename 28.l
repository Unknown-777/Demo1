%{
#include <stdio.h>
#include <string.h>
%}

%option noyywrap
%option caseless

DIGIT      [0-9]
ID         [a-zA-Z_][a-zA-Z0-9_]*
CHAR       \'[a-zA-Z0-9]\'|[a-zA-Z]
STRING     \"([^"])*\"

%%

"char"                  { printf("%s --> [Keyword]\n", yytext); }
"int"|"float"|"double"|"return" { printf("%s --> [Keyword]\n", yytext); }
"printf"                { printf("%s --> [Function]\n", yytext); }

{STRING}                { printf("%s --> [String Literal]\n", yytext); }

{ID}                    { printf("%s --> [Identifier]\n", yytext); }
{DIGIT}+                { printf("%s --> [Number]\n", yytext); }

"="                     { printf("%s --> [Assignment Operator]\n", yytext); }
";"                     { printf("%s --> [Semicolon]\n", yytext); }
","                     { printf("%s --> [Comma]\n", yytext); }
"{"                     { printf("%s --> [Opening Brace]\n", yytext); }
"}"                     { printf("%s --> [Closing Brace]\n", yytext); }
"("                     { printf("%s --> [Opening Parenthesis]\n", yytext); }
")"                     { printf("%s --> [Closing Parenthesis]\n", yytext); }

[ \t\r\n]+              { /* skip whitespace */ }

.                       { printf("%s --> [Unknown or Unhandled Character]\n", yytext); }

%%

int main() {
    char input[] = "{\nchar = a;\nprintf(\"Hello World\");\n}";
    YY_BUFFER_STATE buffer = yy_scan_string(input);
    yylex();
    yy_delete_buffer(buffer);
    return 0;
}

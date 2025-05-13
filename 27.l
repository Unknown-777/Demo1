%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
int         { printf("Keyword: int\n"); }
[0-9]+      { printf("Integer Constant: %s\n", yytext); }
[ a-zA-Z_][a-zA-Z0-9_]*  { printf("Identifier: %s\n", yytext); }
"="         { printf("Assignment Operator: =\n"); }
"-"         { printf("Arithmetic Operator: -\n"); }
";"         { printf("Semicolon: ;\n"); }
\n          { /* Ignore newlines */ }
[ \t]       { /* Ignore whitespaces */ }

%%


int yywrap() {
    return 1;  // Indicate that the end of input has been reached
}

int main() {
    yylex();
    return 0;
}

%{
#include <stdio.h>
%}

%%
"Dread"                 { printf("%s - Verb\n", yytext); }
"Run"                   { printf("%s - Verb\n", yytext); }
"arrives"               { printf("%s - Verb\n", yytext); }
"Destiny"               { printf("%s - Noun\n", yytext); }
"it"                    { printf("%s - Pronoun\n", yytext); }
"from"                  { printf("%s - Preposition\n", yytext); }
"the"                   { printf("%s - Determiner\n", yytext); }
"same"                  { printf("%s - Adjective\n", yytext); }
[.!?\n]                 { /* Ignore punctuation and newline */ }
[ \t]+                  { /* Ignore whitespace */ }
.                       { printf("%s - Unknown\n", yytext); }
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
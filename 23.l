%{
#include <stdio.h>
%}

%option noyywrap

%%

"is"|"has"|"stop"|"exist"                              { printf("%s --> [Verb]\n", yytext); }
"to"|"for"|"of"|"in"|"on"|"with"                       { printf("%s --> [Preposition]\n", yytext); }
"the"|"a"|"an"|"its"|"The"|"Its"                       { printf("%s --> [Article/Determiner]\n", yytext); }
"and"|"or"|"but"                                       { printf("%s --> [Conjunction]\n", yytext); }
"important"|"own"|"existing"                           { printf("%s --> [Adjective]\n", yytext); }
"not"                                                 { printf("%s --> [Negation]\n", yytext); }
"thing"|"reason"|"curiosity"|"Curiosity"              { printf("%s --> [Noun]\n", yytext); }
"questioning"                                          { printf("%s --> [Gerund/Noun]\n", yytext); }

[ \t\n]+                                               { /* skip whitespace */ }
[,\.]                                                  { /* skip punctuation */ }

[a-zA-Z]+                                              { printf("%s --> [Unknown]\n", yytext); }
.                                                      { /* ignore all other single characters */ }

%%

int main() {
    printf("Enter input text:\n");
    yylex();
    return 0;
}

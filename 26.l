%{
#include <stdio.h>
%}

%%

"have"|"has"|"had"|"is"|"am"|"are"|"was"|"were"|"be"|"been"|"being"    { printf("%s : Verb\n", yytext); }

"strong"|"basic"|"dramatic"|"empty"|"binary"|"distinct"                { printf("%s : Adjective\n", yytext); }

"toward"|"into"|"in"|"with"|"between"                                  { printf("%s : Preposition\n", yytext); }

"Human"|"Beings"|"instinct"|"thinking"|"urge"|"gap"|"things"|"groups"  { printf("%s : Noun\n", yytext); }

"divide"|"think"                                                       { printf("%s : Verb\n", yytext); }

"nothing"|"but"                                                        { printf("%s : Determiner/Conjunction\n", yytext); }

"a"|"an"|"the"                                                         { printf("%s : Article\n", yytext); }

"and"|"or"|"with"                                                      { printf("%s : Conjunction\n", yytext); }

[.,]                                                                   { /* Ignore punctuation */ }

[ \t\n]+                                                               { /* Ignore whitespace */ }

[A-Za-z]+                                                              { printf("%s : Unknown Word\n", yytext); }

%%

int main() {
    printf("Enter the sentence:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}

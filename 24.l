%{
#include <stdio.h>
%}

%%

"you"|"it"                      { printf("%s : Pronoun\n", yytext); }
"the"                           { printf("%s : Article\n", yytext); }
"light"|"give"|"kill"|"needs"    { printf("%s : Verb\n", yytext); }
"cigarette"|"thing"|"power"      { printf("%s : Noun\n", yytext); }
"that"|"if"                      { printf("%s : Conjunction\n", yytext); }
"never"                          { printf("%s : Adverb\n", yytext); }
[.,]                             { }
[ \t\n]+                         { }
[A-Za-z]+                        { printf("%s : Unknown Word\n", yytext); }

%%

int main() {
    printf("Enter the sentence:\n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}

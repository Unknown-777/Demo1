%{
#include <stdio.h>
int yywrap(void) {
    return 1;
}
%}

%%

"Hello"|"hello"|"Hi"|"hi"|"Thank"|"thank"         { printf("%s - Interjection\n", yytext); }
"I"|"i"|"you"|"You"|"me"|"Me"|"we"|"We"            { printf("%s - Pronoun\n", yytext); }
"am"|"Am"|"are"|"Are"|"is"|"Is"|"’m"|"‘m"|"I'm"    { printf("%s - Verb\n", yytext); }
"fine"|"Fine"|"good"|"Good"                        { printf("%s - Adjective\n", yytext); }
"How"|"how"|"What"|"what"|"Why"|"why"              { printf("%s - Question Word\n", yytext); }

[.,!?']+                                           { /* Punctuation: ignore */ }
[ \t\n]+                                           { /* Whitespace: ignore */ }

[a-zA-Z]+                                          { printf("%s - Unknown Word\n", yytext); }

%%

int main() {
    printf("Enter text:\n");
    yylex();
    return 0;
}

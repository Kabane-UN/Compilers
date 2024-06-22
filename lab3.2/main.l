%option reentrant noyywrap bison-bridge bison-locations
%option extra-type="struct Extra *"

/* Подавление предупреждений для -Wall */
%option noinput nounput

%{

#include <stdio.h>
#include <stdlib.h>
#include "lexer.h"
#include "main.tab.h"  /* файл генерируется Bison’ом */

#define YY_USER_ACTION \
  { \
    int i; \
    struct Extra *extra = yyextra; \
    if (! extra->continued ) { \
      yylloc->first_line = extra->cur_line; \
      yylloc->first_column = extra->cur_column; \
    } \
    extra->continued = false; \
    for (i = 0; i < yyleng; ++i) { \
      if (yytext[i] == '\n') { \
        extra->cur_line += 1; \
        extra->cur_column = 1; \
      } else { \
        extra->cur_column += 1; \
      } \
    } \
    yylloc->last_line = extra->cur_line; \
    yylloc->last_column = extra->cur_column; \
  }

void yyerror(YYLTYPE *loc, yyscan_t scanner, long env[26], int i, int tab,  
    const char *message) {
    printf(" Error (%d,%d): %s\n", loc->first_line, loc->first_column, message);
}
%}
%%
[ \t\r]+

[\n]+ return KW_NEWLINE;

function return KW_FUNC;
end return KW_END;
for return KW_FOR;
next return KW_NEXT;
then return KW_THEN;
else return KW_ELSE;
do return KW_DO;
while return KW_WHILE;
until return KW_UNTIL;
loop return KW_LOOP;
dim return KW_DIM;
to return KW_TO;
if return KW_IF;
sub return KW_SUB;

== return KW_EQ;
\<> return KW_NE;
\<= return KW_LE;
>= return KW_GE;
\< return KW_LT; 
> return KW_GT;


=  return KW_ASSIGN;
\+  return KW_ADD;
\-  return KW_SUBB;
\*  return KW_MUL;
\/  return KW_DIV;
\( return KW_LEFT_PAREN;
\) return KW_RIGHT_PAREN;
\[ return KW_LEFT_RECT;
\] return KW_RIGHT_RECT;
,   return KW_COMMA;
% return KW_INT; 
\! return KW_LONG;
& return KW_FLOAT;
# return KW_DOUBLE;
\$ return KW_STRING;

[0-9]+ {
    yylval->number = atoi(yytext);
    return NUMBER;
}

[A-Za-z][A-Za-z0-9]*  {
    yylval->ident = yytext;
    return IDENT;
}
\".*\" {
    yylval->string = yytext;
    return STRING;
}

'[^\n]* {
    yylval->comment = yytext;
    return COMMENT;
}

%%

void init_scanner(FILE *input, yyscan_t *scanner, struct Extra *extra) {
    extra->continued = false;
    extra->cur_line = 1;
    extra->cur_column = 1;

    yylex_init(scanner);
    yylex_init_extra(extra, scanner);
    yyset_in(input, *scanner);
}

void destroy_scanner(yyscan_t scanner) {
    yylex_destroy(scanner);
}
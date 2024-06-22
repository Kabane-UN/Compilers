% "Лабораторная работа 3.2 «Форматтер исходных текстов»"
% <лабораторная ещё не сдана>
% Андрей Кабанов, ИУ9-62Б

# Цель работы

Целью данной работы является приобретение навыков использования генератора
синтаксических анализаторов bison.

# Индивидуальный вариант

Диалект Бейсика

```
' Суммирование элементов массива
Function SumArray#(Values#())
  SumArray# = 0
  For i% = 1 To Len%(Values#)
    SumArray# = SumArray# + Values#(i%)
  Next i%
End Function

' Вычисление многочлена по схеме Горнера
Function Polynom!(x!, coefs!())
  Polynom! = 0
  For i% = 1 to Len%(coefs!)
    Polynom! = Polynom! * x! + coefs!(i%)
  Next i%
End Function

' Вычисление многочлена x³ + x² + x + 1
Function Polynom1111!(x!)
  Dim coefs!(4)

  For i% = 1 To 4
    coefs!(i%) = 1
  Next i%

  Polynom1111! = Polynom!(x!, coefs!)
End Function

' Инициализация массива числами Фибоначчи
Sub Fibonacci(res&())
  n% = Len%(res&)

  If n% >= 1 Then
    res&(1) = 1
  End If

  If n% >= 2 Then
    res&(2) = 1
  End If

  i% = 3
  Do While i% <= n%
    ' длинные строки можно переносить знаком прочерка
    res&(i%) = res&(i% - 1) _
      + res&(i% - 2)
    i% = i% + 1
  Loop
End Sub

' Склеивание элементов массива через разделитель: Join$(", ", words)
Function Join$(sep$, items$())
  If Len(items$) >= 1 Then
    Join$ = items$[1]
  Else
    Join$ = ""
  End If

  For i% = 2 To Len%(items$)
    Join$ = Join$ + sep$ + items$(i%)
  Next i%
End Function
```

# Реализация

main.l

```
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
```

main.y

```
%{
#include <stdio.h>
#include "lexer.h"
%}
%define api.pure
%locations
%lex-param {yyscan_t scanner}  /* параметр для yylex() */
/* параметры для yyparse() */
%parse-param {yyscan_t scanner}
%parse-param {long env[26]}
%parse-param {int tab}

%union {
    long number;
    char* string;
    char* ident;
    char* comment;
}

%left KW_ADD KW_SUBB KW_MUL KW_DIV
%token KW_NEWLINE KW_FUNC KW_END KW_FOR KW_NEXT KW_THEN KW_ELSE KW_DO KW_WHILE KW_UNTIL 
%token KW_LOOP KW_DIM KW_TO KW_IF KW_SUB KW_EQ KW_NE KW_LE KW_GE KW_LT KW_GT
%token KW_ASSIGN KW_LEFT_PAREN KW_RIGHT_PAREN KW_COMMA KW_INT KW_LONG KW_FLOAT
%token KW_DOUBLE KW_STRING KW_LEFT_RECT KW_RIGHT_RECT

%token <number> NUMBER
%token <ident> IDENT
%token <string> STRING
%token <comment> COMMENT

%{
int yylex(YYSTYPE *yylval_param, YYLTYPE *yylloc_param, yyscan_t scanner);
void yyerror(YYLTYPE *loc, yyscan_t scanner, long env[26], int tab, const char *message);
%}

%{
void print_tabs(int tab) {
    for(int i = 0; i < tab; i++) {
        printf("  ");
    }
}


%}

%%
NOuterBlockStm:
        NSubDecl KW_NEWLINE {printf("\n");} NOuterBlockStm
        | NFuncDef KW_NEWLINE {printf("\n");} NOuterBlockStm 
        | NStm  KW_NEWLINE {printf("\n");} NOuterBlockStm 
        | COMMENT[C] {printf("%s", $C);} KW_NEWLINE {printf("\n");} NOuterBlockStm 
        | KW_NEWLINE {printf("\n");} NOuterBlockStm 
        | NSubDecl
        | NStm 
        | NFuncDef 
        | COMMENT[C] {printf("%s", $C);}
        |
        ;
NFuncDef: 
        KW_FUNC {printf("Function ");} NVar KW_LEFT_PAREN {printf("(");} NParams  
        KW_RIGHT_PAREN {printf(")");} KW_NEWLINE {printf("\n"); tab++;} NBlockStm
        KW_END {printf("End");} KW_FUNC {printf("Function"); tab--;}
        ;
NSubDecl:
        KW_SUB {printf("Sub ");} IDENT[L] {printf("%s", $L);} KW_LEFT_PAREN 
        {printf("(");} NParams  
        KW_RIGHT_PAREN {printf(")");} KW_NEWLINE {printf("\n"); tab++;} NBlockStm
        KW_END {printf("End ");} KW_SUB {printf("Sub"); tab--;}
        ;
NStm:   
        NVarDecl
        | NArrSet
        | NArrDecl
        | NIfStm
        | NForStm
        | NDoWhileStm
        | NDoUntilStm
        | NDoLoopStm
        | COMMENT[C] {printf("%s", $C);}
        ;
NParams: 
        NVar KW_COMMA {printf(", ");} NParams
        | NApply KW_COMMA {printf(", ");} NParams
        | NVar
        | NApply
        |
        ;
NVar: 
        IDENT[L] {printf("%s", $L);} NVarType
        ;
NVarType:
        KW_INT {printf("%");}
        | KW_LONG {printf("!");}  
        | KW_FLOAT {printf("&");}
        | KW_DOUBLE {printf("#");}
        | KW_STRING {printf("$");}
        ;
NBlockStm: 
        {print_tabs(tab);} NStm KW_NEWLINE {printf("\n");} NBlockStm 
        | KW_NEWLINE {print_tabs(tab); printf("\n");} NBlockStm
        |
        ;
NVarDecl: 
        NVar KW_ASSIGN {printf(" = ");} NExpr
        ;
NArrSet:
        NApply KW_ASSIGN {printf(" = ");} NExpr
        ;
NArrSet:
        NIndxes KW_ASSIGN {printf(" = ");} NExpr
        ;
NArrDecl:
        KW_DIM {printf("Dim ");} NApply
        ;
NApply: 
        NVar KW_LEFT_PAREN {printf("(");} NApplyArgs KW_RIGHT_PAREN {printf(")");}
        ;
NApplyArgs:
        NExpr KW_COMMA {printf(", ");} NApplyArgs
        | NExpr
        |
        ;
NExpr: 
        NTerm
        | NExpr KW_ADD {printf(" + ");} NTerm
        | NExpr KW_SUBB {printf(" - ");} NTerm
        ;
NTerm: 
        NPower
        | NTerm KW_MUL {printf(" * ");} NPower
        | NTerm KW_DIV {printf(" * ");} NPower
        ;
NPower: 
        NApply
        | NVar
        | NUMBER[N] {printf("%d", $N);}
        | STRING[S] {printf("%s", $S);}
        | NIndxes
        | KW_LEFT_PAREN {printf("(");} NExpr KW_RIGHT_PAREN {printf(")");}
        ;
NIndxes:
        NVar KW_LEFT_RECT {printf("[");} 
        NUMBER[N] {printf("%d", $N);} KW_RIGHT_RECT {printf("]");}
        | NVar KW_LEFT_RECT {printf("[");} STRING[S] {printf("%s", $S);}
         KW_RIGHT_RECT {printf("]");}
        ;
NCmpOp:
        KW_EQ {printf(" == ");}
        | KW_NE {printf(" <> ");}
        | KW_LT {printf(" < ");}
        | KW_LE {printf(" <= ");}
        | KW_GT {printf(" > ");}
        | KW_GE {printf(" >= ");}
        ;
NIfStm:
        KW_IF {printf("If ");} NExpr NCmpOp NExpr KW_THEN {printf(" Then");} 
        KW_NEWLINE {printf("\n"); tab++;} NBlockStm {tab--;} 
        NElseStm KW_END {print_tabs(tab);} {printf("End ");} KW_IF {printf("If"); }
        ;
NElseStm:
        {print_tabs(tab);} KW_ELSE {printf("Else");} KW_NEWLINE {printf("\n");tab++;}
        NBlockStm {tab--;}
        |
        ;
NForStm:
        KW_FOR {printf("For ");} NVarDecl KW_TO {printf(" To ");} NExpr 
        KW_NEWLINE {printf("\n"); tab++;} NBlockStm KW_NEXT { tab--;print_tabs(tab);} 
        {printf("Next ");} NVar
        ;
NDoWhileStm:
        KW_DO {printf("Do ");} KW_WHILE {printf("While ");} NExpr NCmpOp NExpr 
        KW_NEWLINE {printf("\n"); tab++;}
        NBlockStm { tab--;print_tabs(tab);} KW_LOOP {printf("Loop");}
        ;
NDoUntilStm:
        KW_DO {printf("Do ");} KW_UNTIL {printf("Until ");} NExpr NCmpOp NExpr 
        KW_NEWLINE {printf("\n"); tab++;}
        NBlockStm { tab--;print_tabs(tab);} KW_LOOP {printf("Loop");}
        ;
NDoLoopStm: 
        KW_DO {printf("Do ");} KW_NEWLINE {printf("\n"); tab++;}  NBlockStm 
        NDoLoopTailStm
        ;
NDoLoopTailStm:
        KW_LOOP {print_tabs(tab);tab--;} {printf("Loop");} KW_WHILE {printf("While ");}
        NExpr  NCmpOp  NExpr 
        | KW_LOOP {tab--; print_tabs(tab);} {printf("Loop");} 
        KW_UNTIL {printf("Until ");}
        NExpr  NCmpOp  NExpr 
        | KW_LOOP {tab--; print_tabs(tab);} {printf("Loop"); }
        ;

            
%%



int main(int argc, char *argv[]) {
    FILE *input = 0;
    long env[26] = { 0 };
    int tab = 0;
    yyscan_t scanner;
    struct Extra extra;

    if (argc > 1) {
        printf("Read file %s\n", argv[1]);
        input = fopen(argv[1], "r");
    } else {
        printf("No file in command line, use stdin\n");
        input = stdin;
    }
    init_scanner(input, &scanner, &extra);
    yyparse(scanner, env, tab);
    destroy_scanner(scanner);

    if (input != stdin) {
        fclose(input);
    }

    return 0;
}
```

lexer.h

```h
#ifndef LEXER_H
#define LEXER_H

#include <stdbool.h>
#include <stdio.h>

#ifndef YY_TYPEDEF_YY_SCANNER_T
#define YY_TYPEDEF_YY_SCANNER_T
typedef void *yyscan_t;
#endif

struct Extra {
    bool continued;
    int cur_line;
    int cur_column;
};

void init_scanner(FILE *input, yyscan_t *scanner, struct Extra *extra);
void destroy_scanner(yyscan_t);

#endif
```

# Тестирование

Входные данные

```
' Суммирование элементов массива
Function SumArray#(Values#())
SumArray#=0
For i% = 1 To Len%(Values#)
SumArray# = SumArray# + Values#(i%)
Next i%
                                                        End Function

' Вычисление многочлена по схеме Горнера
Function Polynom!(x!, coefs!())
  Polynom! = 0
  For i% = 1 to Len%(coefs!)
    Polynom! = Polynom! * x! + coefs!(i%)
  Next i%
End Function

' Вычисление многочлена x³ + x² + x + 1
Function Polynom1111!(x!)
                         Dim coefs!(4)

  For i% = 1 To 4
    coefs!(i%) = 1
  Next i%

  Polynom1111! = Polynom!(x!, coefs!)
End Function

' Инициализация массива числами Фибоначчи
Sub Fibonacci(res&())
  n% = Len%(res&)

  If n% >= 1 Then
    res&(1) = 1
  End If

  If n% >= 2 Then
    res&(2) = 1
  End If

  i% = 3
  Do While i% <= n%
    res&(i%) = res&(i% - 1) + res&(i% - 2)
    i% = i% + 1
  Loop
End Sub

' Склеивание элементов массива через разделитель: Join$(", ", words)
Function Join$(sep$, items$())
  If Len%(items$) >= 1 Then
    Join$ = items$[1]
  Else
    Join$ = ""
  End If

  For i% = 2 To Len%(items$)
    Join$ = Join$ + sep$ + items$(i%)
  Next i%
End Function
```

Вывод на `stdout`

```
' Суммирование элементов массива

Function SumArray#(Values#())
  SumArray# = 0
  For i = 1 To Len(Values#)
    SumArray# = SumArray# + Values#(i)
  Next i
EndFunction
' Вычисление многочлена по схеме Горнера

Function Polynom!(x!, coefs!())
  Polynom! = 0
  For i = 1 To Len(coefs!)
    Polynom! = Polynom! * x! + coefs!(i)
  Next i
EndFunction
' Вычисление многочлена x³ + x² + x + 1

Function Polynom1111!(x!)
  Dim coefs!(4)
  For i = 1 To 4
    coefs!(i) = 1
  Next i
  Polynom1111! = Polynom!(x!, coefs!)
EndFunction
' Инициализация массива числами Фибоначчи

Sub Fibonacci(res&())
  n = Len(res&)
  If n >= 1 Then
    res&(1) = 1
  End If
  If n >= 2 Then
    res&(2) = 1
  End If
  i = 3
  Do While i <= n
    res&(i) = res&(i - 1) + res&(i - 2)
    i = i + 1
  Loop
End Sub
' Склеивание элементов массива через разделитель: Join$(", ", words)

Function Join$(sep$, items$())
  If Len(items$) >= 1 Then
    Join$ = items$[1]
  Else
    Join$ = ""
  End If
  For i = 2 To Len(items$)
    Join$ = Join$ + sep$ + items$(i)
  Next i
```

# Вывод

При выполнении лабораторной работы были приобретены навыки написания лексического
анализатора на flex, синтаксического анализатора на bison. А также была изучена
техника написания слабого форматера.

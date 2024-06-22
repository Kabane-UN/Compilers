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
% Лабораторная работа № 1.5 «Порождение лексического анализатора с помощью flex»
% 18 марта 2024 г.
% Андрей Кабанов, ИУ9-62Б

# Цель работы
Целью данной работы является изучение генератора лексических анализаторов flex.

# Индивидуальный вариант
* Числа фибоначчиевой системы счисления: последовательности знаков «0» и «1»,
 причём две единицы не могут соседствовать друг с другом.
* Идентификаторы: последовательности латинских букв, в которых гласные и
 согласные чередуются.

# Реализация

```lex
%option noyywrap bison-bridge bison-locations
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAG_IDENT 1
#define TAG_FCN 2
#define TAG_ERROR 3
char *tagNames[] = {
    "END_OF_PROGRAM", "IDENT", "FCN", "ERROR"
};
typedef struct Position Position;
struct Position {
    long line, pos, index;
};
void print_pos(Position *p) {
    printf("(%d,%d)",p->line,p->pos);
}
typedef struct Fragment Fragment;
struct Fragment {
    Position starting, following;
};

typedef struct Fragment YYLTYPE;
void print_frag ( struct Fragment *f){
    print_pos (&( f->starting ));
    printf (" -");
    print_pos (&( f->following ));
}
union Token {
    int code;
    long num;
    char* str;
};
typedef union Token YYSTYPE;
int continued;
struct Position cur;
#define YY_USER_ACTION {             \
    int i;                           \
    if (!continued)                  \
        yylloc->starting = cur;      \
    continued = 0;                   \
    for ( i = 0; i < yyleng; i++){   \
        if ( yytext[i] == '\n'){     \
            cur.line++;              \
            cur.pos = 1;             \
        } else                       \
            cur.pos++;               \
        cur.index++;                 \
    }                                \
    yylloc->following = cur;         \
} 
void init_scanner ( char * program ){
    continued = 0;
    cur.line = 1;
    cur.pos = 1;
    cur.index = 0;
    yy_scan_string ( program );
}
typedef struct ErrorToken ErrorToken;
struct ErrorToken{
    Position* pos;
    char* msg;
};
ErrorToken** errors = NULL;
int errorsLen = 0;



void err (char *msg){
    printf ("Error");
    print_pos(&cur);
    printf(":%s\n",msg);
    if (!errors){
        errors = (ErrorToken**)malloc(sizeof(ErrorToken*));
    } else {
        errors = (ErrorToken**)realloc(errors, sizeof(ErrorToken*)*(errorsLen+=1));
    }
    ErrorToken* errToken;
    errToken->msg = msg;
    memcpy(errToken->pos, &cur, sizeof(Position*));
    errors[errorsLen] = errToken;
}

typedef struct Table Table;
struct Table {
    long len;
    char **values;
};
Table IdentTable;
void initTable(Table* table){
    table->len = 0;
    table->values = NULL;
}
int appendTable(Table* table, char* value){
    for (size_t i = 0; i < table->len; i++){
        if (!strcmp(value, table->values[i])){
            return i;
        }
    }
    if (!table->values){
        table->values = (char**)malloc(sizeof(char*));
    } else {
        table->values = (char**)realloc(table->values, sizeof(char*)*(table->len+1));
    }
    table->values[table->len] = (char*)malloc(sizeof(char)*strlen(value));
    strcpy(table->values[table->len], value);
    return (++(table->len)-1);
}
Table table;
long fib(char* fstr){
    int n = 0, first = 1, second = 2, next, c;
    c = 1;
    if (c <= 1)
      next = c;
    else
    {
      next = first + second;
      first = second;
      second = next;
    }
    int i = strlen(fstr)-1;
    goto sr;
    firr:
    if (c <= 1)
      next = c;
    else
    {
      next = first + second;
      first = second;
      second = next;
    }
    c++;
    goto tg;
    sr:
    int y = (int)(fstr[i]-'0');
    n += y * next;
    goto firr;
    tg:
    i--;
    if (i >= 0)
        goto sr;
    return n;
}
%}
FCN (1((0+1)|(0+))*)|(0)
VOWELS (a|e|y|u|i|o|j|A|E|Y|U|I|O|J)
CONSONANT (q|w|r|t|p|s|d|f|g|h|k|l|z|x|c|v|b|m|Q|W|R|T|P|S|D|F|G|H|K|L|Z|X|C|V|B|N|M)
IDENT ({VOWELS})|({CONSONANT})|({VOWELS}{CONSONANT})+|({CONSONANT}{VOWELS})+
%%
[\n\t ]+
{FCN} {
        yylval->num = fib(yytext);
        return TAG_FCN;
      }
{IDENT} {
            yylval->code = appendTable(&table, yytext);
            return TAG_IDENT;
        } 
.   {
        err("Unexpected character");
        return TAG_ERROR;
    }
<<EOF>> return 0;
%%
int main(){
    int tag;
    YYSTYPE value;
    YYLTYPE coords;
    FILE *inputFile;
	long size_str;
	char *str;
	union Token token;
	inputFile = fopen("test.txt","r");
	if (inputFile == NULL) {
		fputs("File not found", stderr);
		exit(1);
	}
	fseek(inputFile, 0,SEEK_END);
	size_str = ftell(inputFile);
    rewind(inputFile);
    str=(char*)malloc(sizeof(char)*(size_str+1));
    if (str == NULL) {
		fputs("Memory error",stderr);
		exit(2);
	}    
    size_t n = fread(str,sizeof(char),size_str,inputFile);
    if (n != size_str) {
		fputs ("Reading error",stderr);
		exit (3);
	}
    str[size_str] = '\0';
    fclose (inputFile);
    init_scanner(str);
    goto start;
    while (0 != tag) {
        start:
        tag = yylex(&value, &coords);
        if (0 != tag && TAG_ERROR != tag) {
		    printf("%s ", tagNames[tag]);
            print_frag(&coords);
            if (tag == 2) {
                printf(": %d\n", value.num);
            }
            if (tag == 1) {
                printf(": %s\n", table.values[value.code]);
            }
        }
    }
	free(str);
    for (size_t i = 0; i < table.len; i++){
        free(table.values[i]);
    }
    free(table.values);
    for (size_t i = 0; i < errorsLen; i++){
        free(errors[i]);
    }
    free(errors);
    return 0;
}
```

# Тестирование

Входные данные

```
10001 101
afer
1 1
aq g
```

Вывод на `stdout`

```
FCN (1,1) -(1,6): 9
FCN (1,7) -(1,10): 4
IDENT (2,1) -(2,5): afer
FCN (3,1) -(3,2): 1
FCN (3,3) -(3,4): 1
IDENT (4,1) -(4,3): aq
IDENT (4,4) -(4,5): g
```

# Вывод
При выполнения лабораторной работы были изучены основные принципы написания 
лексического анализатора на языке flex, также была изучена фибоначчиева система 
исчисления, и перевод чисел, записанных в ней, в обычную десятичную. 
Также был интересен тот факт, что flex поставляется вместе с gcc в базовом покете 
base-devel, то-есть по мнению мейнтейнеров является важным компонентом для сборки 
и разработки программ, что для меня было неожиданностью.
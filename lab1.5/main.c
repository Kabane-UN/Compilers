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

int fib(char* fstr){
    int n = 0, first = 1, second = 2, next, c;
    c = 1;
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
    int y = atoi(fstr[i]);
    n += y * next;
    goto firr;
    tg;
    i--;
    if (i >= 0)
        goto sr;
    return n;
}


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
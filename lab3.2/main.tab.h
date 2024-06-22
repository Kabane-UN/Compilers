/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_MAIN_TAB_H_INCLUDED
# define YY_YY_MAIN_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    KW_ADD = 258,                  /* KW_ADD  */
    KW_SUBB = 259,                 /* KW_SUBB  */
    KW_MUL = 260,                  /* KW_MUL  */
    KW_DIV = 261,                  /* KW_DIV  */
    KW_NEWLINE = 262,              /* KW_NEWLINE  */
    KW_FUNC = 263,                 /* KW_FUNC  */
    KW_END = 264,                  /* KW_END  */
    KW_FOR = 265,                  /* KW_FOR  */
    KW_NEXT = 266,                 /* KW_NEXT  */
    KW_THEN = 267,                 /* KW_THEN  */
    KW_ELSE = 268,                 /* KW_ELSE  */
    KW_DO = 269,                   /* KW_DO  */
    KW_WHILE = 270,                /* KW_WHILE  */
    KW_UNTIL = 271,                /* KW_UNTIL  */
    KW_LOOP = 272,                 /* KW_LOOP  */
    KW_DIM = 273,                  /* KW_DIM  */
    KW_TO = 274,                   /* KW_TO  */
    KW_IF = 275,                   /* KW_IF  */
    KW_SUB = 276,                  /* KW_SUB  */
    KW_EQ = 277,                   /* KW_EQ  */
    KW_NE = 278,                   /* KW_NE  */
    KW_LE = 279,                   /* KW_LE  */
    KW_GE = 280,                   /* KW_GE  */
    KW_LT = 281,                   /* KW_LT  */
    KW_GT = 282,                   /* KW_GT  */
    KW_ASSIGN = 283,               /* KW_ASSIGN  */
    KW_LEFT_PAREN = 284,           /* KW_LEFT_PAREN  */
    KW_RIGHT_PAREN = 285,          /* KW_RIGHT_PAREN  */
    KW_COMMA = 286,                /* KW_COMMA  */
    KW_INT = 287,                  /* KW_INT  */
    KW_LONG = 288,                 /* KW_LONG  */
    KW_FLOAT = 289,                /* KW_FLOAT  */
    KW_DOUBLE = 290,               /* KW_DOUBLE  */
    KW_STRING = 291,               /* KW_STRING  */
    KW_LEFT_RECT = 292,            /* KW_LEFT_RECT  */
    KW_RIGHT_RECT = 293,           /* KW_RIGHT_RECT  */
    NUMBER = 294,                  /* NUMBER  */
    IDENT = 295,                   /* IDENT  */
    STRING = 296,                  /* STRING  */
    COMMENT = 297                  /* COMMENT  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 13 "main.y"

    long number;
    char* string;
    char* ident;
    char* comment;

#line 113 "main.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif

/* Location type.  */
#if ! defined YYLTYPE && ! defined YYLTYPE_IS_DECLARED
typedef struct YYLTYPE YYLTYPE;
struct YYLTYPE
{
  int first_line;
  int first_column;
  int last_line;
  int last_column;
};
# define YYLTYPE_IS_DECLARED 1
# define YYLTYPE_IS_TRIVIAL 1
#endif




int yyparse (yyscan_t scanner, long env[26], int tab);


#endif /* !YY_YY_MAIN_TAB_H_INCLUDED  */

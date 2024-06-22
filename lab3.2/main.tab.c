/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison implementation for Yacc-like parsers in C

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

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output, and Bison version.  */
#define YYBISON 30802

/* Bison version string.  */
#define YYBISON_VERSION "3.8.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 1

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* First part of user prologue.  */
#line 1 "main.y"

#include <stdio.h>
#include "lexer.h"

#line 76 "main.tab.c"

# ifndef YY_CAST
#  ifdef __cplusplus
#   define YY_CAST(Type, Val) static_cast<Type> (Val)
#   define YY_REINTERPRET_CAST(Type, Val) reinterpret_cast<Type> (Val)
#  else
#   define YY_CAST(Type, Val) ((Type) (Val))
#   define YY_REINTERPRET_CAST(Type, Val) ((Type) (Val))
#  endif
# endif
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

#include "main.tab.h"
/* Symbol kind.  */
enum yysymbol_kind_t
{
  YYSYMBOL_YYEMPTY = -2,
  YYSYMBOL_YYEOF = 0,                      /* "end of file"  */
  YYSYMBOL_YYerror = 1,                    /* error  */
  YYSYMBOL_YYUNDEF = 2,                    /* "invalid token"  */
  YYSYMBOL_KW_ADD = 3,                     /* KW_ADD  */
  YYSYMBOL_KW_SUBB = 4,                    /* KW_SUBB  */
  YYSYMBOL_KW_MUL = 5,                     /* KW_MUL  */
  YYSYMBOL_KW_DIV = 6,                     /* KW_DIV  */
  YYSYMBOL_KW_NEWLINE = 7,                 /* KW_NEWLINE  */
  YYSYMBOL_KW_FUNC = 8,                    /* KW_FUNC  */
  YYSYMBOL_KW_END = 9,                     /* KW_END  */
  YYSYMBOL_KW_FOR = 10,                    /* KW_FOR  */
  YYSYMBOL_KW_NEXT = 11,                   /* KW_NEXT  */
  YYSYMBOL_KW_THEN = 12,                   /* KW_THEN  */
  YYSYMBOL_KW_ELSE = 13,                   /* KW_ELSE  */
  YYSYMBOL_KW_DO = 14,                     /* KW_DO  */
  YYSYMBOL_KW_WHILE = 15,                  /* KW_WHILE  */
  YYSYMBOL_KW_UNTIL = 16,                  /* KW_UNTIL  */
  YYSYMBOL_KW_LOOP = 17,                   /* KW_LOOP  */
  YYSYMBOL_KW_DIM = 18,                    /* KW_DIM  */
  YYSYMBOL_KW_TO = 19,                     /* KW_TO  */
  YYSYMBOL_KW_IF = 20,                     /* KW_IF  */
  YYSYMBOL_KW_SUB = 21,                    /* KW_SUB  */
  YYSYMBOL_KW_EQ = 22,                     /* KW_EQ  */
  YYSYMBOL_KW_NE = 23,                     /* KW_NE  */
  YYSYMBOL_KW_LE = 24,                     /* KW_LE  */
  YYSYMBOL_KW_GE = 25,                     /* KW_GE  */
  YYSYMBOL_KW_LT = 26,                     /* KW_LT  */
  YYSYMBOL_KW_GT = 27,                     /* KW_GT  */
  YYSYMBOL_KW_ASSIGN = 28,                 /* KW_ASSIGN  */
  YYSYMBOL_KW_LEFT_PAREN = 29,             /* KW_LEFT_PAREN  */
  YYSYMBOL_KW_RIGHT_PAREN = 30,            /* KW_RIGHT_PAREN  */
  YYSYMBOL_KW_COMMA = 31,                  /* KW_COMMA  */
  YYSYMBOL_KW_INT = 32,                    /* KW_INT  */
  YYSYMBOL_KW_LONG = 33,                   /* KW_LONG  */
  YYSYMBOL_KW_FLOAT = 34,                  /* KW_FLOAT  */
  YYSYMBOL_KW_DOUBLE = 35,                 /* KW_DOUBLE  */
  YYSYMBOL_KW_STRING = 36,                 /* KW_STRING  */
  YYSYMBOL_KW_LEFT_RECT = 37,              /* KW_LEFT_RECT  */
  YYSYMBOL_KW_RIGHT_RECT = 38,             /* KW_RIGHT_RECT  */
  YYSYMBOL_NUMBER = 39,                    /* NUMBER  */
  YYSYMBOL_IDENT = 40,                     /* IDENT  */
  YYSYMBOL_STRING = 41,                    /* STRING  */
  YYSYMBOL_COMMENT = 42,                   /* COMMENT  */
  YYSYMBOL_YYACCEPT = 43,                  /* $accept  */
  YYSYMBOL_NOuterBlockStm = 44,            /* NOuterBlockStm  */
  YYSYMBOL_45_1 = 45,                      /* $@1  */
  YYSYMBOL_46_2 = 46,                      /* $@2  */
  YYSYMBOL_47_3 = 47,                      /* $@3  */
  YYSYMBOL_48_4 = 48,                      /* $@4  */
  YYSYMBOL_49_5 = 49,                      /* $@5  */
  YYSYMBOL_50_6 = 50,                      /* $@6  */
  YYSYMBOL_NFuncDef = 51,                  /* NFuncDef  */
  YYSYMBOL_52_7 = 52,                      /* $@7  */
  YYSYMBOL_53_8 = 53,                      /* $@8  */
  YYSYMBOL_54_9 = 54,                      /* $@9  */
  YYSYMBOL_55_10 = 55,                     /* $@10  */
  YYSYMBOL_56_11 = 56,                     /* $@11  */
  YYSYMBOL_NSubDecl = 57,                  /* NSubDecl  */
  YYSYMBOL_58_12 = 58,                     /* $@12  */
  YYSYMBOL_59_13 = 59,                     /* $@13  */
  YYSYMBOL_60_14 = 60,                     /* $@14  */
  YYSYMBOL_61_15 = 61,                     /* $@15  */
  YYSYMBOL_62_16 = 62,                     /* $@16  */
  YYSYMBOL_63_17 = 63,                     /* $@17  */
  YYSYMBOL_NStm = 64,                      /* NStm  */
  YYSYMBOL_NParams = 65,                   /* NParams  */
  YYSYMBOL_66_18 = 66,                     /* $@18  */
  YYSYMBOL_67_19 = 67,                     /* $@19  */
  YYSYMBOL_NVar = 68,                      /* NVar  */
  YYSYMBOL_69_20 = 69,                     /* $@20  */
  YYSYMBOL_NVarType = 70,                  /* NVarType  */
  YYSYMBOL_NBlockStm = 71,                 /* NBlockStm  */
  YYSYMBOL_72_21 = 72,                     /* $@21  */
  YYSYMBOL_73_22 = 73,                     /* $@22  */
  YYSYMBOL_74_23 = 74,                     /* $@23  */
  YYSYMBOL_NVarDecl = 75,                  /* NVarDecl  */
  YYSYMBOL_76_24 = 76,                     /* $@24  */
  YYSYMBOL_NArrSet = 77,                   /* NArrSet  */
  YYSYMBOL_78_25 = 78,                     /* $@25  */
  YYSYMBOL_79_26 = 79,                     /* $@26  */
  YYSYMBOL_NArrDecl = 80,                  /* NArrDecl  */
  YYSYMBOL_81_27 = 81,                     /* $@27  */
  YYSYMBOL_NApply = 82,                    /* NApply  */
  YYSYMBOL_83_28 = 83,                     /* $@28  */
  YYSYMBOL_NApplyArgs = 84,                /* NApplyArgs  */
  YYSYMBOL_85_29 = 85,                     /* $@29  */
  YYSYMBOL_NExpr = 86,                     /* NExpr  */
  YYSYMBOL_87_30 = 87,                     /* $@30  */
  YYSYMBOL_88_31 = 88,                     /* $@31  */
  YYSYMBOL_NTerm = 89,                     /* NTerm  */
  YYSYMBOL_90_32 = 90,                     /* $@32  */
  YYSYMBOL_91_33 = 91,                     /* $@33  */
  YYSYMBOL_NPower = 92,                    /* NPower  */
  YYSYMBOL_93_34 = 93,                     /* $@34  */
  YYSYMBOL_NIndxes = 94,                   /* NIndxes  */
  YYSYMBOL_95_35 = 95,                     /* $@35  */
  YYSYMBOL_96_36 = 96,                     /* $@36  */
  YYSYMBOL_97_37 = 97,                     /* $@37  */
  YYSYMBOL_98_38 = 98,                     /* $@38  */
  YYSYMBOL_NCmpOp = 99,                    /* NCmpOp  */
  YYSYMBOL_NIfStm = 100,                   /* NIfStm  */
  YYSYMBOL_101_39 = 101,                   /* $@39  */
  YYSYMBOL_102_40 = 102,                   /* $@40  */
  YYSYMBOL_103_41 = 103,                   /* $@41  */
  YYSYMBOL_104_42 = 104,                   /* $@42  */
  YYSYMBOL_105_43 = 105,                   /* $@43  */
  YYSYMBOL_106_44 = 106,                   /* $@44  */
  YYSYMBOL_NElseStm = 107,                 /* NElseStm  */
  YYSYMBOL_108_45 = 108,                   /* $@45  */
  YYSYMBOL_109_46 = 109,                   /* $@46  */
  YYSYMBOL_110_47 = 110,                   /* $@47  */
  YYSYMBOL_NForStm = 111,                  /* NForStm  */
  YYSYMBOL_112_48 = 112,                   /* $@48  */
  YYSYMBOL_113_49 = 113,                   /* $@49  */
  YYSYMBOL_114_50 = 114,                   /* $@50  */
  YYSYMBOL_115_51 = 115,                   /* $@51  */
  YYSYMBOL_116_52 = 116,                   /* $@52  */
  YYSYMBOL_NDoWhileStm = 117,              /* NDoWhileStm  */
  YYSYMBOL_118_53 = 118,                   /* $@53  */
  YYSYMBOL_119_54 = 119,                   /* $@54  */
  YYSYMBOL_120_55 = 120,                   /* $@55  */
  YYSYMBOL_121_56 = 121,                   /* $@56  */
  YYSYMBOL_NDoUntilStm = 122,              /* NDoUntilStm  */
  YYSYMBOL_123_57 = 123,                   /* $@57  */
  YYSYMBOL_124_58 = 124,                   /* $@58  */
  YYSYMBOL_125_59 = 125,                   /* $@59  */
  YYSYMBOL_126_60 = 126,                   /* $@60  */
  YYSYMBOL_NDoLoopStm = 127,               /* NDoLoopStm  */
  YYSYMBOL_128_61 = 128,                   /* $@61  */
  YYSYMBOL_129_62 = 129,                   /* $@62  */
  YYSYMBOL_NDoLoopTailStm = 130,           /* NDoLoopTailStm  */
  YYSYMBOL_131_63 = 131,                   /* $@63  */
  YYSYMBOL_132_64 = 132,                   /* $@64  */
  YYSYMBOL_133_65 = 133,                   /* $@65  */
  YYSYMBOL_134_66 = 134,                   /* $@66  */
  YYSYMBOL_135_67 = 135,                   /* $@67  */
  YYSYMBOL_136_68 = 136,                   /* $@68  */
  YYSYMBOL_137_69 = 137                    /* $@69  */
};
typedef enum yysymbol_kind_t yysymbol_kind_t;


/* Second part of user prologue.  */
#line 31 "main.y"

int yylex(YYSTYPE *yylval_param, YYLTYPE *yylloc_param, yyscan_t scanner);
void yyerror(YYLTYPE *loc, yyscan_t scanner, long env[26], int tab, const char *message);
#line 36 "main.y"

void print_tabs(int tab) {
    for(int i = 0; i < tab; i++) {
        printf("  ");
    }
}



#line 261 "main.tab.c"


#ifdef short
# undef short
#endif

/* On compilers that do not define __PTRDIFF_MAX__ etc., make sure
   <limits.h> and (if available) <stdint.h> are included
   so that the code can choose integer types of a good width.  */

#ifndef __PTRDIFF_MAX__
# include <limits.h> /* INFRINGES ON USER NAME SPACE */
# if defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stdint.h> /* INFRINGES ON USER NAME SPACE */
#  define YY_STDINT_H
# endif
#endif

/* Narrow types that promote to a signed type and that can represent a
   signed or unsigned integer of at least N bits.  In tables they can
   save space and decrease cache pressure.  Promoting to a signed type
   helps avoid bugs in integer arithmetic.  */

#ifdef __INT_LEAST8_MAX__
typedef __INT_LEAST8_TYPE__ yytype_int8;
#elif defined YY_STDINT_H
typedef int_least8_t yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef __INT_LEAST16_MAX__
typedef __INT_LEAST16_TYPE__ yytype_int16;
#elif defined YY_STDINT_H
typedef int_least16_t yytype_int16;
#else
typedef short yytype_int16;
#endif

/* Work around bug in HP-UX 11.23, which defines these macros
   incorrectly for preprocessor constants.  This workaround can likely
   be removed in 2023, as HPE has promised support for HP-UX 11.23
   (aka HP-UX 11i v2) only through the end of 2022; see Table 2 of
   <https://h20195.www2.hpe.com/V2/getpdf.aspx/4AA4-7673ENW.pdf>.  */
#ifdef __hpux
# undef UINT_LEAST8_MAX
# undef UINT_LEAST16_MAX
# define UINT_LEAST8_MAX 255
# define UINT_LEAST16_MAX 65535
#endif

#if defined __UINT_LEAST8_MAX__ && __UINT_LEAST8_MAX__ <= __INT_MAX__
typedef __UINT_LEAST8_TYPE__ yytype_uint8;
#elif (!defined __UINT_LEAST8_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST8_MAX <= INT_MAX)
typedef uint_least8_t yytype_uint8;
#elif !defined __UINT_LEAST8_MAX__ && UCHAR_MAX <= INT_MAX
typedef unsigned char yytype_uint8;
#else
typedef short yytype_uint8;
#endif

#if defined __UINT_LEAST16_MAX__ && __UINT_LEAST16_MAX__ <= __INT_MAX__
typedef __UINT_LEAST16_TYPE__ yytype_uint16;
#elif (!defined __UINT_LEAST16_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST16_MAX <= INT_MAX)
typedef uint_least16_t yytype_uint16;
#elif !defined __UINT_LEAST16_MAX__ && USHRT_MAX <= INT_MAX
typedef unsigned short yytype_uint16;
#else
typedef int yytype_uint16;
#endif

#ifndef YYPTRDIFF_T
# if defined __PTRDIFF_TYPE__ && defined __PTRDIFF_MAX__
#  define YYPTRDIFF_T __PTRDIFF_TYPE__
#  define YYPTRDIFF_MAXIMUM __PTRDIFF_MAX__
# elif defined PTRDIFF_MAX
#  ifndef ptrdiff_t
#   include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  endif
#  define YYPTRDIFF_T ptrdiff_t
#  define YYPTRDIFF_MAXIMUM PTRDIFF_MAX
# else
#  define YYPTRDIFF_T long
#  define YYPTRDIFF_MAXIMUM LONG_MAX
# endif
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM                                  \
  YY_CAST (YYPTRDIFF_T,                                 \
           (YYPTRDIFF_MAXIMUM < YY_CAST (YYSIZE_T, -1)  \
            ? YYPTRDIFF_MAXIMUM                         \
            : YY_CAST (YYSIZE_T, -1)))

#define YYSIZEOF(X) YY_CAST (YYPTRDIFF_T, sizeof (X))


/* Stored state numbers (used for stacks). */
typedef yytype_uint8 yy_state_t;

/* State numbers in computations.  */
typedef int yy_state_fast_t;

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif


#ifndef YY_ATTRIBUTE_PURE
# if defined __GNUC__ && 2 < __GNUC__ + (96 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_PURE __attribute__ ((__pure__))
# else
#  define YY_ATTRIBUTE_PURE
# endif
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# if defined __GNUC__ && 2 < __GNUC__ + (7 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_UNUSED __attribute__ ((__unused__))
# else
#  define YY_ATTRIBUTE_UNUSED
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YY_USE(E) ((void) (E))
#else
# define YY_USE(E) /* empty */
#endif

/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
#if defined __GNUC__ && ! defined __ICC && 406 <= __GNUC__ * 100 + __GNUC_MINOR__
# if __GNUC__ * 100 + __GNUC_MINOR__ < 407
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")
# else
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")              \
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# endif
# define YY_IGNORE_MAYBE_UNINITIALIZED_END      \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

#if defined __cplusplus && defined __GNUC__ && ! defined __ICC && 6 <= __GNUC__
# define YY_IGNORE_USELESS_CAST_BEGIN                          \
    _Pragma ("GCC diagnostic push")                            \
    _Pragma ("GCC diagnostic ignored \"-Wuseless-cast\"")
# define YY_IGNORE_USELESS_CAST_END            \
    _Pragma ("GCC diagnostic pop")
#endif
#ifndef YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_END
#endif


#define YY_ASSERT(E) ((void) (0 && (E)))

#if !defined yyoverflow

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* !defined yyoverflow */

#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL \
             && defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yy_state_t yyss_alloc;
  YYSTYPE yyvs_alloc;
  YYLTYPE yyls_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (YYSIZEOF (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (YYSIZEOF (yy_state_t) + YYSIZEOF (YYSTYPE) \
             + YYSIZEOF (YYLTYPE)) \
      + 2 * YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYPTRDIFF_T yynewbytes;                                         \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * YYSIZEOF (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / YYSIZEOF (*yyptr);                        \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, YY_CAST (YYSIZE_T, (Count)) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYPTRDIFF_T yyi;                      \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  36
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   207

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  43
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  95
/* YYNRULES -- Number of rules.  */
#define YYNRULES  143
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  227

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   297


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK                     \
   ? YY_CAST (yysymbol_kind_t, yytranslate[YYX])        \
   : YYSYMBOL_YYUNDEF)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_int8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint8 yyrline[] =
{
       0,    48,    48,    48,    49,    49,    50,    50,    51,    51,
      51,    52,    52,    53,    54,    55,    56,    57,    60,    60,
      61,    61,    62,    60,    65,    65,    65,    66,    66,    67,
      65,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      81,    81,    82,    82,    83,    84,    85,    88,    88,    91,
      92,    93,    94,    95,    98,    98,    98,    99,    99,   100,
     103,   103,   106,   106,   109,   109,   112,   112,   115,   115,
     118,   118,   119,   120,   123,   124,   124,   125,   125,   128,
     129,   129,   130,   130,   133,   134,   135,   136,   137,   138,
     138,   141,   141,   141,   142,   142,   142,   145,   146,   147,
     148,   149,   150,   153,   153,   154,   154,   154,   154,   153,
     157,   157,   157,   157,   159,   162,   162,   163,   163,   163,
     162,   166,   166,   167,   168,   166,   171,   171,   172,   173,
     171,   176,   176,   176,   180,   180,   180,   180,   182,   182,
     182,   182,   184,   184
};
#endif

/** Accessing symbol of state STATE.  */
#define YY_ACCESSING_SYMBOL(State) YY_CAST (yysymbol_kind_t, yystos[State])

#if YYDEBUG || 0
/* The user-facing name of the symbol whose (internal) number is
   YYSYMBOL.  No bounds checking.  */
static const char *yysymbol_name (yysymbol_kind_t yysymbol) YY_ATTRIBUTE_UNUSED;

/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "\"end of file\"", "error", "\"invalid token\"", "KW_ADD", "KW_SUBB",
  "KW_MUL", "KW_DIV", "KW_NEWLINE", "KW_FUNC", "KW_END", "KW_FOR",
  "KW_NEXT", "KW_THEN", "KW_ELSE", "KW_DO", "KW_WHILE", "KW_UNTIL",
  "KW_LOOP", "KW_DIM", "KW_TO", "KW_IF", "KW_SUB", "KW_EQ", "KW_NE",
  "KW_LE", "KW_GE", "KW_LT", "KW_GT", "KW_ASSIGN", "KW_LEFT_PAREN",
  "KW_RIGHT_PAREN", "KW_COMMA", "KW_INT", "KW_LONG", "KW_FLOAT",
  "KW_DOUBLE", "KW_STRING", "KW_LEFT_RECT", "KW_RIGHT_RECT", "NUMBER",
  "IDENT", "STRING", "COMMENT", "$accept", "NOuterBlockStm", "$@1", "$@2",
  "$@3", "$@4", "$@5", "$@6", "NFuncDef", "$@7", "$@8", "$@9", "$@10",
  "$@11", "NSubDecl", "$@12", "$@13", "$@14", "$@15", "$@16", "$@17",
  "NStm", "NParams", "$@18", "$@19", "NVar", "$@20", "NVarType",
  "NBlockStm", "$@21", "$@22", "$@23", "NVarDecl", "$@24", "NArrSet",
  "$@25", "$@26", "NArrDecl", "$@27", "NApply", "$@28", "NApplyArgs",
  "$@29", "NExpr", "$@30", "$@31", "NTerm", "$@32", "$@33", "NPower",
  "$@34", "NIndxes", "$@35", "$@36", "$@37", "$@38", "NCmpOp", "NIfStm",
  "$@39", "$@40", "$@41", "$@42", "$@43", "$@44", "NElseStm", "$@45",
  "$@46", "$@47", "NForStm", "$@48", "$@49", "$@50", "$@51", "$@52",
  "NDoWhileStm", "$@53", "$@54", "$@55", "$@56", "NDoUntilStm", "$@57",
  "$@58", "$@59", "$@60", "NDoLoopStm", "$@61", "$@62", "NDoLoopTailStm",
  "$@63", "$@64", "$@65", "$@66", "$@67", "$@68", "$@69", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-142)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-139)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
     109,  -142,  -142,  -142,    46,  -142,  -142,  -142,  -142,    22,
      28,    25,    31,    57,    -8,  -142,  -142,  -142,    42,    85,
    -142,  -142,  -142,  -142,  -142,   109,    45,    45,    76,    89,
     111,    45,    20,    82,    61,   121,  -142,  -142,  -142,  -142,
    -142,  -142,   100,  -142,  -142,  -142,   131,   134,   142,  -142,
    -142,  -142,   137,  -142,  -142,  -142,  -142,    38,  -142,   130,
      63,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,
    -142,   109,   109,   109,    20,    20,   124,   126,    20,    20,
    -142,  -142,    20,    20,    -1,    20,  -142,  -142,  -142,  -142,
    -142,  -142,  -142,  -142,    20,  -142,  -142,   139,   109,  -142,
    -142,  -142,   108,   141,    10,  -142,  -142,   108,   108,    45,
      20,   130,   130,  -142,   155,    -3,    15,    20,    20,    62,
      20,    20,  -142,  -142,  -142,  -142,   138,   140,   143,     4,
     146,   128,    20,    20,    33,   110,  -142,  -142,   172,  -142,
      63,    63,  -142,  -142,  -142,    45,    20,  -142,  -142,  -142,
    -142,  -142,  -142,   133,   135,  -142,  -142,  -142,  -142,  -142,
     173,   151,  -142,   175,    45,    45,     1,  -142,  -142,   168,
     169,    33,  -142,  -142,  -142,  -142,  -142,   176,    -1,    -1,
    -142,  -142,  -142,    77,   177,   101,  -142,  -142,  -142,    20,
      20,  -142,  -142,   179,  -142,   174,   178,   130,   130,   180,
     101,  -142,    45,  -142,  -142,    20,    20,   181,   183,   184,
     186,  -142,   108,   108,  -142,  -142,  -142,  -142,  -142,   185,
     165,   187,  -142,  -142,  -142,   101,  -142
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
      17,    11,    18,   115,   121,    66,   103,    24,    47,     8,
       0,    15,    13,    14,     0,    31,    32,    33,     0,     0,
      34,    35,    36,    37,    38,    17,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     1,     4,     2,     6,
      60,    68,    91,    62,    64,    12,     0,     0,     0,   122,
     127,   132,     0,    67,    89,    86,    87,    85,    84,     0,
      74,    79,    88,    25,    49,    50,    51,    52,    53,    48,
       9,    17,    17,    17,     0,    73,     0,     0,     0,     0,
      19,   116,     0,     0,    54,     0,    75,    77,    97,    98,
     100,   102,    99,   101,     0,    80,    82,     0,    17,     5,
       3,     7,    61,     0,    72,    92,    95,    63,    65,    46,
       0,     0,     0,    57,     0,     0,     0,     0,     0,     0,
       0,     0,    26,    10,    69,    70,     0,     0,     0,    44,
      45,     0,     0,     0,    54,   142,   133,    39,     0,    90,
      76,    78,   104,    81,    83,    46,    73,    93,    96,    20,
      40,    42,   117,     0,     0,    58,   135,   139,   143,    55,
       0,     0,    71,     0,    46,    46,    54,   123,   128,     0,
       0,    54,   105,    27,    21,    41,    43,     0,    54,    54,
     136,   140,    56,    54,     0,    54,   118,   124,   129,     0,
       0,   106,    28,     0,   119,     0,     0,     0,     0,   110,
      54,    22,     0,   125,   130,     0,     0,     0,     0,     0,
       0,   120,   137,   141,   107,   111,    29,    23,   108,     0,
       0,     0,   112,    30,   109,    54,   113
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -142,   -15,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,
    -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,
    -142,    83,  -141,  -142,  -142,     0,  -142,  -142,   -79,  -142,
    -142,  -142,   170,  -142,  -142,  -142,  -142,  -142,  -142,     5,
    -142,    53,  -142,   -31,  -142,  -142,    26,  -142,  -142,    27,
    -142,     9,  -142,  -142,  -142,  -142,  -109,  -142,  -142,  -142,
    -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,
    -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,
    -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,  -142,
    -142,  -142,  -142,  -142,  -142
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_uint8 yydefgoto[] =
{
       0,    10,    72,    71,    73,    35,    98,    25,    11,    26,
     109,   163,   185,   210,    12,    33,    97,   145,   184,   200,
     220,    13,   128,   164,   165,    57,    34,    69,   114,   115,
     171,   134,    15,    74,    16,    78,    79,    17,    31,    58,
      75,   103,   146,   104,   117,   118,    60,   120,   121,    61,
      85,    62,    76,   126,    77,   127,    94,    20,    32,   160,
     183,   199,   218,   221,   207,   208,   219,   225,    21,    27,
     110,   166,   194,   202,    22,    28,    82,   178,   195,    23,
      29,    83,   179,   196,    24,    30,    84,   136,   156,   169,
     189,   157,   170,   190,   158
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      14,    59,   132,   133,   161,    18,   113,     3,   113,    19,
      45,     4,   -59,    86,    87,     5,   -59,     6,    86,    87,
      40,    41,   -16,   175,   176,    14,    46,    47,    36,    42,
      18,    52,    37,    41,    19,   150,    53,     8,    38,   137,
     113,   125,   -59,   102,   -59,   139,   -59,   107,   108,    54,
     -59,   111,   112,  -131,   116,   155,    99,   100,   101,    55,
       8,    56,  -126,   119,    39,    86,    87,    41,    95,    96,
      43,    14,    14,    14,   142,    42,    18,    18,    18,   131,
      19,    19,    19,   123,   113,     8,   -59,   177,   205,   206,
     -59,    49,   182,    64,    65,    66,    67,    68,    14,   187,
     188,   153,   154,    18,   191,    50,   193,    19,   113,   129,
     -59,    86,    87,    44,   130,    14,     1,     2,    51,     3,
      18,   209,    63,     4,    19,  -134,  -138,     5,    70,     6,
       7,    86,    87,    86,    87,   152,    86,    87,    86,    87,
     167,   -94,   168,   140,   141,   129,   226,   143,   144,     8,
     130,     9,    88,    89,    90,    91,    92,    93,   197,   198,
      80,    81,    40,   105,   129,   129,    41,   106,   122,   130,
     130,   124,   135,   149,   212,   213,   147,   151,   148,   159,
     172,   173,   174,   180,   192,   181,   223,   186,   201,  -114,
     214,   203,   222,   216,   217,   204,   215,    48,   138,   162,
       0,     0,   211,     0,     0,     0,     0,   224
};

static const yytype_int16 yycheck[] =
{
       0,    32,   111,   112,   145,     0,     7,    10,     7,     0,
      25,    14,    11,     3,     4,    18,    17,    20,     3,     4,
      28,    29,     0,   164,   165,    25,    26,    27,     0,    37,
      25,    31,     7,    29,    25,    31,    31,    40,     7,    42,
       7,    31,     9,    74,    11,    30,    13,    78,    79,    29,
      17,    82,    83,     7,    85,   134,    71,    72,    73,    39,
      40,    41,    16,    94,     7,     3,     4,    29,     5,     6,
      28,    71,    72,    73,    12,    37,    71,    72,    73,   110,
      71,    72,    73,    98,     7,    40,     9,   166,   197,   198,
      13,    15,   171,    32,    33,    34,    35,    36,    98,   178,
     179,   132,   133,    98,   183,    16,   185,    98,     7,   109,
       9,     3,     4,    28,   109,   115,     7,     8,     7,    10,
     115,   200,    40,    14,   115,    15,    16,    18,     7,    20,
      21,     3,     4,     3,     4,     7,     3,     4,     3,     4,
       7,    41,     7,   117,   118,   145,   225,   120,   121,    40,
     145,    42,    22,    23,    24,    25,    26,    27,   189,   190,
      29,    19,    28,    39,   164,   165,    29,    41,    29,   164,
     165,    30,    17,    30,   205,   206,    38,    31,    38,     7,
       7,    30,     7,    15,     7,    16,    21,    11,     9,     9,
       9,    17,     7,     9,     8,    17,    13,    27,   115,   146,
      -1,    -1,   202,    -1,    -1,    -1,    -1,    20
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     7,     8,    10,    14,    18,    20,    21,    40,    42,
      44,    51,    57,    64,    68,    75,    77,    80,    82,    94,
     100,   111,   117,   122,   127,    50,    52,   112,   118,   123,
     128,    81,   101,    58,    69,    48,     0,     7,     7,     7,
      28,    29,    37,    28,    28,    44,    68,    68,    75,    15,
      16,     7,    68,    82,    29,    39,    41,    68,    82,    86,
      89,    92,    94,    40,    32,    33,    34,    35,    36,    70,
       7,    46,    45,    47,    76,    83,    95,    97,    78,    79,
      29,    19,   119,   124,   129,    93,     3,     4,    22,    23,
      24,    25,    26,    27,    99,     5,     6,    59,    49,    44,
      44,    44,    86,    84,    86,    39,    41,    86,    86,    53,
     113,    86,    86,     7,    71,    72,    86,    87,    88,    86,
      90,    91,    29,    44,    30,    31,    96,    98,    65,    68,
      82,    86,    99,    99,    74,    17,   130,    42,    64,    30,
      89,    89,    12,    92,    92,    60,    85,    38,    38,    30,
      31,    31,     7,    86,    86,    71,   131,   134,   137,     7,
     102,    65,    84,    54,    66,    67,   114,     7,     7,   132,
     135,    73,     7,    30,     7,    65,    65,    71,   120,   125,
      15,    16,    71,   103,    61,    55,    11,    71,    71,   133,
     136,    71,     7,    71,   115,   121,   126,    86,    86,   104,
      62,     9,   116,    17,    17,    99,    99,   107,   108,    71,
      56,    68,    86,    86,     9,    13,     9,     8,   105,   109,
      63,   106,     7,    21,    20,   110,    71
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,    43,    45,    44,    46,    44,    47,    44,    48,    49,
      44,    50,    44,    44,    44,    44,    44,    44,    52,    53,
      54,    55,    56,    51,    58,    59,    60,    61,    62,    63,
      57,    64,    64,    64,    64,    64,    64,    64,    64,    64,
      66,    65,    67,    65,    65,    65,    65,    69,    68,    70,
      70,    70,    70,    70,    72,    73,    71,    74,    71,    71,
      76,    75,    78,    77,    79,    77,    81,    80,    83,    82,
      85,    84,    84,    84,    86,    87,    86,    88,    86,    89,
      90,    89,    91,    89,    92,    92,    92,    92,    92,    93,
      92,    95,    96,    94,    97,    98,    94,    99,    99,    99,
      99,    99,    99,   101,   102,   103,   104,   105,   106,   100,
     108,   109,   110,   107,   107,   112,   113,   114,   115,   116,
     111,   118,   119,   120,   121,   117,   123,   124,   125,   126,
     122,   128,   129,   127,   131,   132,   133,   130,   134,   135,
     136,   130,   137,   130
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     0,     4,     0,     4,     0,     4,     0,     0,
       5,     0,     3,     1,     1,     1,     1,     0,     0,     0,
       0,     0,     0,    14,     0,     0,     0,     0,     0,     0,
      15,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       0,     4,     0,     4,     1,     1,     0,     0,     3,     1,
       1,     1,     1,     1,     0,     0,     5,     0,     3,     0,
       0,     4,     0,     4,     0,     4,     0,     3,     0,     5,
       0,     4,     1,     0,     1,     0,     4,     0,     4,     1,
       0,     4,     0,     4,     1,     1,     1,     1,     1,     0,
       4,     0,     0,     6,     0,     0,     6,     1,     1,     1,
       1,     1,     1,     0,     0,     0,     0,     0,     0,    16,
       0,     0,     0,     6,     0,     0,     0,     0,     0,     0,
      13,     0,     0,     0,     0,    12,     0,     0,     0,     0,
      12,     0,     0,     6,     0,     0,     0,     8,     0,     0,
       0,     8,     0,     2
};


enum { YYENOMEM = -2 };

#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab
#define YYNOMEM         goto yyexhaustedlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (yychar == YYEMPTY)                                        \
      {                                                           \
        yychar = (Token);                                         \
        yylval = (Value);                                         \
        YYPOPSTACK (yylen);                                       \
        yystate = *yyssp;                                         \
        goto yybackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        yyerror (&yylloc, scanner, env, tab, YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Backward compatibility with an undocumented macro.
   Use YYerror or YYUNDEF. */
#define YYERRCODE YYUNDEF

/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)                                \
    do                                                                  \
      if (N)                                                            \
        {                                                               \
          (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;        \
          (Current).first_column = YYRHSLOC (Rhs, 1).first_column;      \
          (Current).last_line    = YYRHSLOC (Rhs, N).last_line;         \
          (Current).last_column  = YYRHSLOC (Rhs, N).last_column;       \
        }                                                               \
      else                                                              \
        {                                                               \
          (Current).first_line   = (Current).last_line   =              \
            YYRHSLOC (Rhs, 0).last_line;                                \
          (Current).first_column = (Current).last_column =              \
            YYRHSLOC (Rhs, 0).last_column;                              \
        }                                                               \
    while (0)
#endif

#define YYRHSLOC(Rhs, K) ((Rhs)[K])


/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)


/* YYLOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

# ifndef YYLOCATION_PRINT

#  if defined YY_LOCATION_PRINT

   /* Temporary convenience wrapper in case some people defined the
      undocumented and private YY_LOCATION_PRINT macros.  */
#   define YYLOCATION_PRINT(File, Loc)  YY_LOCATION_PRINT(File, *(Loc))

#  elif defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL

/* Print *YYLOCP on YYO.  Private, do not rely on its existence. */

YY_ATTRIBUTE_UNUSED
static int
yy_location_print_ (FILE *yyo, YYLTYPE const * const yylocp)
{
  int res = 0;
  int end_col = 0 != yylocp->last_column ? yylocp->last_column - 1 : 0;
  if (0 <= yylocp->first_line)
    {
      res += YYFPRINTF (yyo, "%d", yylocp->first_line);
      if (0 <= yylocp->first_column)
        res += YYFPRINTF (yyo, ".%d", yylocp->first_column);
    }
  if (0 <= yylocp->last_line)
    {
      if (yylocp->first_line < yylocp->last_line)
        {
          res += YYFPRINTF (yyo, "-%d", yylocp->last_line);
          if (0 <= end_col)
            res += YYFPRINTF (yyo, ".%d", end_col);
        }
      else if (0 <= end_col && yylocp->first_column < end_col)
        res += YYFPRINTF (yyo, "-%d", end_col);
    }
  return res;
}

#   define YYLOCATION_PRINT  yy_location_print_

    /* Temporary convenience wrapper in case some people defined the
       undocumented and private YY_LOCATION_PRINT macros.  */
#   define YY_LOCATION_PRINT(File, Loc)  YYLOCATION_PRINT(File, &(Loc))

#  else

#   define YYLOCATION_PRINT(File, Loc) ((void) 0)
    /* Temporary convenience wrapper in case some people defined the
       undocumented and private YY_LOCATION_PRINT macros.  */
#   define YY_LOCATION_PRINT  YYLOCATION_PRINT

#  endif
# endif /* !defined YYLOCATION_PRINT */


# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Kind, Value, Location, scanner, env, tab); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
yy_symbol_value_print (FILE *yyo,
                       yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep, YYLTYPE const * const yylocationp, yyscan_t scanner, long env[26], int tab)
{
  FILE *yyoutput = yyo;
  YY_USE (yyoutput);
  YY_USE (yylocationp);
  YY_USE (scanner);
  YY_USE (env);
  YY_USE (tab);
  if (!yyvaluep)
    return;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
yy_symbol_print (FILE *yyo,
                 yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep, YYLTYPE const * const yylocationp, yyscan_t scanner, long env[26], int tab)
{
  YYFPRINTF (yyo, "%s %s (",
             yykind < YYNTOKENS ? "token" : "nterm", yysymbol_name (yykind));

  YYLOCATION_PRINT (yyo, yylocationp);
  YYFPRINTF (yyo, ": ");
  yy_symbol_value_print (yyo, yykind, yyvaluep, yylocationp, scanner, env, tab);
  YYFPRINTF (yyo, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yy_state_t *yybottom, yy_state_t *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yy_state_t *yyssp, YYSTYPE *yyvsp, YYLTYPE *yylsp,
                 int yyrule, yyscan_t scanner, long env[26], int tab)
{
  int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %d):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       YY_ACCESSING_SYMBOL (+yyssp[yyi + 1 - yynrhs]),
                       &yyvsp[(yyi + 1) - (yynrhs)],
                       &(yylsp[(yyi + 1) - (yynrhs)]), scanner, env, tab);
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, yylsp, Rule, scanner, env, tab); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args) ((void) 0)
# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif






/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg,
            yysymbol_kind_t yykind, YYSTYPE *yyvaluep, YYLTYPE *yylocationp, yyscan_t scanner, long env[26], int tab)
{
  YY_USE (yyvaluep);
  YY_USE (yylocationp);
  YY_USE (scanner);
  YY_USE (env);
  YY_USE (tab);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yykind, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}






/*----------.
| yyparse.  |
`----------*/

int
yyparse (yyscan_t scanner, long env[26], int tab)
{
/* Lookahead token kind.  */
int yychar;


/* The semantic value of the lookahead symbol.  */
/* Default value used for initialization, for pacifying older GCCs
   or non-GCC compilers.  */
YY_INITIAL_VALUE (static YYSTYPE yyval_default;)
YYSTYPE yylval YY_INITIAL_VALUE (= yyval_default);

/* Location data for the lookahead symbol.  */
static YYLTYPE yyloc_default
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL
  = { 1, 1, 1, 1 }
# endif
;
YYLTYPE yylloc = yyloc_default;

    /* Number of syntax errors so far.  */
    int yynerrs = 0;

    yy_state_fast_t yystate = 0;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus = 0;

    /* Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* Their size.  */
    YYPTRDIFF_T yystacksize = YYINITDEPTH;

    /* The state stack: array, bottom, top.  */
    yy_state_t yyssa[YYINITDEPTH];
    yy_state_t *yyss = yyssa;
    yy_state_t *yyssp = yyss;

    /* The semantic value stack: array, bottom, top.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs = yyvsa;
    YYSTYPE *yyvsp = yyvs;

    /* The location stack: array, bottom, top.  */
    YYLTYPE yylsa[YYINITDEPTH];
    YYLTYPE *yyls = yylsa;
    YYLTYPE *yylsp = yyls;

  int yyn;
  /* The return value of yyparse.  */
  int yyresult;
  /* Lookahead symbol kind.  */
  yysymbol_kind_t yytoken = YYSYMBOL_YYEMPTY;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;
  YYLTYPE yyloc;

  /* The locations where the error started and ended.  */
  YYLTYPE yyerror_range[3];



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N), yylsp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yychar = YYEMPTY; /* Cause a token to be read.  */

  yylsp[0] = yylloc;
  goto yysetstate;


/*------------------------------------------------------------.
| yynewstate -- push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;


/*--------------------------------------------------------------------.
| yysetstate -- set current state (the top of the stack) to yystate.  |
`--------------------------------------------------------------------*/
yysetstate:
  YYDPRINTF ((stderr, "Entering state %d\n", yystate));
  YY_ASSERT (0 <= yystate && yystate < YYNSTATES);
  YY_IGNORE_USELESS_CAST_BEGIN
  *yyssp = YY_CAST (yy_state_t, yystate);
  YY_IGNORE_USELESS_CAST_END
  YY_STACK_PRINT (yyss, yyssp);

  if (yyss + yystacksize - 1 <= yyssp)
#if !defined yyoverflow && !defined YYSTACK_RELOCATE
    YYNOMEM;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYPTRDIFF_T yysize = yyssp - yyss + 1;

# if defined yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        yy_state_t *yyss1 = yyss;
        YYSTYPE *yyvs1 = yyvs;
        YYLTYPE *yyls1 = yyls;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * YYSIZEOF (*yyssp),
                    &yyvs1, yysize * YYSIZEOF (*yyvsp),
                    &yyls1, yysize * YYSIZEOF (*yylsp),
                    &yystacksize);
        yyss = yyss1;
        yyvs = yyvs1;
        yyls = yyls1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        YYNOMEM;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yy_state_t *yyss1 = yyss;
        union yyalloc *yyptr =
          YY_CAST (union yyalloc *,
                   YYSTACK_ALLOC (YY_CAST (YYSIZE_T, YYSTACK_BYTES (yystacksize))));
        if (! yyptr)
          YYNOMEM;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
        YYSTACK_RELOCATE (yyls_alloc, yyls);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;
      yylsp = yyls + yysize - 1;

      YY_IGNORE_USELESS_CAST_BEGIN
      YYDPRINTF ((stderr, "Stack size increased to %ld\n",
                  YY_CAST (long, yystacksize)));
      YY_IGNORE_USELESS_CAST_END

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }
#endif /* !defined yyoverflow && !defined YYSTACK_RELOCATE */


  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;


/*-----------.
| yybackup.  |
`-----------*/
yybackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either empty, or end-of-input, or a valid lookahead.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token\n"));
      yychar = yylex (&yylval, &yylloc, scanner);
    }

  if (yychar <= YYEOF)
    {
      yychar = YYEOF;
      yytoken = YYSYMBOL_YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else if (yychar == YYerror)
    {
      /* The scanner already issued an error message, process directly
         to error recovery.  But do not keep the error token as
         lookahead, it is too special and may lead us to an endless
         loop in error recovery. */
      yychar = YYUNDEF;
      yytoken = YYSYMBOL_YYerror;
      yyerror_range[1] = yylloc;
      goto yyerrlab1;
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);
  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END
  *++yylsp = yylloc;

  /* Discard the shifted token.  */
  yychar = YYEMPTY;
  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];

  /* Default location. */
  YYLLOC_DEFAULT (yyloc, (yylsp - yylen), yylen);
  yyerror_range[1] = yyloc;
  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
  case 2: /* $@1: %empty  */
#line 48 "main.y"
                            {printf("\n");}
#line 1520 "main.tab.c"
    break;

  case 4: /* $@2: %empty  */
#line 49 "main.y"
                              {printf("\n");}
#line 1526 "main.tab.c"
    break;

  case 6: /* $@3: %empty  */
#line 50 "main.y"
                           {printf("\n");}
#line 1532 "main.tab.c"
    break;

  case 8: /* $@4: %empty  */
#line 51 "main.y"
                     {printf("%s", (yyvsp[0].comment));}
#line 1538 "main.tab.c"
    break;

  case 9: /* $@5: %empty  */
#line 51 "main.y"
                                                    {printf("\n");}
#line 1544 "main.tab.c"
    break;

  case 11: /* $@6: %empty  */
#line 52 "main.y"
                     {printf("\n");}
#line 1550 "main.tab.c"
    break;

  case 16: /* NOuterBlockStm: COMMENT  */
#line 56 "main.y"
                     {printf("%s", (yyvsp[0].comment));}
#line 1556 "main.tab.c"
    break;

  case 18: /* $@7: %empty  */
#line 60 "main.y"
                {printf("Function ");}
#line 1562 "main.tab.c"
    break;

  case 19: /* $@8: %empty  */
#line 60 "main.y"
                                                          {printf("(");}
#line 1568 "main.tab.c"
    break;

  case 20: /* $@9: %empty  */
#line 61 "main.y"
                       {printf(")");}
#line 1574 "main.tab.c"
    break;

  case 21: /* $@10: %empty  */
#line 61 "main.y"
                                                 {printf("\n"); tab++;}
#line 1580 "main.tab.c"
    break;

  case 22: /* $@11: %empty  */
#line 62 "main.y"
               {printf("End");}
#line 1586 "main.tab.c"
    break;

  case 23: /* NFuncDef: KW_FUNC $@7 NVar KW_LEFT_PAREN $@8 NParams KW_RIGHT_PAREN $@9 KW_NEWLINE $@10 NBlockStm KW_END $@11 KW_FUNC  */
#line 62 "main.y"
                                        {printf("Function"); tab--;}
#line 1592 "main.tab.c"
    break;

  case 24: /* $@12: %empty  */
#line 65 "main.y"
               {printf("Sub ");}
#line 1598 "main.tab.c"
    break;

  case 25: /* $@13: %empty  */
#line 65 "main.y"
                                          {printf("%s", (yyvsp[0].ident));}
#line 1604 "main.tab.c"
    break;

  case 26: /* $@14: %empty  */
#line 65 "main.y"
                                                                            {printf("(");}
#line 1610 "main.tab.c"
    break;

  case 27: /* $@15: %empty  */
#line 66 "main.y"
                       {printf(")");}
#line 1616 "main.tab.c"
    break;

  case 28: /* $@16: %empty  */
#line 66 "main.y"
                                                 {printf("\n"); tab++;}
#line 1622 "main.tab.c"
    break;

  case 29: /* $@17: %empty  */
#line 67 "main.y"
               {printf("End ");}
#line 1628 "main.tab.c"
    break;

  case 30: /* NSubDecl: KW_SUB $@12 IDENT $@13 KW_LEFT_PAREN $@14 NParams KW_RIGHT_PAREN $@15 KW_NEWLINE $@16 NBlockStm KW_END $@17 KW_SUB  */
#line 67 "main.y"
                                        {printf("Sub"); tab--;}
#line 1634 "main.tab.c"
    break;

  case 39: /* NStm: COMMENT  */
#line 78 "main.y"
                     {printf("%s", (yyvsp[0].comment));}
#line 1640 "main.tab.c"
    break;

  case 40: /* $@18: %empty  */
#line 81 "main.y"
                      {printf(", ");}
#line 1646 "main.tab.c"
    break;

  case 42: /* $@19: %empty  */
#line 82 "main.y"
                          {printf(", ");}
#line 1652 "main.tab.c"
    break;

  case 47: /* $@20: %empty  */
#line 88 "main.y"
                 {printf("%s", (yyvsp[0].ident));}
#line 1658 "main.tab.c"
    break;

  case 49: /* NVarType: KW_INT  */
#line 91 "main.y"
               {printf("%");}
#line 1664 "main.tab.c"
    break;

  case 50: /* NVarType: KW_LONG  */
#line 92 "main.y"
                  {printf("!");}
#line 1670 "main.tab.c"
    break;

  case 51: /* NVarType: KW_FLOAT  */
#line 93 "main.y"
                   {printf("&");}
#line 1676 "main.tab.c"
    break;

  case 52: /* NVarType: KW_DOUBLE  */
#line 94 "main.y"
                    {printf("#");}
#line 1682 "main.tab.c"
    break;

  case 53: /* NVarType: KW_STRING  */
#line 95 "main.y"
                    {printf("$");}
#line 1688 "main.tab.c"
    break;

  case 54: /* $@21: %empty  */
#line 98 "main.y"
        {print_tabs(tab);}
#line 1694 "main.tab.c"
    break;

  case 55: /* $@22: %empty  */
#line 98 "main.y"
                                           {printf("\n");}
#line 1700 "main.tab.c"
    break;

  case 57: /* $@23: %empty  */
#line 99 "main.y"
                     {print_tabs(tab); printf("\n");}
#line 1706 "main.tab.c"
    break;

  case 60: /* $@24: %empty  */
#line 103 "main.y"
                       {printf(" = ");}
#line 1712 "main.tab.c"
    break;

  case 62: /* $@25: %empty  */
#line 106 "main.y"
                         {printf(" = ");}
#line 1718 "main.tab.c"
    break;

  case 64: /* $@26: %empty  */
#line 109 "main.y"
                          {printf(" = ");}
#line 1724 "main.tab.c"
    break;

  case 66: /* $@27: %empty  */
#line 112 "main.y"
               {printf("Dim ");}
#line 1730 "main.tab.c"
    break;

  case 68: /* $@28: %empty  */
#line 115 "main.y"
                           {printf("(");}
#line 1736 "main.tab.c"
    break;

  case 69: /* NApply: NVar KW_LEFT_PAREN $@28 NApplyArgs KW_RIGHT_PAREN  */
#line 115 "main.y"
                                                                    {printf(")");}
#line 1742 "main.tab.c"
    break;

  case 70: /* $@29: %empty  */
#line 118 "main.y"
                       {printf(", ");}
#line 1748 "main.tab.c"
    break;

  case 75: /* $@30: %empty  */
#line 124 "main.y"
                       {printf(" + ");}
#line 1754 "main.tab.c"
    break;

  case 77: /* $@31: %empty  */
#line 125 "main.y"
                        {printf(" - ");}
#line 1760 "main.tab.c"
    break;

  case 80: /* $@32: %empty  */
#line 129 "main.y"
                       {printf(" * ");}
#line 1766 "main.tab.c"
    break;

  case 82: /* $@33: %empty  */
#line 130 "main.y"
                       {printf(" * ");}
#line 1772 "main.tab.c"
    break;

  case 86: /* NPower: NUMBER  */
#line 135 "main.y"
                    {printf("%d", (yyvsp[0].number));}
#line 1778 "main.tab.c"
    break;

  case 87: /* NPower: STRING  */
#line 136 "main.y"
                    {printf("%s", (yyvsp[0].string));}
#line 1784 "main.tab.c"
    break;

  case 89: /* $@34: %empty  */
#line 138 "main.y"
                        {printf("(");}
#line 1790 "main.tab.c"
    break;

  case 90: /* NPower: KW_LEFT_PAREN $@34 NExpr KW_RIGHT_PAREN  */
#line 138 "main.y"
                                                            {printf(")");}
#line 1796 "main.tab.c"
    break;

  case 91: /* $@35: %empty  */
#line 141 "main.y"
                          {printf("[");}
#line 1802 "main.tab.c"
    break;

  case 92: /* $@36: %empty  */
#line 141 "main.y"
                                                   {printf("%d", (yyvsp[0].number));}
#line 1808 "main.tab.c"
    break;

  case 93: /* NIndxes: NVar KW_LEFT_RECT $@35 NUMBER $@36 KW_RIGHT_RECT  */
#line 141 "main.y"
                                                                                     {printf("]");}
#line 1814 "main.tab.c"
    break;

  case 94: /* $@37: %empty  */
#line 142 "main.y"
                            {printf("[");}
#line 1820 "main.tab.c"
    break;

  case 95: /* $@38: %empty  */
#line 142 "main.y"
                                                     {printf("%s", (yyvsp[0].string));}
#line 1826 "main.tab.c"
    break;

  case 96: /* NIndxes: NVar KW_LEFT_RECT $@37 STRING $@38 KW_RIGHT_RECT  */
#line 142 "main.y"
                                                                                       {printf("]");}
#line 1832 "main.tab.c"
    break;

  case 97: /* NCmpOp: KW_EQ  */
#line 145 "main.y"
              {printf(" == ");}
#line 1838 "main.tab.c"
    break;

  case 98: /* NCmpOp: KW_NE  */
#line 146 "main.y"
                {printf(" <> ");}
#line 1844 "main.tab.c"
    break;

  case 99: /* NCmpOp: KW_LT  */
#line 147 "main.y"
                {printf(" < ");}
#line 1850 "main.tab.c"
    break;

  case 100: /* NCmpOp: KW_LE  */
#line 148 "main.y"
                {printf(" <= ");}
#line 1856 "main.tab.c"
    break;

  case 101: /* NCmpOp: KW_GT  */
#line 149 "main.y"
                {printf(" > ");}
#line 1862 "main.tab.c"
    break;

  case 102: /* NCmpOp: KW_GE  */
#line 150 "main.y"
                {printf(" >= ");}
#line 1868 "main.tab.c"
    break;

  case 103: /* $@39: %empty  */
#line 153 "main.y"
              {printf("If ");}
#line 1874 "main.tab.c"
    break;

  case 104: /* $@40: %empty  */
#line 153 "main.y"
                                                          {printf(" Then");}
#line 1880 "main.tab.c"
    break;

  case 105: /* $@41: %empty  */
#line 154 "main.y"
                   {printf("\n"); tab++;}
#line 1886 "main.tab.c"
    break;

  case 106: /* $@42: %empty  */
#line 154 "main.y"
                                                    {tab--;}
#line 1892 "main.tab.c"
    break;

  case 107: /* $@43: %empty  */
#line 154 "main.y"
                                                                             {print_tabs(tab);}
#line 1898 "main.tab.c"
    break;

  case 108: /* $@44: %empty  */
#line 154 "main.y"
                                                                                                {printf("End ");}
#line 1904 "main.tab.c"
    break;

  case 109: /* NIfStm: KW_IF $@39 NExpr NCmpOp NExpr KW_THEN $@40 KW_NEWLINE $@41 NBlockStm $@42 NElseStm KW_END $@43 $@44 KW_IF  */
#line 154 "main.y"
                                                                                                                        {printf("If"); }
#line 1910 "main.tab.c"
    break;

  case 110: /* $@45: %empty  */
#line 157 "main.y"
        {print_tabs(tab);}
#line 1916 "main.tab.c"
    break;

  case 111: /* $@46: %empty  */
#line 157 "main.y"
                                   {printf("Else");}
#line 1922 "main.tab.c"
    break;

  case 112: /* $@47: %empty  */
#line 157 "main.y"
                                                                {printf("\n");tab++;}
#line 1928 "main.tab.c"
    break;

  case 113: /* NElseStm: $@45 KW_ELSE $@46 KW_NEWLINE $@47 NBlockStm  */
#line 158 "main.y"
                  {tab--;}
#line 1934 "main.tab.c"
    break;

  case 115: /* $@48: %empty  */
#line 162 "main.y"
               {printf("For ");}
#line 1940 "main.tab.c"
    break;

  case 116: /* $@49: %empty  */
#line 162 "main.y"
                                                {printf(" To ");}
#line 1946 "main.tab.c"
    break;

  case 117: /* $@50: %empty  */
#line 163 "main.y"
                   {printf("\n"); tab++;}
#line 1952 "main.tab.c"
    break;

  case 118: /* $@51: %empty  */
#line 163 "main.y"
                                                            { tab--;print_tabs(tab);}
#line 1958 "main.tab.c"
    break;

  case 119: /* $@52: %empty  */
#line 163 "main.y"
                                                                                      {printf("Next ");}
#line 1964 "main.tab.c"
    break;

  case 121: /* $@53: %empty  */
#line 166 "main.y"
              {printf("Do ");}
#line 1970 "main.tab.c"
    break;

  case 122: /* $@54: %empty  */
#line 166 "main.y"
                                        {printf("While ");}
#line 1976 "main.tab.c"
    break;

  case 123: /* $@55: %empty  */
#line 167 "main.y"
                   {printf("\n"); tab++;}
#line 1982 "main.tab.c"
    break;

  case 124: /* $@56: %empty  */
#line 168 "main.y"
                  { tab--;print_tabs(tab);}
#line 1988 "main.tab.c"
    break;

  case 125: /* NDoWhileStm: KW_DO $@53 KW_WHILE $@54 NExpr NCmpOp NExpr KW_NEWLINE $@55 NBlockStm $@56 KW_LOOP  */
#line 168 "main.y"
                                                    {printf("Loop");}
#line 1994 "main.tab.c"
    break;

  case 126: /* $@57: %empty  */
#line 171 "main.y"
              {printf("Do ");}
#line 2000 "main.tab.c"
    break;

  case 127: /* $@58: %empty  */
#line 171 "main.y"
                                        {printf("Until ");}
#line 2006 "main.tab.c"
    break;

  case 128: /* $@59: %empty  */
#line 172 "main.y"
                   {printf("\n"); tab++;}
#line 2012 "main.tab.c"
    break;

  case 129: /* $@60: %empty  */
#line 173 "main.y"
                  { tab--;print_tabs(tab);}
#line 2018 "main.tab.c"
    break;

  case 130: /* NDoUntilStm: KW_DO $@57 KW_UNTIL $@58 NExpr NCmpOp NExpr KW_NEWLINE $@59 NBlockStm $@60 KW_LOOP  */
#line 173 "main.y"
                                                    {printf("Loop");}
#line 2024 "main.tab.c"
    break;

  case 131: /* $@61: %empty  */
#line 176 "main.y"
              {printf("Do ");}
#line 2030 "main.tab.c"
    break;

  case 132: /* $@62: %empty  */
#line 176 "main.y"
                                          {printf("\n"); tab++;}
#line 2036 "main.tab.c"
    break;

  case 134: /* $@63: %empty  */
#line 180 "main.y"
                {print_tabs(tab);tab--;}
#line 2042 "main.tab.c"
    break;

  case 135: /* $@64: %empty  */
#line 180 "main.y"
                                         {printf("Loop");}
#line 2048 "main.tab.c"
    break;

  case 136: /* $@65: %empty  */
#line 180 "main.y"
                                                                    {printf("While ");}
#line 2054 "main.tab.c"
    break;

  case 138: /* $@66: %empty  */
#line 182 "main.y"
                  {tab--; print_tabs(tab);}
#line 2060 "main.tab.c"
    break;

  case 139: /* $@67: %empty  */
#line 182 "main.y"
                                            {printf("Loop");}
#line 2066 "main.tab.c"
    break;

  case 140: /* $@68: %empty  */
#line 182 "main.y"
                                                                       {printf("Until ");}
#line 2072 "main.tab.c"
    break;

  case 142: /* $@69: %empty  */
#line 184 "main.y"
                  {tab--; print_tabs(tab);}
#line 2078 "main.tab.c"
    break;

  case 143: /* NDoLoopTailStm: KW_LOOP $@69  */
#line 184 "main.y"
                                            {printf("Loop"); }
#line 2084 "main.tab.c"
    break;


#line 2088 "main.tab.c"

      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", YY_CAST (yysymbol_kind_t, yyr1[yyn]), &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;

  *++yyvsp = yyval;
  *++yylsp = yyloc;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int yylhs = yyr1[yyn] - YYNTOKENS;
    const int yyi = yypgoto[yylhs] + *yyssp;
    yystate = (0 <= yyi && yyi <= YYLAST && yycheck[yyi] == *yyssp
               ? yytable[yyi]
               : yydefgoto[yylhs]);
  }

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYSYMBOL_YYEMPTY : YYTRANSLATE (yychar);
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
      yyerror (&yylloc, scanner, env, tab, YY_("syntax error"));
    }

  yyerror_range[1] = yylloc;
  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval, &yylloc, scanner, env, tab);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label yyerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;
  ++yynerrs;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  /* Pop stack until we find a state that shifts the error token.  */
  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYSYMBOL_YYerror;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYSYMBOL_YYerror)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;

      yyerror_range[1] = *yylsp;
      yydestruct ("Error: popping",
                  YY_ACCESSING_SYMBOL (yystate), yyvsp, yylsp, scanner, env, tab);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  yyerror_range[2] = yylloc;
  ++yylsp;
  YYLLOC_DEFAULT (*yylsp, yyerror_range, 2);

  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", YY_ACCESSING_SYMBOL (yyn), yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturnlab;


/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturnlab;


/*-----------------------------------------------------------.
| yyexhaustedlab -- YYNOMEM (memory exhaustion) comes here.  |
`-----------------------------------------------------------*/
yyexhaustedlab:
  yyerror (&yylloc, scanner, env, tab, YY_("memory exhausted"));
  yyresult = 2;
  goto yyreturnlab;


/*----------------------------------------------------------.
| yyreturnlab -- parsing is finished, clean up and return.  |
`----------------------------------------------------------*/
yyreturnlab:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval, &yylloc, scanner, env, tab);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  YY_ACCESSING_SYMBOL (+*yyssp), yyvsp, yylsp, scanner, env, tab);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif

  return yyresult;
}

#line 188 "main.y"




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

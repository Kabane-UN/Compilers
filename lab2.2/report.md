% Лабораторная работа № 2.2 «Абстрактные синтаксические деревья»
% 1 апреля 2024 г.
% Андрей Кабанов, ИУ9-62Б

# Цель работы

Целью данной работы является получение навыков составления грамматик и проектирования
 синтаксических деревьев.

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
    res&(i%) = res&(i% - 1) + res&(i% - 2)
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

## Абстрактный синтаксис

```
Program --> OuterBlockStm
OuterBlockStm --> (FuncDecl | Stm | SubDecl )*
FuncDecl --> Var Params BlockStm 
Params --> (Apply | Var )*
Var --> str[name] Type
Type --> "%" | "&" | "!" | "#" | "$"
Apply --> Var ApplyArgs
ApplyArgs --> (Expr)*
SubDecl --> str[name] Params BlockStm
BlockStm --> (Stm)*
Stm --> VarDecl | ArrSet | ArrDecl | IfStm | ForStm | DoWhileStm | DoUntilStm | DoLoopStm
VarDecl --> Var Expr
ArrSet --> (Apply | Idexes) Expr
ArrDecl --> Apply
Idexes --> Var int
Expr --> BinExpr | VarExpr | ConstExpr | ApplyExpr | IdexesExpr
BinExpr --> Expr str[operator] Expr
VarExpr --> Var
ApplyExpr --> Apply
IdexesExpr --> Idexes
ConstExpr --> Any[anything] Type
IfStm --> Expr str[operator] Expr BlockStm
IfElseStm --> Expr str[operator] Expr BlockStm BlockStm
ForStm --> VarDecl Expr BlockStm Var
DoWhileStm --> Expr str[operator] Expr BlockStm
DoUntilStm --> Expr str[operator] Expr BlockStm
DoLoopWStm --> BlockStm Expr str[operator] Expr
DoLoopUStm --> BlockStm Expr str[operator] Expr
DoLoopStm --> BlockStm
```

## Лексическая структура и конкретный синтаксис

```
NProgram :== NOuterBlockStm
NOuterBlockStm :== NSubDecl KW_NEWLINE  NOuterBlockStm
        | NFuncDef KW_NEWLINE  NOuterBlockStm
        | NStm  KW_NEWLINE NOuterBlockStm
        | KW_NEWLINE  NOuterBlockStm
        | KW_NEWLINE NOuterBlockStm
        | NSubDecl
        | NStm
        | NFuncDef
        | eps
NFuncDef :== KW_FUNC NVar KW_LEFT_PAREN NParams  
        KW_RIGHT_PAREN  KW_NEWLINE  NBlockStm
        KW_END  KW_FUNC
NSubDecl:==
        KW_SUB  IDENT  KW_LEFT_PAREN  NParams  
        KW_RIGHT_PAREN  KW_NEWLINE  NBlockStm
        KW_END  KW_SUB
NStm:==
        NVarDecl
        | NArrSet
        | NArrDecl
        | NIfStm
        | NForStm
        | NDoWhileStm
        | NDoUntilStm
        | NDoLoopStm

NParams:==
        NVar KW_COMMA  NParams
        | NApply KW_COMMA  NParams
        | NVar
        | NApply
        | epsNVar:==
        IDENT  NVarType

NVarType:==
        KW_INT
        | KW_LONG
        | KW_FLOAT
        | KW_DOUBLE
        | KW_STRING

NBlockStm:==
         NStm KW_NEWLINE  NBlockStm
        | KW_NEWLINE  NBlockStm
        | eps
NVarDecl:==
        NVar KW_ASSIGN  NExpr

NArrSet:==
        NApply KW_ASSIGN  NExpr

NArrSet:==
        NIndxes KW_ASSIGN  NExpr

NArrDecl:==
        KW_DIM  NApply

NApply:==
        NVar KW_LEFT_PAREN  NApplyArgs KW_RIGHT_PAREN

NApplyArgs:==
        NExpr KW_COMMA  NApplyArgs
        | NExpr
        | eps
NExpr:==
        NTerm
        | NExpr KW_ADD  NTerm
        | NExpr KW_SUBB  NTerm

NTerm:==
        NPower
        | NTerm KW_MUL  NPower
        | NTerm KW_DIV  NPower

NPower:==
        NApply
        | NVar
        | NUMBER
        | STRING
        | NIndxes
        | KW_LEFT_PAREN  NExpr KW_RIGHT_PAREN

NIndxes:==
        NVar KW_LEFT_RECT  NUMBER  KW_RIGHT_RECT
        | NVar KW_LEFT_RECT  STRING  KW_RIGHT_RECT

NCmpOp:==
        KW_EQ
        | KW_NE
        | KW_LT
        | KW_LE
        | KW_GT
        | KW_GE

NIfStm:==
        KW_IF  NExpr NCmpOp NExpr KW_THEN  
        KW_NEWLINE  NBlockStm  
        KW_ELSE  KW_NEWLINE
        NBlockStm  KW_END   KW_IF
        |  KW_IF  NExpr NCmpOp NExpr KW_THEN  
        KW_NEWLINE  NBlockStm  KW_END   KW_IF
NForStm:==
        KW_FOR  NVarDecl KW_TO  NExpr
        KW_NEWLINE  NBlockStm KW_NEXT   NVar

NDoWhileStm:==
        KW_DO  KW_WHILE  NExpr NCmpOp NExpr
        KW_NEWLINE
        NBlockStm  KW_LOOP

NDoUntilStm:==
        KW_DO  KW_UNTIL  NExpr NCmpOp NExpr
        KW_NEWLINE
        NBlockStm  KW_LOOP

NDoLoopWStm:==
        KW_DO  KW_NEWLINE   NBlockStm
        KW_LOOP   KW_WHILE
        NExpr  NCmpOp  NExpr
NDoLoopUStm:==
        KW_DO  KW_NEWLINE   NBlockStm
        KW_LOOP   KW_UNTIL
        NExpr  NCmpOp  NExpr

NDoLoopStm:==
        KW_DO  KW_NEWLINE   NBlockStm
        KW_LOOP
```

```
[0-9]+ --> NUMBER
[A-Za-z][A-Za-z0-9]*--> IDENT
\".*\" --> STRING
```

## Программная реализация

```python
import parser_edsl as pe
from dataclasses import dataclass
from pprint import pprint
import enum
import abc
import re
import typing


class Type(enum.Enum):
    Integer = "%"
    Long = "&"
    Float = "!"
    Double = "#"
    String = "$"


@dataclass
class Var:
    name: str
    type: Type


@dataclass
class Expr(abc.ABC):
    pass


@dataclass
class VarDecl:
    var: Var
    expr: Expr


@dataclass
class ApplyArgs:
    items: list[Expr]


@dataclass
class Apply:
    var: Var
    apply_params: ApplyArgs


@dataclass
class Idexes:
    var: Var
    value: int


@dataclass
class ArrSet:
    apply: Apply | Idexes
    expr: Expr


@dataclass
class Params:
    items: list[Apply | Var]


@dataclass
class ArrayDecl:
    apply: Apply


@dataclass
class BinExpr(Expr):
    left: Expr
    op: str
    right: Expr


@dataclass
class VarExpr(Expr, Var):
    pass


@dataclass
class ConstExpr(Expr):
    value: typing.Any
    type: Type


@dataclass
class ApplyExpr(Expr, Apply):
    pass


@dataclass
class IdexesExpr(Expr, Idexes):
    pass


@dataclass
class Stm(abc.ABC):
    pass


@dataclass
class BlockStm:
    pass


@dataclass
class IfStm(Stm):
    left: Expr
    op: str
    right: Expr
    body: BlockStm


@dataclass
class IfElseStm(Stm):
    left: Expr
    op: str
    right: Expr
    body: BlockStm
    else_body: BlockStm


@dataclass
class ForStm:
    var_decl: VarDecl
    to: Expr
    body: BlockStm
    next_var: Var


@dataclass
class DoWhileStm:
    left: Expr
    op: str
    right: Expr
    body: BlockStm


@dataclass
class DoUntilStm:
    left: Expr
    op: str
    right: Expr
    body: BlockStm


@dataclass
class DoLoopWStm:
    body: BlockStm
    left: Expr
    op: str
    right: Expr


@dataclass
class DoLoopUStm:
    body: BlockStm
    left: Expr
    op: str
    right: Expr


@dataclass
class DoLoopStm:
    body: BlockStm


@dataclass
class BlockStm:
    stms: list[Stm]


@dataclass
class FuncDecl:
    var: Var
    params: Params
    body: BlockStm


@dataclass
class SubDecl:
    name: str
    params: Params
    body: BlockStm


@dataclass
class OuterBlockStm:
    outer_stms: list[FuncDecl | Stm | SubDecl]


@dataclass
class Program:
    outer_block_stm: OuterBlockStm


INTEGER = pe.Terminal("INTEGER", "[0-9]+", int, priority=7)
STRING = pe.Terminal("STRING", '".*"', eval, priority=7)
VARNAME = pe.Terminal("VARNAME", "[A-Za-z][A-Za-z0-9]*", str.upper)


def make_keyword(image):
    return pe.Terminal(
        image, image, lambda _: None, re_flags=re.IGNORECASE, priority=10
    )


(
    KW_FUNC,
    KW_END,
    KW_FOR,
    KW_NEXT,
    KW_THEN,
    KW_ELSE,
    KW_DO,
    KW_WHILE,
    KW_UNTIL,
    KW_LOOP,
    KW_DIM,
    KW_TO,
    KW_IF,
    KW_SUB,
) = map(
    make_keyword,
    "function end for next then else do while until loop dim to if sub".split(),
)
(
    NProgram,
    NOuterBlockStm,
    NFuncDef,
    NBlockStm,
    NVar,
    NParams,
    NType,
    NVarDecl,
    NArrDecl,
    NApply,
    NStm,
    NConst,
    NExpr,
    NAddOp,
    NTerm,
    NMulOp,
    NPower,
    NCmpOp,
    NIndxes,
    NIfStm,
    NIFElseStm,
    NForStm,
    NDoWhileStm,
    NDoUntilStm,
    NDoLoopWStm,
    NDoLoopUStm,
    NDoLoopStm,
    NArrSet,
    NApplyArgs,
    NSubDecl,
) = map(
    pe.NonTerminal,
    "Program OuterBlockStm FuncDef BlockStm Var Params Type VarDecl ArrDecl \
Apply Stm Const Expr AddOp Term MulOp Power CmpOp Indxes IfStm IFElseStm \
ForStm DoWhileStm DoUntilStm DoLoopWStm DoLoopUStm DoLoopStm ArrSer ApplyArgs SubDecl".split(),
)
NProgram |= NOuterBlockStm, Program
NVar |= VARNAME, NType, Var
NType |= "%", lambda: Type.Integer
NType |= "!", lambda: Type.Long
NType |= "&", lambda: Type.Float
NType |= "#", lambda: Type.Double
NType |= "$", lambda: Type.String
NOuterBlockStm |= (
    NFuncDef,
    "\n",
    NOuterBlockStm,
    lambda x, y: OuterBlockStm([x] + y.outer_stms),
)
NOuterBlockStm |= (
    NSubDecl,
    "\n",
    NOuterBlockStm,
    lambda x, y: OuterBlockStm([x] + y.outer_stms),
)
NOuterBlockStm |= (
    NStm,
    "\n",
    NOuterBlockStm,
    lambda x, y: OuterBlockStm([x] + y.outer_stms),
)
NOuterBlockStm |= "\n", NOuterBlockStm, lambda x: OuterBlockStm(x.outer_stms)
NOuterBlockStm |= NFuncDef, lambda x: OuterBlockStm([x])
NOuterBlockStm |= NSubDecl, lambda x: OuterBlockStm([x])
NOuterBlockStm |= NStm, lambda x: OuterBlockStm([x])
NOuterBlockStm |= lambda: OuterBlockStm([])
NFuncDef |= KW_FUNC, NVar, "(", NParams, ")", "\n", NBlockStm, KW_END, KW_FUNC, FuncDecl
NSubDecl |= KW_SUB, VARNAME, "(", NParams, ")", "\n", NBlockStm, KW_END, KW_SUB, SubDecl
NBlockStm |= NStm, "\n", NBlockStm, lambda x, y: BlockStm([x] + y.stms)
NBlockStm |= "\n", NBlockStm, lambda x: BlockStm(x.stms)
NBlockStm |= NStm, lambda x: BlockStm([x])
NBlockStm |= lambda: BlockStm([])
NParams |= NVar, ",", NParams, lambda x, y: Params([x] + y.items)
NParams |= NApply, ",", NParams, lambda x, y: Params([x] + y.items)
NParams |= NVar, lambda x: Params([x])
NParams |= NApply, lambda x: Params([x])
NParams |= lambda: Params([])
NVarDecl |= NVar, "=", NExpr, VarDecl
NArrSet |= NApply, "=", NExpr, ArrSet
NArrSet |= NIndxes, "=", NExpr, ArrSet
NArrDecl |= KW_DIM, NApply, ArrayDecl
NApply |= NVar, "(", NApplyArgs, ")", Apply
NApplyArgs |= NExpr, ",", NApplyArgs, lambda x, y: ApplyArgs([x] + y.items)
NApplyArgs |= NExpr, lambda x: ApplyArgs([x])
NApplyArgs |= lambda: ApplyArgs([])
NStm |= NVarDecl
NStm |= NArrSet
NStm |= NArrDecl
NStm |= NIfStm
NStm |= NIFElseStm
NStm |= NForStm
NStm |= NDoWhileStm
NStm |= NDoUntilStm
NStm |= NDoLoopWStm
NStm |= NDoLoopUStm
NStm |= NDoLoopStm
NConst |= INTEGER
NConst |= STRING
NExpr |= NTerm
NExpr |= NExpr, NAddOp, NTerm, BinExpr
NAddOp |= "+", lambda: "+"
NAddOp |= "-", lambda: "-"
NTerm |= NPower
NTerm |= NTerm, NMulOp, NPower, BinExpr
NMulOp |= "*", lambda: "*"
NMulOp |= "/", lambda: "/"
NPower |= NApply, lambda x: ApplyExpr(x.var, x.apply_params)
NPower |= NVar, lambda x: VarExpr(x.name, x.type)
NPower |= NConst, lambda x: ConstExpr(x, type(x))
NPower |= NIndxes, lambda x: IdexesExpr(x.var, x.value)
NPower |= "(", NExpr, ")"
NCmpOp |= "<", lambda: "<"
NCmpOp |= "<=", lambda: "<="
NCmpOp |= ">", lambda: ">"
NCmpOp |= ">=", lambda: ">="
NCmpOp |= "==", lambda: "=="
NCmpOp |= "<>", lambda: "<>"
NIndxes |= NVar, "[", NConst, "]", Idexes
NIfStm |= KW_IF, NExpr, NCmpOp, NExpr, KW_THEN, "\n", NBlockStm, KW_END, KW_IF, IfStm
NIFElseStm |= (
    KW_IF,
    NExpr,
    NCmpOp,
    NExpr,
    KW_THEN,
    "\n",
    NBlockStm,
    KW_ELSE,
    "\n",
    NBlockStm,
    KW_END,
    KW_IF,
    IfElseStm,
)
NForStm |= KW_FOR, NVarDecl, KW_TO, NExpr, "\n", NBlockStm, KW_NEXT, NVar, ForStm
NDoWhileStm |= (
    KW_DO,
    KW_WHILE,
    NExpr,
    NCmpOp,
    NExpr,
    "\n",
    NBlockStm,
    KW_LOOP,
    DoWhileStm,
)
NDoUntilStm |= (
    KW_DO,
    KW_UNTIL,
    NExpr,
    NCmpOp,
    NExpr,
    "\n",
    NBlockStm,
    KW_LOOP,
    DoUntilStm,
)
NDoLoopWStm |= (
    KW_DO,
    "\n",
    NBlockStm,
    KW_LOOP,
    KW_WHILE,
    NExpr,
    NCmpOp,
    NExpr,
    DoLoopWStm,
)
NDoLoopUStm |= (
    KW_DO,
    "\n",
    NBlockStm,
    KW_LOOP,
    KW_UNTIL,
    NExpr,
    NCmpOp,
    NExpr,
    DoLoopWStm,
)
NDoLoopStm |= KW_DO, "\n", NBlockStm, KW_LOOP, DoLoopStm
p = pe.Parser(NProgram)
print(p.is_lalr_one())
p.add_skipped_domain("\s")
p.add_skipped_domain("'.*\n")
try:
    with open("test.txt") as f:
        tree = p.parse(f.read())
        pprint(tree)
except pe.Error as e:
    print(f"Ошибка {e.pos}: {e.message}")
except Exception as e:
    print(e)

```

# Тестирование

## Входные данные

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

## Вывод на `stdout`

<!-- ENABLE LONG LINES -->

```
Program(outer_block_stm=OuterBlockStm(outer_stms=[FuncDecl(var=Var(name='SUMARRAY',
                                                                   type=<Type.Double: '#'>),
                                                           params=Params(items=[Apply(var=Var(name='VALUES',
                                                                                              type=<Type.Double: '#'>),
                                                                                      apply_params=ApplyArgs(items=[]))]),
                                                           body=BlockStm(stms=[VarDecl(var=Var(name='SUMARRAY',
                                                                                               type=<Type.Double: '#'>),
                                                                                       expr=ConstExpr(value=0,
                                                                                                      type=<class 'int'>)),
                                                                               ForStm(var_decl=VarDecl(var=Var(name='I',
                                                                                                               type=<Type.Integer: '%'>),
                                                                                                       expr=ConstExpr(value=1,
                                                                                                                      type=<class 'int'>)),
                                                                                      to=ApplyExpr(var=Var(name='LEN',
                                                                                                           type=<Type.Integer: '%'>),
                                                                                                   apply_params=ApplyArgs(items=[VarExpr(name='VALUES',
                                                                                                                                         type=<Type.Double: '#'>)])),
                                                                                      body=BlockStm(stms=[VarDecl(var=Var(name='SUMARRAY',
                                                                                                                          type=<Type.Double: '#'>),
                                                                                                                  expr=BinExpr(left=VarExpr(name='SUMARRAY',
                                                                                                                                            type=<Type.Double: '#'>),
                                                                                                                               op='+',
                                                                                                                               right=ApplyExpr(var=Var(name='VALUES',
                                                                                                                                                       type=<Type.Double: '#'>),
                                                                                                                                               apply_params=ApplyArgs(items=[VarExpr(name='I',
                                                                                                                                                                                     type=<Type.Integer: '%'>)]))))]),
                                                                                      next_var=Var(name='I',
                                                                                                   type=<Type.Integer: '%'>))])),
                                                  FuncDecl(var=Var(name='POLYNOM',
                                                                   type=<Type.Long: '&'>),
                                                           params=Params(items=[Var(name='X',
                                                                                    type=<Type.Long: '&'>),
                                                                                Apply(var=Var(name='COEFS',
                                                                                              type=<Type.Long: '&'>),
                                                                                      apply_params=ApplyArgs(items=[]))]),
                                                           body=BlockStm(stms=[VarDecl(var=Var(name='POLYNOM',
                                                                                               type=<Type.Long: '&'>),
                                                                                       expr=ConstExpr(value=0,
                                                                                                      type=<class 'int'>)),
                                                                               ForStm(var_decl=VarDecl(var=Var(name='I',
                                                                                                               type=<Type.Integer: '%'>),
                                                                                                       expr=ConstExpr(value=1,
                                                                                                                      type=<class 'int'>)),
                                                                                      to=ApplyExpr(var=Var(name='LEN',
                                                                                                           type=<Type.Integer: '%'>),
                                                                                                   apply_params=ApplyArgs(items=[VarExpr(name='COEFS',
                                                                                                                                         type=<Type.Long: '&'>)])),
                                                                                      body=BlockStm(stms=[VarDecl(var=Var(name='POLYNOM',
                                                                                                                          type=<Type.Long: '&'>),
                                                                                                                  expr=BinExpr(left=BinExpr(left=VarExpr(name='POLYNOM',
                                                                                                                                                         type=<Type.Long: '&'>),
                                                                                                                                            op='*',
                                                                                                                                            right=VarExpr(name='X',
                                                                                                                                                          type=<Type.Long: '&'>)),
                                                                                                                               op='+',
                                                                                                                               right=ApplyExpr(var=Var(name='COEFS',
                                                                                                                                                       type=<Type.Long: '&'>),
                                                                                                                                               apply_params=ApplyArgs(items=[VarExpr(name='I',
                                                                                                                                                                                     type=<Type.Integer: '%'>)]))))]),
                                                                                      next_var=Var(name='I',
                                                                                                   type=<Type.Integer: '%'>))])),
                                                  FuncDecl(var=Var(name='POLYNOM1111',
                                                                   type=<Type.Long: '&'>),
                                                           params=Params(items=[Var(name='X',
                                                                                    type=<Type.Long: '&'>)]),
                                                           body=BlockStm(stms=[ArrayDecl(apply=Apply(var=Var(name='COEFS',
                                                                                                             type=<Type.Long: '&'>),
                                                                                                     apply_params=ApplyArgs(items=[ConstExpr(value=4,
                                                                                                                                             type=<class 'int'>)]))),
                                                                               ForStm(var_decl=VarDecl(var=Var(name='I',
                                                                                                               type=<Type.Integer: '%'>),
                                                                                                       expr=ConstExpr(value=1,
                                                                                                                      type=<class 'int'>)),
                                                                                      to=ConstExpr(value=4,
                                                                                                   type=<class 'int'>),
                                                                                      body=BlockStm(stms=[ArrSet(apply=Apply(var=Var(name='COEFS',
                                                                                                                                     type=<Type.Long: '&'>),
                                                                                                                             apply_params=ApplyArgs(items=[VarExpr(name='I',
                                                                                                                                                                   type=<Type.Integer: '%'>)])),
                                                                                                                 expr=ConstExpr(value=1,
                                                                                                                                type=<class 'int'>))]),
                                                                                      next_var=Var(name='I',
                                                                                                   type=<Type.Integer: '%'>)),
                                                                               VarDecl(var=Var(name='POLYNOM1111',
                                                                                               type=<Type.Long: '&'>),
                                                                                       expr=ApplyExpr(var=Var(name='POLYNOM',
                                                                                                              type=<Type.Long: '&'>),
                                                                                                      apply_params=ApplyArgs(items=[VarExpr(name='X',
                                                                                                                                            type=<Type.Long: '&'>),
                                                                                                                                    VarExpr(name='COEFS',
                                                                                                                                            type=<Type.Long: '&'>)])))])),
                                                  SubDecl(name='FIBONACCI',
                                                          params=Params(items=[Apply(var=Var(name='RES',
                                                                                             type=<Type.Float: '!'>),
                                                                                     apply_params=ApplyArgs(items=[]))]),
                                                          body=BlockStm(stms=[VarDecl(var=Var(name='N',
                                                                                              type=<Type.Integer: '%'>),
                                                                                      expr=ApplyExpr(var=Var(name='LEN',
                                                                                                             type=<Type.Integer: '%'>),
                                                                                                     apply_params=ApplyArgs(items=[VarExpr(name='RES',
                                                                                                                                           type=<Type.Float: '!'>)]))),
                                                                              IfStm(left=VarExpr(name='N',
                                                                                                 type=<Type.Integer: '%'>),
                                                                                    op='>=',
                                                                                    right=ConstExpr(value=1,
                                                                                                    type=<class 'int'>),
                                                                                    body=BlockStm(stms=[ArrSet(apply=Apply(var=Var(name='RES',
                                                                                                                                   type=<Type.Float: '!'>),
                                                                                                                           apply_params=ApplyArgs(items=[ConstExpr(value=1,
                                                                                                                                                                   type=<class 'int'>)])),
                                                                                                               expr=ConstExpr(value=1,
                                                                                                                              type=<class 'int'>))])),
                                                                              IfStm(left=VarExpr(name='N',
                                                                                                 type=<Type.Integer: '%'>),
                                                                                    op='>=',
                                                                                    right=ConstExpr(value=2,
                                                                                                    type=<class 'int'>),
                                                                                    body=BlockStm(stms=[ArrSet(apply=Apply(var=Var(name='RES',
                                                                                                                                   type=<Type.Float: '!'>),
                                                                                                                           apply_params=ApplyArgs(items=[ConstExpr(value=2,
                                                                                                                                                                   type=<class 'int'>)])),
                                                                                                               expr=ConstExpr(value=1,
                                                                                                                              type=<class 'int'>))])),
                                                                              VarDecl(var=Var(name='I',
                                                                                              type=<Type.Integer: '%'>),
                                                                                      expr=ConstExpr(value=3,
                                                                                                     type=<class 'int'>)),
                                                                              DoWhileStm(left=VarExpr(name='I',
                                                                                                      type=<Type.Integer: '%'>),
                                                                                         op='<=',
                                                                                         right=VarExpr(name='N',
                                                                                                       type=<Type.Integer: '%'>),
                                                                                         body=BlockStm(stms=[ArrSet(apply=Apply(var=Var(name='RES',
                                                                                                                                        type=<Type.Float: '!'>),
                                                                                                                                apply_params=ApplyArgs(items=[VarExpr(name='I',
                                                                                                                                                                      type=<Type.Integer: '%'>)])),
                                                                                                                    expr=BinExpr(left=ApplyExpr(var=Var(name='RES',
                                                                                                                                                        type=<Type.Float: '!'>),
                                                                                                                                                apply_params=ApplyArgs(items=[BinExpr(left=VarExpr(name='I',
                                                                                                                                                                                                   type=<Type.Integer: '%'>),
                                                                                                                                                                                      op='-',
                                                                                                                                                                                      right=ConstExpr(value=1,
                                                                                                                                                                                                      type=<class 'int'>))])),
                                                                                                                                 op='+',
                                                                                                                                 right=ApplyExpr(var=Var(name='RES',
                                                                                                                                                         type=<Type.Float: '!'>),
                                                                                                                                                 apply_params=ApplyArgs(items=[BinExpr(left=VarExpr(name='I',
                                                                                                                                                                                                    type=<Type.Integer: '%'>),
                                                                                                                                                                                       op='-',
                                                                                                                                                                                       right=ConstExpr(value=2,
                                                                                                                                                                                                       type=<class 'int'>))])))),
                                                                                                             VarDecl(var=Var(name='I',
                                                                                                                             type=<Type.Integer: '%'>),
                                                                                                                     expr=BinExpr(left=VarExpr(name='I',
                                                                                                                                               type=<Type.Integer: '%'>),
                                                                                                                                  op='+',
                                                                                                                                  right=ConstExpr(value=1,
                                                                                                                                                  type=<class 'int'>)))]))])),
                                                  FuncDecl(var=Var(name='JOIN',
                                                                   type=<Type.String: '$'>),
                                                           params=Params(items=[Var(name='SEP',
                                                                                    type=<Type.String: '$'>),
                                                                                Apply(var=Var(name='ITEMS',
                                                                                              type=<Type.String: '$'>),
                                                                                      apply_params=ApplyArgs(items=[]))]),
                                                           body=BlockStm(stms=[IfElseStm(left=ApplyExpr(var=Var(name='LEN',
                                                                                                                type=<Type.Integer: '%'>),
                                                                                                        apply_params=ApplyArgs(items=[VarExpr(name='ITEMS',
                                                                                                                                              type=<Type.String: '$'>)])),
                                                                                         op='>=',
                                                                                         right=ConstExpr(value=1,
                                                                                                         type=<class 'int'>),
                                                                                         body=BlockStm(stms=[VarDecl(var=Var(name='JOIN',
                                                                                                                             type=<Type.String: '$'>),
                                                                                                                     expr=IdexesExpr(var=Var(name='ITEMS',
                                                                                                                                             type=<Type.String: '$'>),
                                                                                                                                     value=1))]),
                                                                                         else_body=BlockStm(stms=[VarDecl(var=Var(name='JOIN',
                                                                                                                                  type=<Type.String: '$'>),
                                                                                                                          expr=ConstExpr(value='',
                                                                                                                                         type=<class 'str'>))])),
                                                                               ForStm(var_decl=VarDecl(var=Var(name='I',
                                                                                                               type=<Type.Integer: '%'>),
                                                                                                       expr=ConstExpr(value=2,
                                                                                                                      type=<class 'int'>)),
                                                                                      to=ApplyExpr(var=Var(name='LEN',
                                                                                                           type=<Type.Integer: '%'>),
                                                                                                   apply_params=ApplyArgs(items=[VarExpr(name='ITEMS',
                                                                                                                                         type=<Type.String: '$'>)])),
                                                                                      body=BlockStm(stms=[VarDecl(var=Var(name='JOIN',
                                                                                                                          type=<Type.String: '$'>),
                                                                                                                  expr=BinExpr(left=BinExpr(left=VarExpr(name='JOIN',
                                                                                                                                                         type=<Type.String: '$'>),
                                                                                                                                            op='+',
                                                                                                                                            right=VarExpr(name='SEP',
                                                                                                                                                          type=<Type.String: '$'>)),
                                                                                                                               op='+',
                                                                                                                               right=ApplyExpr(var=Var(name='ITEMS',
                                                                                                                                                       type=<Type.String: '$'>),
                                                                                                                                               apply_params=ApplyArgs(items=[VarExpr(name='I',
                                                                                                                                                                                     type=<Type.Integer: '%'>)]))))]),
                                                                                      next_var=Var(name='I',
                                                                                                   type=<Type.Integer: '%'>))]))]))
```

# Вывод

При выполнении лабораторной работы была изучена библиотека parser_edsl, также были
приобретены навыки написания синтаксического анализатора с использованием этой
библиотеки.

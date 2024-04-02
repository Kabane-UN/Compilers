import parser_edsl as pe
from dataclasses import dataclass
from pprint import pprint
import enum
import abc
import re
import typing
class Type(enum.Enum):
    Integer = '%'
    Long = '&'
    Float = '!'
    Double = '#'
    String = '$'

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
    value : int
@dataclass
class ArrSet:
    apply: Apply|Idexes
    expr: Expr
@dataclass
class Params:
    items: list[Apply|Var]

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
    value : typing.Any
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
    outer_stms: list[FuncDecl|Stm|SubDecl]
@dataclass
class Program:
    outer_block_stm: OuterBlockStm


INTEGER = pe.Terminal('INTEGER', '[0-9]+', int, priority=7)
STRING = pe.Terminal('STRING', '".*"', eval, priority=7)
VARNAME = pe.Terminal('VARNAME', '[A-Za-z][A-Za-z0-9]*', str.upper)
def make_keyword(image):
    return pe.Terminal(image, image, lambda _: None,
                       re_flags=re.IGNORECASE, priority=10)
KW_FUNC, KW_END, KW_FOR, KW_NEXT, \
    KW_THEN, KW_ELSE, KW_DO, KW_WHILE, KW_UNTIL, KW_LOOP, KW_DIM, KW_TO, KW_IF, KW_SUB= \
    map(make_keyword, 'function end for next then else do while until loop dim to if sub'.split())
NProgram, NOuterBlockStm, NFuncDef, NBlockStm, NVar, NParams, NType, NVarDecl, NArrDecl, \
NApply, NStm, NConst, NExpr, NAddOp, NTerm, NMulOp, NPower, NCmpOp, NIndxes, NIfStm, NIFElseStm, \
NForStm, NDoWhileStm, NDoUntilStm, NDoLoopWStm, NDoLoopUStm, NDoLoopStm, NArrSet, NApplyArgs, NSubDecl = \
map(pe.NonTerminal, 'Program OuterBlockStm FuncDef BlockStm Var Params Type VarDecl ArrDecl \
Apply Stm Const Expr AddOp Term MulOp Power CmpOp Indxes IfStm IFElseStm \
ForStm DoWhileStm DoUntilStm DoLoopWStm DoLoopUStm DoLoopStm ArrSer ApplyArgs SubDecl'.split())
NProgram |= NOuterBlockStm, Program
NVar |= VARNAME, NType, Var
NType |= '%', lambda: Type.Integer
NType |= '!', lambda: Type.Long
NType |= '&', lambda: Type.Float
NType |= '#', lambda: Type.Double
NType |= '$', lambda: Type.String
NOuterBlockStm |= NFuncDef, '\n', NOuterBlockStm, lambda x, y: OuterBlockStm([x]+y.outer_stms)
NOuterBlockStm |= NSubDecl, '\n', NOuterBlockStm, lambda x, y: OuterBlockStm([x]+y.outer_stms)
NOuterBlockStm |= NStm, '\n', NOuterBlockStm, lambda x, y: OuterBlockStm([x]+y.outer_stms)
NOuterBlockStm |= '\n', NOuterBlockStm, lambda x: OuterBlockStm(x.outer_stms)
NOuterBlockStm |= NFuncDef, lambda x: OuterBlockStm([x])
NOuterBlockStm |= NSubDecl, lambda x: OuterBlockStm([x])
NOuterBlockStm |= NStm, lambda x: OuterBlockStm([x])
NOuterBlockStm |= lambda: OuterBlockStm([])
NFuncDef |= KW_FUNC, NVar, '(', NParams, ')','\n', NBlockStm, KW_END, KW_FUNC, FuncDecl
NSubDecl |= KW_SUB, VARNAME,'(', NParams, ')','\n', NBlockStm, KW_END, KW_SUB, SubDecl
NBlockStm |= NStm, '\n', NBlockStm, lambda x, y: BlockStm([x]+y.stms)
NBlockStm |= '\n', NBlockStm, lambda x: BlockStm(x.stms)
NBlockStm |= NStm, lambda x: BlockStm([x])
NBlockStm |= lambda: BlockStm([]) 
NParams |= NVar, ',', NParams, lambda x, y: Params([x]+y.items)
NParams |= NApply,  ',', NParams, lambda x, y: Params([x]+y.items)
NParams |= NVar, lambda x: Params([x])
NParams |= NApply,  lambda x: Params([x])
NParams |= lambda: Params([])
NVarDecl |= NVar, '=', NExpr, VarDecl
NArrSet |= NApply, '=', NExpr, ArrSet
NArrSet |= NIndxes, '=', NExpr, ArrSet
NArrDecl |= KW_DIM, NApply, ArrayDecl
NApply |= NVar, '(', NApplyArgs ,')', Apply
NApplyArgs |= NExpr, ',', NApplyArgs, lambda x, y: ApplyArgs([x]+y.items)
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
NAddOp |= '+', lambda: '+'
NAddOp |= '-', lambda: '-'
NTerm |= NPower
NTerm |= NTerm, NMulOp, NPower, BinExpr
NMulOp |= '*', lambda: '*'
NMulOp |= '/', lambda: '/'
NPower |= NApply, lambda x: ApplyExpr(x.var, x.apply_params)
NPower |= NVar, lambda x: VarExpr(x.name, x.type)
NPower |= NConst, lambda x: ConstExpr(x, type(x))
NPower |= NIndxes, lambda x: IdexesExpr(x.var, x.value)
NPower |= '(', NExpr, ')'
NCmpOp |= '<', lambda: '<'
NCmpOp |= '<=', lambda: '<='
NCmpOp |= '>', lambda: '>'
NCmpOp |= '>=', lambda: '>='
NCmpOp |= '==', lambda: '=='
NCmpOp |= '<>', lambda: '<>'
NIndxes |= NVar, '[', NConst ,']', Idexes
NIfStm |= KW_IF, NExpr, NCmpOp, NExpr, KW_THEN,'\n', NBlockStm, KW_END, KW_IF, IfStm
NIFElseStm |= KW_IF, NExpr, NCmpOp, NExpr, KW_THEN,'\n', NBlockStm, KW_ELSE, '\n', NBlockStm , \
    KW_END, KW_IF, IfElseStm
NForStm |= KW_FOR, NVarDecl, KW_TO, NExpr,'\n', NBlockStm, KW_NEXT, NVar, ForStm
NDoWhileStm |= KW_DO, KW_WHILE, NExpr, NCmpOp, NExpr,'\n', NBlockStm, KW_LOOP, DoWhileStm
NDoUntilStm |= KW_DO, KW_UNTIL, NExpr, NCmpOp, NExpr,'\n', NBlockStm, KW_LOOP, DoUntilStm
NDoLoopWStm |= KW_DO,'\n',  NBlockStm,KW_LOOP, KW_WHILE, NExpr, NCmpOp, NExpr, DoLoopWStm
NDoLoopUStm |= KW_DO,'\n',  NBlockStm,KW_LOOP, KW_UNTIL, NExpr, NCmpOp, NExpr, DoLoopWStm
NDoLoopStm |= KW_DO,'\n',  NBlockStm,KW_LOOP, DoLoopStm
p = pe.Parser(NProgram)
print(p.is_lalr_one())
p.add_skipped_domain('\s')
p.add_skipped_domain('\'.*\n')
try:
    with open('test.txt') as f:
        tree = p.parse(f.read())
        pprint(tree)
except pe.Error as e:
    print(f'Ошибка {e.pos}: {e.message}')
except Exception as e:
    print(e)


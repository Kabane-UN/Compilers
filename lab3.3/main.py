import parser_edsl as pe
from dataclasses import dataclass
from pprint import pprint
import enum
import abc
import re
from typing import Iterable, Any


class SemanticError(pe.Error): ...


class TypeError(SemanticError):
    def __init__(self, pos, _type, true_types) -> None:
        self.pos = pos.start
        self.type = _type
        self.true_types = true_types

    @property
    def message(self):
        return f"[{self.pos}] :::: Ошибка типа, ожидалось {self.true_types}, но никак не {self.type}\n"


class NameShadowError(SemanticError):
    def __init__(self, pos, name) -> None:
        self.pos = pos.start
        self.name = name

    @property
    def message(self):
        return f"[{self.pos}] :::: Ошибка имени, имя {self.name} перекрывает другое объявление\n"


class Type(enum.Enum):
    Integer = "%"
    Long = "&"
    Float = "!"
    Double = "#"
    String = "$"
    Any = "-"


@dataclass
class Var:
    name: str
    name_coord: pe.Position
    type: Type

    @pe.ExAction
    def create(attrs: Iterable[Any], coords, res_coords):
        name, __type = attrs

        cname, _ = coords
        return Var(name, cname, __type)

    def check_type(self, names):
        return self.type


@dataclass
class Expr(abc.ABC):
    def check_type(self, names): ...


@dataclass
class Stm(abc.ABC):
    def check_type(self, names):
        pass


@dataclass
class VarDecl(Stm):
    var: Var
    expr: Expr

    def check_type(self, names):
        res = self.var.check_type(names)
        ex_res = self.expr.check_type(names)
        if res == ex_res and res == Type.String:
            return res
        elif res != ex_res and ex_res == Type.String:
            raise TypeError(self.var.name_coord, ex_res, [res])
        elif res != ex_res and ex_res == Type.String:
            raise TypeError(self.var.name_coord, res, [ex_res])
        else:
            m = count_max(res, ex_res)
            if m == ex_res and m != res:
                raise TypeError(self.var.name_coord, res, [m])
            else:
                return m


@dataclass
class ApplyArgs:
    items: list[Expr]

    def check_type(self, names):
        for i in self.items:
            i.check_type(names)


@dataclass
class Apply:
    var: Var
    apply_params: ApplyArgs

    def check_type(self, names):
        if not self.var.name in names.keys():
            return self.check_type_array(names)
        for ii, i in enumerate(self.apply_params.items):
            res = names[self.var.name][ii]
            ex_res = i.check_type(names)
            if res == ex_res and res == Type.String or res == Type.Any:
                return self.var.type
            elif res != ex_res and ex_res == Type.String:
                raise TypeError(self.var.name_coord, ex_res, [res])
            elif res != ex_res and ex_res == Type.String:
                raise TypeError(self.var.name_coord, res, [ex_res])
            else:
                m = count_max(res, ex_res)
            if m == ex_res and m != res:
                raise TypeError(self.var.name_coord, res, [m])
            else:
                return self.var.type

    def check_type_array(self, names):
        for i in self.apply_params.items:
            res = i.check_type(names)
            if not res in [Type.Integer, Type.Long]:
                raise TypeError(self.var.name_coord, res, [Type.Integer, Type.Long])
        return self.var.type


@dataclass
class Idexes:
    var: Var
    value: int

    def check_type(self, names):
        return self.var.check_type(names)


@dataclass
class ArrSet(Stm):
    apply: Apply | Idexes
    expr: Expr

    def check_type(self, names):
        if type(self.apply) == Apply:
            res = self.apply.check_type_array(names)
        else:
            res = self.apply.check_type(names)
        ex_res = self.expr.check_type(names)
        if res == ex_res and res == Type.String:
            return res
        elif res != ex_res and ex_res == Type.String:
            raise TypeError(self.apply.var.name_coord, ex_res, [res])
        elif res != ex_res and ex_res == Type.String:
            raise TypeError(self.apply.var.name_coord, res, [ex_res])
        else:
            m = count_max(res, ex_res)
            if m == ex_res and m != res:
                raise TypeError(self.apply.var.name_coord, res, [ex_res])
            else:
                return m


@dataclass
class Params:
    items: list[Apply | Var]

    def check_type(self, names):
        ret = []
        for i in self.items:
            ret.append(i.check_type(names))
        return ret


@dataclass
class ArrayDecl(Stm):
    apply: Apply

    def check_type(self, names):
        return self.apply.check_type_array(names)


def count_max(t1, t2):
    if t1 == Type.Double:
        return t1
    elif t1 == Type.Float:
        if t2 == Type.Double:
            return t2
        else:
            return t1
    elif t1 == Type.Long:
        if t2 == Type.Integer:
            return t1
        else:
            return t2
    else:
        return t2


@dataclass
class BinExpr(Expr):
    left: Expr
    op: str
    op_coord: pe.Position
    right: Expr

    @staticmethod
    def create():
        @pe.ExAction
        def action(attrs: Iterable[Any], coords, res_coord):
            __left, __op, __right = attrs
            tt, __op_coord, _ = coords
            return BinExpr(__left, __op, __op_coord, __right)

        return action

    def check_type(self, names):
        res_l = self.left.check_type(names)
        res_r = self.left.check_type(names)
        if self.op in ["+", "-", "*", "/"]:
            if res_l in [
                Type.Double,
                Type.Float,
                Type.Integer,
                Type.Long,
            ] and res_r in [Type.Double, Type.Float, Type.Integer, Type.Long]:
                return count_max(res_l, res_r)
            elif res_l == Type.String and res_r == Type.String:
                return Type.String
            else:
                raise TypeError(
                    self.op_coord,
                    [res_l, res_r],
                    [
                        [
                            [Type.Double, Type.Float, Type.Integer, Type.Long],
                            [Type.Double, Type.Float, Type.Integer, Type.Long],
                        ],
                        [Type.String, Type.String],
                    ],
                )


@dataclass
class VarExpr(Expr, Var):
    def check_type(self, names):
        return self.type


@dataclass
class ConstExpr(Expr):
    value: Any
    value_coord: pe.Position

    @pe.ExAction
    def create(attrs: Iterable[Any], coords, res_coord):
        (__value,) = attrs
        __value_coord = coords
        return ConstExpr(__value, __value_coord)

    def check_type(self, names):
        return Type.Integer if type(self.value) == int else Type.String


@dataclass
class ApplyExpr(Expr, Apply):
    def check_type(self, names):
        return Apply.check_type(self, names)


@dataclass
class IdexesExpr(Expr, Idexes):
    def check_type(self, names):
        return super(Expr, self).check_type(names)


@dataclass
class IfStm(Stm):
    left: Expr
    op: str
    right: Expr
    body: "BlockStm"

    def check_type(self, names):
        self.body.check_type(names)
        self.left.check_type(names)
        self.right.check_type(names)


@dataclass
class IfElseStm(Stm):
    left: Expr
    op: str
    right: Expr
    body: "BlockStm"
    else_body: "BlockStm"

    def check_type(self, names):
        self.body.check_type(names)
        self.else_body.check_type(names)
        self.left.check_type(names)
        self.right.check_type(names)


@dataclass
class ForStm(Stm):
    var_decl: VarDecl
    to: Expr
    body: "BlockStm"
    next_var: Var

    def check_type(self, names):
        res = self.var_decl.check_type(names)
        if res not in [Type.Integer, Type.Long]:
            raise TypeError(
                self.var_decl.var.name_coord, res, [Type.Integer, Type.Long]
            )
        res = self.to.check_type(names)
        if res not in [Type.Integer, Type.Long]:
            raise TypeError(
                self.var_decl.var.name_coord, res, [Type.Integer, Type.Long]
            )
        self.body.check_type(names)
        res = self.next_var.check_type(names)
        if res not in [Type.Integer, Type.Long]:
            raise TypeError(self.next_var.name_coord, res, [Type.Integer, Type.Long])


@dataclass
class DoWhileStm(Stm):
    left: Expr
    op: str
    right: Expr
    body: "BlockStm"

    def check_type(self, names):
        self.body.check_type(names)
        self.left.check_type(names)
        self.right.check_type(names)


@dataclass
class DoUntilStm(Stm):
    left: Expr
    op: str
    right: Expr
    body: "BlockStm"

    def check_type(self, names):
        self.body.check_type(names)
        self.left.check_type(names)
        self.right.check_type(names)


@dataclass
class DoLoopWStm(Stm):
    body: "BlockStm"
    left: Expr
    op: str
    right: Expr

    def check_type(self, names):
        self.body.check_type(names)
        self.left.check_type(names)
        self.right.check_type(names)


@dataclass
class DoLoopUStm(Stm):
    body: "BlockStm"
    left: Expr
    op: str
    right: Expr

    def check_type(self, names):
        self.body.check_type(names)
        self.left.check_type(names)
        self.right.check_type(names)


@dataclass
class DoLoopStm(Stm):
    body: "BlockStm"

    def check_type(self, names):
        self.body.check_type(names)


@dataclass
class BlockStm:
    stms: list[Stm]

    def check_type(self, names):
        expect = [Type.Integer, Type.Double, Type.Float, Type.Long, Type.String]
        for s in self.stms:
            s.check_type(names)


@dataclass
class FuncDecl:
    var: Var
    var_coord: pe.Position
    params: Params
    body: BlockStm

    @pe.ExAction
    def create(attrs: Iterable[Any], coords, res_coord):
        __var, __params, __body = attrs
        return FuncDecl(
            __var,
            __var.name_coord,
            __params,
            __body,
        )

    def check_names(self, names):
        if self.var.name in names.keys():
            raise NameShadowError(self.var_coord, self.var.name)
        else:
            names[self.var.name] = self.params.check_type(names)
            self.body.check_type(names)


@dataclass
class SubDecl:
    name: str
    name_coord: pe.Position
    params: Params
    body: BlockStm

    @pe.ExAction
    def create(attrs: Iterable[Any], coords, res_coord):
        __name, __params, __body = attrs
        __name_coord = coords[0]
        return SubDecl(
            __name,
            __name_coord,
            __params,
            __body,
        )

    def check_names(self, names):
        if self.name in names.keys():
            raise NameShadowError(self.name_coord, self.name)
        else:
            names[self.name] = self.params.check_type(names)
            self.body.check_type(names)


@dataclass
class OuterBlockStm:
    outer_stms: list[FuncDecl | Stm | SubDecl]

    def check_names(self, names):
        for s in self.outer_stms:
            if isinstance(s, Stm):
                s.check_type(names)
            else:
                s.check_names(names)


@dataclass
class Program:
    outer_block_stm: OuterBlockStm

    def check(self):
        names = {"LEN": [Type.Any]}
        self.outer_block_stm.check_names(names)


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
NVar |= VARNAME, NType, Var.create
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
NFuncDef |= (
    KW_FUNC,
    NVar,
    "(",
    NParams,
    ")",
    "\n",
    NBlockStm,
    KW_END,
    KW_FUNC,
    FuncDecl.create,
)
NSubDecl |= (
    KW_SUB,
    VARNAME,
    "(",
    NParams,
    ")",
    "\n",
    NBlockStm,
    KW_END,
    KW_SUB,
    SubDecl.create,
)
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
NConst |= (INTEGER,)
NConst |= STRING
NExpr |= NTerm
NExpr |= NExpr, NAddOp, NTerm, BinExpr.create()
NAddOp |= "+", lambda: "+"
NAddOp |= "-", lambda: "-"
NTerm |= NPower
NTerm |= NTerm, NMulOp, NPower, BinExpr.create()
NMulOp |= "*", lambda: "*"
NMulOp |= "/", lambda: "/"
NPower |= NApply, lambda x: ApplyExpr(x.var, x.apply_params)
NPower |= NVar, lambda x: VarExpr(x.name, x.name_coord, x.type)
NPower |= NConst, ConstExpr.create
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


with open("test.txt") as f:
    tree = p.parse(f.read())
    # pprint(tree)
    if tree:
        tree.check()
    print('PASS')

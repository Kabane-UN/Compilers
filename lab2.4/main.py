from typing import Generator
from dataclasses import dataclass
from typing import Any
from pprint import pprint
from abc import ABC
from enum import Enum

class Token(ABC):
    coords: 'Fragment'
    attr: str|int
class CmpToken(Token, ABC):
    pass


    
class FuncToken(Token):
    coords: 'Fragment'
    attr: str = 'function'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(FuncToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"FuncToken({self.coords!r})"
class EndToken(Token):
    coords: 'Fragment'
    attr: str = 'end'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(EndToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"EndToken({self.coords!r})"
class ForToken(Token):
    coords: 'Fragment'
    attr: str = 'for'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(ForToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"ForToken({self.coords!r})"
class NextToken(Token):
    coords: 'Fragment'
    attr: str = 'next'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(NextToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"NextToken({self.coords!r})"
class ElseToken(Token):
    coords: 'Fragment'
    attr: str = 'else'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(ElseToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"ElseToken({self.coords!r})"
class DoToken(Token):
    coords: 'Fragment'
    attr: str = 'do'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(DoToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"DoToken({self.coords!r})"
class ThenToken(Token):
    coords: 'Fragment'
    attr: str = 'then'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(ThenToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"ThenToken({self.coords!r})"
class WhileToken(Token):
    coords: 'Fragment'
    attr: str = 'while'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(WhileToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"WhileToken({self.coords!r})"

class UntilToken(Token):
    coords: 'Fragment'
    attr: str = 'until'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(UntilToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"UntilToken({self.coords!r})"

class LoopToken(Token):
    coords: 'Fragment'
    attr: str = 'loop'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(LoopToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"LoopToken({self.coords!r})"
class DimToken(Token):
    coords: 'Fragment'
    attr: str = 'dim'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(DimToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"DimToken({self.coords!r})"

class ToToken(Token):
    coords: 'Fragment'
    attr: str = 'to'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(ToToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"ToToken({self.coords!r})"

class IfToken(Token):
    coords: 'Fragment'
    attr: str = 'if'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(IfToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"IfToken({self.coords!r})"
class SubToken(Token):
    coords: 'Fragment'
    attr: str = 'sub'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(SubToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"SubToken({self.coords!r})"

class IntTypeToken(Token):
    coords: 'Fragment'
    attr: str = '%'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(IntTypeToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"IntTypeToken({self.coords!r})"
class LongTypeToken(Token):
    coords: 'Fragment'
    attr: str = '&'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(LongTypeToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"LongTypeToken({self.coords!r})"
class FloatTypeToken(Token):
    coords: 'Fragment'
    attr: str = '!'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(FloatTypeToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"FloatTypeToken({self.coords!r})"
class DoubleTypeToken(Token):
    coords: 'Fragment'
    attr: str = '#'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(DoubleTypeToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"DoubleTypeToken({self.coords!r})"
class StrTypeToken(Token):
    coords: 'Fragment'
    attr: str = '$'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(StrTypeToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"StrTypeToken({self.coords!r})"
class OpenBrToken(Token):
    coords: 'Fragment'
    attr: str = '('
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(OpenBrToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"OpenBrToken({self.coords!r})"
class CloseBrToken(Token):
    coords: 'Fragment'
    attr: str = ')'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(CloseBrToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"CloseBrToken({self.coords!r})"
class CloseRectBrToken(Token):
    coords: 'Fragment'
    attr: str = ']'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(CloseRectBrToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"CloseRectBrToken({self.coords!r})"
class OpenRectBrToken(Token):
    coords: 'Fragment'
    attr: str = '['
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(OpenRectBrToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"OpenRectBrToken({self.coords!r})"
class CommaToken(Token):
    coords: 'Fragment'
    attr: str = ','
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(CommaToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"CommaToken({self.coords!r})"
class AssignToken(Token):
    coords: 'Fragment'
    attr: str = '='
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(AssignToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"AssignToken({self.coords!r})"
class LTToken(CmpToken):
    coords: 'Fragment'
    attr: str = '<'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(LTToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"LTToken({self.coords!r})"
class LEToken(CmpToken):
    coords: 'Fragment'
    attr: str = '<='
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(LEToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"LEToken({self.coords!r})"
class GTToken(CmpToken):
    coords: 'Fragment'
    attr: str = '>'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(GTToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"GTToken({self.coords!r})"
class GEToken(CmpToken):
    coords: 'Fragment'
    attr: str = '>='
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(GEToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"GEToken({self.coords!r})"
class EQToken(CmpToken):
    coords: 'Fragment'
    attr: str = '=='
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(EQToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"EQToken({self.coords!r})"
class NEToken(CmpToken):
    coords: 'Fragment'
    attr: str = '<>'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(NEToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"NEToken({self.coords!r})"
class AddToken(Token):
    coords: 'Fragment'
    attr: str = '+'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(AddToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"AddToken({self.coords!r})"
class ResToken(Token):
    coords: 'Fragment'
    attr: str = '-'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(ResToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"ResToken({self.coords!r})"
class MulToken(Token):
    coords: 'Fragment'
    attr: str = '*'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(MulToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"MulToken({self.coords!r})"
class DivToken(Token):
    coords: 'Fragment'
    attr: str = '/'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(DivToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"DivToken({self.coords!r})"
class NewLineToken(Token):
    coords: 'Fragment'
    attr: str = '\n'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(NewLineToken: ({self.coords}), attr=\\n)"
    def __repr__(self) -> str:
        return f"NewLineToken({self.coords!r})"

class StringToken(Token):
    coords: 'Fragment'
    attr: str
    def __init__(self, coords: 'Fragment', attr:str) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(StringToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"StringToken({self.coords!r})"
class IntegerToken(Token):
    coords: 'Fragment'
    attr: int
    def __init__(self, coords: 'Fragment', attr:int) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(IntegerToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"IntegerToken({self.coords!r})"
class IdentToken(Token):
    coords: 'Fragment'
    attr: int
    def __init__(self, coords: 'Fragment', attr: int) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(IdentToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"IdentToken({self.coords!r}, {self.attr})"
    

class EOPToken(Token):
    coords: 'Fragment'
    attr: str
    def __init__(self, coords: 'Fragment', attr: str) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(EOPToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"EOPToken({self.coords!r}, {self.attr})"

class Fragment:
    opening: 'Coord'
    ending: 'Coord'
    def __init__(self, opening: 'Coord', ending: 'Coord') -> None:
        self.opening = opening
        self.ending = ending
    def __str__(self) -> str:
        return 'from' + str(self.opening) + 'to' + str(self.ending)
    def __repr__(self) -> str:
        return f"Fragment({self.opening!r}, {self.ending!r})"

class Coord:
    def __init__(self, position: 'Position') -> None:
        self.line: int = position.line 
        self.pos: int = position.pos
    def __str__(self) -> str:
        return f'(line: {self.line}, pos: {self.pos})'
    def __repr__(self) -> str:
        return f"Coord({self.line!r}, {self.pos!r})"

class Position:
    line: int
    pos: int
    index: int
    def __init__(self, text: str) -> None:
        self.line = 1
        self.pos = 1
        self.index = 0
        self.text: str = text
    def read(self):
        return '' if self.index == len(self.text) \
            else self.text[self.index].lower()
    def next(self):
        if self.index+1 < len(self.text):
            if self.text[self.index] == '\n':
                self.line+=1
                self.pos = 1
                self.index+=1
            else:
                self.pos += 1
                self.index+=1
        elif self.index+1 == len(self.text):
            self.index+=1
        else:
            raise(EOFError)
    def read_next(self):
        if self.index+1 < len(self.text):
            return self.text[self.index+1].lower()
        elif self.index+1 == len(self.text):
            return ''
        else:
            raise(EOFError)
    def __str__(self) -> str:
        return f'(line: {self.line}, pos: {self.pos})'
    


class Message:
    is_error: bool
    text: str 
    coord: Coord
    def __init__(self, is_error: bool, text: str,
                  coord: Coord) -> None:
        self.is_error = is_error
        self.text = text
        self.coord = coord
    def __str__(self) -> str:
        return ("(Error" if self.is_error \
                else "(Warning") + str(self.coord) \
        + self.text + ")"
class Comment:
    text: str 
    coord: Coord
    def __init__(self, text: str,
                  coord: Coord) -> None:
        self.text = text
        self.coord = coord
    def __str__(self) -> str:
        return "(Comment " + self.text + " )"

class Scanner: 
    program: str
    def __init__(self, compiler: 'Compiler',
                  program: str) -> None:
        self._compiler: Compiler = compiler
        self.program = program
        self._position: Position = Position(program)
    def tokens(self) -> Generator[Token, None, None]:
        panic = False
        all_key_tokens:list[type] = [FuncToken, EndToken, ForToken, NextToken, ElseToken,
                                      DoToken, ThenToken, WhileToken, UntilToken, DimToken,
                                        ToToken, IfToken, SubToken, LoopToken,
                                     IntTypeToken, LongTypeToken, FloatTypeToken,
                                       DoubleTypeToken,
                                       StrTypeToken, OpenBrToken, CloseBrToken,
                                         CloseRectBrToken,
                                         OpenRectBrToken,
                                     CommaToken,LEToken,EQToken,NEToken,GEToken, AssignToken,NEToken, LTToken, GTToken, NewLineToken, AddToken,
                                         ResToken, MulToken, DivToken]
        all_key_first:list[str] = [i.attr[0] for i in all_key_tokens]
        while self._position.read() != '':
            match self._position.read():
                case x if str.isspace(x) and x != '\n':
                    self._position.next()
                case x if x in all_key_first:
                    ttype = []
                    for i, token_first in enumerate(all_key_first):
                        if self._position.read() == token_first:
                            ttype.append(all_key_tokens[i])
                    panic = False
                    key_word = x
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    left = list(ttype[0].attr[1:]) if len( ttype[0].attr) > 1 else []
        
                    while left:
                        if self._position.read() == left[0]:
                            left.pop(0)
                            key_word += self._position.read()
                            self._position.next()
                        else:
                            ttype.pop(0)
                            if ttype and ttype[0].attr.startswith(key_word):
                                left = list(ttype[0].attr[len(key_word):])
                            elif not ttype:
                                break
                    else:
                        ending: Coord = Coord(self._position)
                        yield ttype[0](Fragment(opening, ending))
                        continue
                    if key_word[0].isalpha() and not [i for i in key_word if not (i.isalpha() or i.isdigit())]:
                        while self._position.read().isalpha() or self._position.read().isdigit():
                            key_word += self._position.read()
                            self._position.next()
                        ending: Coord = Coord(self._position)
                        code = self._compiler.names.contains(key_word)
                        if code == -1:
                            code = self._compiler.names.add_name(key_word)
                        yield IdentToken(Fragment(opening, ending), code)
                        continue

                    panic = True
                    self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "Bad Key Word")
                case x if x.isdigit():
                    panic = False
                    opening: Coord = Coord(self._position)
                    attr = self._position.read()
                    self._position.next()
                    while self._position.read().isdigit():
                        attr += self._position.read()
                        self._position.next()
                    ending: Coord = Coord(self._position)
                    yield IntegerToken(Fragment(opening, ending), int(attr))
                case '"':
                    panic = False
                    opening: Coord = Coord(self._position)
                    attr = self._position.read()
                    self._position.next()
                    while self._position.read() != '"':
                        attr += self._position.read()
                        self._position.next()
                    attr += self._position.read()
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield StringToken(Fragment(opening, ending), attr)
                case x if x.isalpha():
                    panic = False
                    opening: Coord = Coord(self._position)
                    attr = self._position.read()
                    self._position.next()
                    while self._position.read().isalpha() or self._position.read().isdigit():
                        attr += self._position.read()
                        self._position.next()
                    ending: Coord = Coord(self._position)
                    code = self._compiler.names.contains(attr)
                    if code == -1:
                        code = self._compiler.names.add_name(attr)
                    yield IdentToken(Fragment(opening, ending), code)
                case "'":
                    panic = False
                    opening: Coord = Coord(self._position)
                    attr = ''
                    self._position.next()
                    while self._position.read() != '\n':
                        attr += self._position.read()
                        self._position.next()
                    self._position.next()
                    self._compiler.comments.append(Comment(attr, opening))
                case _:
                    if panic:
                        self._position.next()
                    else:
                        panic = True
        yield EOPToken(Fragment(Coord(self._position),
                                 Coord(self._position)),
                                   "End of Program")
                
            
                    
         

class NameDictionary:
    _names: dict[int, str]
    _num: int
    def __init__(self) -> None:
        self._names = {}
        self._num = 0
    def add_name(self, s: str) -> int:
        self._names[self._num] = s 
        self._num+=1
        return self._num - 1
        
    def contains(self, s: str) -> int:
        try:
            return list(self._names.values()).index(s)
        except ValueError:
            return -1
    def __getitem__(self, code: int) -> str:
        return self._names[code]

class MessageList:
    _messages: list[Message]
    def __init__(self) -> None:
        self._messages = []
    def add_error(self, coord: Coord,
                   text: str) -> None:
        self._messages.append(Message(True,
                                       text, coord))
    def add_warning(self, coord, text: str) -> None:
        self._messages.append(Message(False, text, coord))
    def get_sorted(self):
        return sorted(self._messages, 
                      key= lambda x: x.coord.line)

class Type(Enum):
    Integer = '%'
    Long = '&'
    Float = '!'
    Double = '#'
    String = '$'

@dataclass
class Var:
    name: Token
    type: Token
    


@dataclass
class Expr(ABC):
    pass


@dataclass
class VarAction(Expr):
    var: Var 
    const: 'ConstExpr|None' 
    apply_params: 'ApplyArgs|None'




@dataclass
class ApplyArgs:
    items: list[Expr]


@dataclass
class Params:
    items: list['VarAction|Var']
@dataclass
class Stm(ABC):
    pass
@dataclass
class ArrayDecl(Stm):
    var: Var
    apply_params: ApplyArgs

@dataclass
class BinExpr(Expr):
    left: Expr
    op: AddToken|ResToken|MulToken|DivToken
    right: Expr
@dataclass
class ConstExpr(Expr):
    value : Token

@dataclass
class AssignExpr(Stm):
    var: VarAction
    expr: Expr
@dataclass
class IfStm(Stm):
    left: Expr
    op: Token 
    right: Expr
    body: 'BlockStm'
    else_body: 'BlockStm|None'
@dataclass
class ForStm(Stm):
    var_decl: AssignExpr
    to: Expr
    body: 'BlockStm'
    next_var: Var
@dataclass
class DoWhileStm(Stm):
    left: Expr
    op: Token 
    right: Expr
    body: 'BlockStm'
@dataclass
class DoUntilStm(Stm):
    left: Expr
    op: Token 
    right: Expr
    body: 'BlockStm'
@dataclass
class DoLoopWStm(Stm):
    body: 'BlockStm'
    left: Expr
    op: Token 
    right: Expr

@dataclass
class DoLoopUStm(Stm):
    body: 'BlockStm'
    left: Expr
    op: Token 
    right: Expr
@dataclass
class DoLoopStm(Stm):
    body: 'BlockStm'
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

sym:Token

def sym_check(t: type, tokens: Generator[Token, None, None]):
    global sym
    if type(sym) == t:
        old = sym
        if t != EOPToken:
            sym = next(tokens)
            return old
        else:
            return None
    else:
        raise Exception(f'Expected {t} got {type(sym)} as {sym}')
def sym_checks(ts: list[type], tokens: Generator[Token, None, None]):
    global sym
    for t in ts:
        if type(sym) == t:
            old = sym
            sym = next(tokens)
            return old
    else:
        raise Exception(f'Expected {ts} got {type(sym)} as {sym}')

# NProgram -> NOuterBlockStm
def parse_program(tokens: Generator[Token, None, None]) -> Program:
    global sym
    program = Program(parse_outer_block_stm(tokens))
    sym_check(EOPToken, tokens)
    return program

# NOuterBlockStm ->  { { NFuncDef | NSubDecl | NStm } { \n NFuncDef | NSubDecl | NStm }* \n}?
def parse_outer_block_stm(tokens: Generator[Token, None, None]) -> OuterBlockStm:
    global sym
    outer_stms: list[FuncDecl|Stm|SubDecl] = []
    if type(sym) == EOPToken:
        return OuterBlockStm(outer_stms)
    if type(sym) == FuncToken:
            outer_stms.append(parse_func_decl(tokens))
    elif type(sym) == SubToken:
            outer_stms.append(parse_sub_decl(tokens))
    elif type(sym) == IdentToken:
            outer_stms.append(parse_assign_expr(tokens))
    elif type(sym) == DimToken:
            outer_stms.append(parse_arr_decl(tokens))
    elif type(sym) == IfToken:
            outer_stms.append(parse_if_stm(tokens))
    elif type(sym) == ForToken:
            outer_stms.append(parse_for_stm(tokens))
    elif type(sym) == DoToken:
            outer_stms.append(parse_do_while_until_loop_stm(tokens))
    else:
        raise Exception
    while type(sym) == NewLineToken:
        sym = next(tokens)
        if type(sym) == FuncToken:
            outer_stms.append(parse_func_decl(tokens))
        elif type(sym) == SubToken:
            outer_stms.append(parse_sub_decl(tokens))
        elif type(sym) == IdentToken:
            outer_stms.append(parse_assign_expr(tokens))
        elif type(sym) == DimToken:
            outer_stms.append(parse_arr_decl(tokens))
        elif type(sym) == IfToken:
            outer_stms.append(parse_if_stm(tokens))
        elif type(sym) == ForToken:
            outer_stms.append(parse_for_stm(tokens))
        elif type(sym) == DoToken:
            outer_stms.append(parse_do_while_until_loop_stm(tokens))
        elif type(sym) == NewLineToken:
            pass
        else:
            return OuterBlockStm(outer_stms)
    return OuterBlockStm(outer_stms)

# NVar -> VARNAME  NType
def parse_var(tokens: Generator[Token, None, None]) -> Var:
    global sym
    ident = sym_check(IdentToken, tokens)
    typ = sym_checks([IntTypeToken, LongTypeToken, FloatTypeToken,
                                       DoubleTypeToken,
                                       StrTypeToken,], tokens)
    return Var(ident, typ)
# NFuncDef -> KW_FUNC  NVar  (  NParams  ) \n  NBlockStm  KW_END  KW_FUNC 
def parse_func_decl(tokens: Generator[Token, None, None]) -> FuncDecl:
    global sym
    sym_check(FuncToken, tokens)
    var = parse_var(tokens)
    sym_check(OpenBrToken, tokens)
    params = parse_params(tokens)
    sym_check(CloseBrToken, tokens)
    sym_check(NewLineToken, tokens)
    body = parse_block_stm(tokens)
    sym_check(EndToken, tokens)
    sym_check(FuncToken, tokens)
    return FuncDecl(var, params, body)
# NSubDecl -> KW_SUB  VARNAME (  NParams  ) \n  NBlockStm  KW_END  KW_SUB 
def parse_sub_decl(tokens: Generator[Token, None, None]) -> SubDecl:
    global sym
    sym_check(SubToken, tokens)
    var = sym_check(IdentToken, tokens)
    sym_check(OpenBrToken, tokens)
    params = parse_params(tokens)
    sym_check(CloseBrToken, tokens)
    sym_check(NewLineToken, tokens)
    body = parse_block_stm(tokens)
    sym_check(EndToken, tokens)
    sym_check(SubToken, tokens)
    return SubDecl(str(var.attr), params, body)
# NAssignExpr -> NVarAction = NExpr
def parse_assign_expr(tokens: Generator[Token, None, None]) -> AssignExpr:
    global sym
    var_action = parse_var_action(tokens)
    sym_check(AssignToken, tokens)
    expr = parse_expr(tokens)
    return AssignExpr(var_action, expr)
# NVarAction -> NVar | NVar  (  NApplyArgs  ) | NVar  [  NConst  ]
def parse_var_action(tokens: Generator[Token, None, None]) -> VarAction:
    global sym
    var = parse_var(tokens)
    if type(sym) == OpenBrToken:
        sym = next(tokens)
        apply = parse_apply_args(tokens)
        sym_check(CloseBrToken, tokens)
        return VarAction(var, None, apply)
    elif type(sym) == OpenRectBrToken:
        sym = next(tokens)
        const = parse_const(tokens)
        sym_check(CloseRectBrToken, tokens)
        return VarAction(var, const, None)
    else:
        return VarAction(var, None, None)

# NApplyArgs -> { NExpr { ,  NExpr }* }?
def parse_apply_args(tokens: Generator[Token, None, None]) -> ApplyArgs:
    global sym
    args = []
    if type(sym) == IntegerToken or type(sym) == StringToken or type(sym) == IdentToken or type(sym) == OpenBrToken:
        args.append(parse_expr(tokens))
        while type(sym) == CommaToken:
            sym = next(tokens)
            args.append(parse_expr(tokens))
    return ApplyArgs(args)

# NConst -> INTEGER | STRING
def parse_const(tokens: Generator[Token, None, None]) -> ConstExpr:
    global sym
    return ConstExpr(sym_checks([IntegerToken, StringToken], tokens))

# NParams -> { NVarAction { ,  NVarAction }* }?
def parse_params(tokens: Generator[Token, None, None]) -> Params:
    global sym
    args = []
    if type(sym) == IdentToken:
        args.append(parse_var_action(tokens))
        while type(sym) == CommaToken:
            sym = next(tokens)
            args.append(parse_var_action(tokens))
    return Params(args)

# NArrDecl -> KW_DIM  NVar  (  NApplyArgs  )
def parse_arr_decl(tokens: Generator[Token, None, None]) -> ArrayDecl:
    global sym
    sym_check(DimToken, tokens)
    var = parse_var(tokens)
    sym_check(OpenBrToken, tokens)
    args = parse_apply_args(tokens)
    sym_check(CloseBrToken, tokens)
    return ArrayDecl(var, args)

# NBlockStm ->  { NStm { \n NStm}* }?
def parse_block_stm(tokens: Generator[Token, None, None]) -> BlockStm:
    global sym
    stms: list[Stm] = []
    if type(sym) == IdentToken:
            stms.append(parse_assign_expr(tokens))
    elif type(sym) == DimToken:
            stms.append(parse_arr_decl(tokens))
    elif type(sym) == IfToken:
            stms.append(parse_if_stm(tokens))
    elif type(sym) == ForToken:
            stms.append(parse_for_stm(tokens))
    elif type(sym) == DoToken:
            stms.append(parse_do_while_until_loop_stm(tokens))
    else:
        return BlockStm(stms)
    while type(sym) == NewLineToken:
        sym = next(tokens)
        if type(sym) == IdentToken:
            stms.append(parse_assign_expr(tokens))
        elif type(sym) == DimToken:
            stms.append(parse_arr_decl(tokens))
        elif type(sym) == IfToken:
            stms.append(parse_if_stm(tokens))
        elif type(sym) == ForToken:
            stms.append(parse_for_stm(tokens))
        elif type(sym) == DoToken:
            stms.append(parse_do_while_until_loop_stm(tokens))
        elif type(sym) == NewLineToken:
            pass
        else:
            return BlockStm(stms)
    return BlockStm(stms)

# NExpr -> NTerm { NAddOp NTerm }*
def parse_expr(tokens: Generator[Token, None, None]) -> BinExpr|VarAction|ConstExpr:
    global sym
    expr1 = parse_term(tokens)
    while type(sym) == AddToken or type(sym) == ResToken:
        op_token = sym
        sym = next(tokens)
        expr2 = parse_term(tokens)
        expr1 = BinExpr(expr1, op_token, expr2)
    return expr1
# NTerm -> NFactor { NMulOp NFactor }*
def parse_term(tokens: Generator[Token, None, None]) -> BinExpr|VarAction|ConstExpr:
    global sym
    expr1 = parse_factor(tokens)
    while type(sym) == MulToken or type(sym) == DivToken:
        op_token = sym
        sym = next(tokens)
        expr2 = parse_factor(tokens)
        expr1 = BinExpr(expr1, op_token, expr2)
    return expr1
# NFactor -> NVarAction  | NConst   | (  NExpr  )
def parse_factor(tokens: Generator[Token, None, None]) -> BinExpr|VarAction|ConstExpr:
    global sym
    expr = None
    if type(sym) == IdentToken:
        expr = parse_var_action(tokens)
    elif type(sym) == IntegerToken or type(sym) == StringToken:
        expr = parse_const(tokens)
    elif type(sym) == OpenBrToken:
        sym = next(tokens)
        expr = parse_expr(tokens)
        sym_check(CloseBrToken, tokens)
    else:
        raise Exception(f'Expected {IdentToken} {StringToken} {IntegerToken} {OpenBrToken} got {type(sym)} as {sym}')
    return expr
# NCmpOp -> <  | <=  | >  | >=  | ==  | <>
def parse_cmp_op(tokens: Generator[Token, None, None]) -> Token:
    global sym
    if issubclass(type(sym), CmpToken):
        res = sym 
        sym = next(tokens)
        return res
    else:
        raise Exception
     
# NIfStm -> KW_IF  NExpr  NCmpOp  NExpr  KW_THEN \n  NBlockStm { KW_ELSE  \n  NBlockStm }? KW_END  KW_IF  
def parse_if_stm(tokens: Generator[Token, None, None]) -> IfStm:
    global sym
    sym_check(IfToken, tokens)
    left = parse_expr(tokens)
    op = parse_cmp_op(tokens)
    right = parse_expr(tokens)
    sym_check(ThenToken, tokens)
    sym_check(NewLineToken, tokens)
    body = parse_block_stm(tokens)
    else_body = None
    if type(sym) == ElseToken:
        sym = next(tokens)
        sym_check(NewLineToken, tokens)
        else_body = parse_block_stm(tokens)
    sym_check(EndToken, tokens)
    sym_check(IfToken, tokens)
    return IfStm(left, op, right, body, else_body)
# NForStm -> KW_FOR  NAssignExpr  KW_TO  NExpr \n  NBlockStm  KW_NEXT  NVar 
def parse_for_stm(tokens: Generator[Token, None, None]) -> ForStm:
    global sym
    sym_check(ForToken, tokens)
    assign = parse_assign_expr(tokens)
    sym_check(ToToken, tokens)
    expr = parse_expr(tokens)
    sym_check(NewLineToken, tokens)
    body = parse_block_stm(tokens)
    sym_check(NextToken, tokens)
    var = parse_var(tokens)
    return ForStm(assign, expr, body, var)
# NDoWhileUntilLoopStm -> KW_DO  {KW_WHILE | KW_UNTIL}  NExpr  NCmpOp  NExpr \n  NBlockStm  KW_LOOP  | KW_DO \n   NBlockStm KW_LOOP  { {KW_WHILE | KW_UNTIL}  NExpr  NCmpOp  NExpr }?
def parse_do_while_until_loop_stm(tokens: Generator[Token, None, None]) -> DoWhileStm|DoLoopStm|DoUntilStm|DoLoopWStm|DoLoopUStm:
    global sym
    sym_check(DoToken, tokens)
    if type(sym) == WhileToken or type(sym) == UntilToken:
        flag = False
        if type(sym) == UntilToken:
            flag = True
        sym = next(tokens)
        expr1 = parse_expr(tokens)
        cmp_op = parse_cmp_op(tokens)
        expr2 = parse_expr(tokens)
        sym_check(NewLineToken, tokens)
        body = parse_block_stm(tokens)
        sym_check(LoopToken, tokens)
        return DoUntilStm(expr1, cmp_op, expr2, body) if flag else DoWhileStm(expr1, cmp_op, expr2, body)
    elif type(sym) == NewLineToken:
        body = parse_block_stm(tokens)
        sym_check(LoopToken, tokens)
        if type(sym) == WhileToken or type(sym) == UntilToken:
            flag = False
            if type(sym) == UntilToken:
                flag = True
            expr1 = parse_expr(tokens)
            cmp_op = parse_cmp_op(tokens)
            expr2 = parse_expr(tokens)
            return DoLoopUStm(body, expr1, cmp_op, expr2) if flag else DoLoopWStm(body, expr1, cmp_op, expr2)
        else:
            return DoLoopStm(body)
    else:
        raise Exception



    
class Compiler:
    names: NameDictionary = NameDictionary()
    messages: MessageList = MessageList()
    comments: list[Comment]
    def __init__(self) -> None:
        self.comments = []
        pass
    def get_scanner(self, program: str) -> Scanner:
        return Scanner(self, program)

with open(r"test.txt", "r") as f:
    program = ""
    for line in f.readlines():
        if not program:
            program += line
        else:
            program += line
    compiler: Compiler = Compiler()
    scanner = compiler.get_scanner(program)
    # for token in scanner.tokens():
    #     print(token)
    tokens = scanner.tokens()
    sym = next(tokens)
    try:
        pprint(parse_program(tokens))
    except Exception as ex:
        print(ex)

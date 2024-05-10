from typing import Generator, Iterable
from dataclasses import dataclass
from typing import Any
from pprint import pprint
import gram_parser
from sys import argv
from gram2 import *
from functools import reduce


    
class AddToken(AddBaseToken):
    coords: 'Fragment'
    attr: str = '+'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(AddToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"AddToken({self.coords!r})"
class SubToken(SubBaseToken):
    coords: 'Fragment'
    attr: str = '-'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(SubToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"SubToken({self.coords!r})"
class MulToken(MulBaseToken):
    coords: 'Fragment'
    attr: str = '*'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(MulToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"MulToken({self.coords!r})"
class DivToken(DivBaseToken):
    coords: 'Fragment'
    attr: str = '/'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(DivToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"DivToken({self.coords!r})"
class RightParenToken(RightParenBaseToken):
    coords: 'Fragment'
    attr: str = ')'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(RightParenToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"RightParenToken({self.coords!r})"
class LeftParenToken(LeftParenBaseToken):
    coords: 'Fragment'
    attr: str = '('
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(LeftParenToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"LeftParenToken({self.coords!r})"
class NumToken(NumBaseToken):
    coords: 'Fragment'
    attr: int
    def __init__(self, coords: 'Fragment', attr: int) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(NumToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"NumToken({self.coords!r}, {self.attr})"
class EOPToken(EOPBaseToken):
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
            else self.text[self.index]
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
            return self.text[self.index+1]
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

class Scanner():
    program: str
    def __init__(self, compiler: 'Compiler',
                  program: str) -> None:
        self._compiler: Compiler = compiler
        self.program = program
        self._position: Position = Position(program)
    def tokens(self) -> Generator[AddToken|SubToken|MulToken|DivToken|RightParenToken|LeftParenToken|NumToken|EOPToken, None, None]:
        panic = False
        while self._position.read() != '':
            
            match self._position.read():
                case x if str.isspace(x):
                    self._position.next()
                case "+":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield AddToken(Fragment(opening, ending))
                case "-":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield SubToken(Fragment(opening, ending))
                case "*":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield MulToken(Fragment(opening, ending))

                case "/":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield DivToken(Fragment(opening, ending))
                case "(":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield LeftParenToken(Fragment(opening, ending))
                case ")":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield RightParenToken(Fragment(opening, ending))
                case x if str.isdigit(x):
                    panic = False
                    opening: Coord = Coord(self._position)
                    str_num = self._position.read()
                    self._position.next()
                    while str.isdigit(self._position.read()):
                        str_num+=self._position.read()
                        self._position.next()
                    ending: Coord = Coord(self._position)
                    yield NumToken(Fragment(opening, ending), eval(str_num))   
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
    def keys(self) -> set[int]:
        return set(self._names.keys())

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
    



class Compiler:
    names: NameDictionary = NameDictionary()
    messages: MessageList = MessageList()
    comments: list[Comment]
    def __init__(self) -> None:
        self.comments = []
        pass
    def get_scanner(self, program: str) -> Scanner:
        return Scanner(self, program)
    def parse(self, program: str):
        tree = gram_parser.parse(self.get_scanner(program), parse_table, ExprBase, EOPToken, Token)
        print(gen_expr(tree))


def gen_expr(tree):
    res = 0
    res += gen_term(tree.leafs[0])
    res += gen_add_sub_seq(tree.leafs[1])
    return res
def gen_add_sub_seq(tree):
    res = 0
    if not tree.leafs:
        return 0
    if type(tree.leafs[0]) == AddToken:
        res += gen_term(tree.leafs[1])
        res += gen_add_sub_seq(tree.leafs[2])
    else:
        res -= gen_term(tree.leafs[1])
        res += gen_add_sub_seq(tree.leafs[2])
    return res
def gen_term(tree):
    res = 1
    res *= gen_factor(tree.leafs[0])
    res *= gen_mul_div_seq(tree.leafs[1])
    return res
def gen_mul_div_seq(tree):
    res = 1
    if not tree.leafs:
        return 1
    if type(tree.leafs[0]) == MulToken:
        res *= gen_factor(tree.leafs[1])
        res *= gen_mul_div_seq(tree.leafs[2])
    else:
        res /= gen_factor(tree.leafs[1])
        res /= gen_mul_div_seq(tree.leafs[2])
    return res
def gen_factor(tree):
    if type(tree.leafs[0]) == NumToken:
        return tree.leafs[0].attr
    else:
        return gen_expr(tree.leafs[1])

with open(argv[1], "r") as f:
    program = ""
    for line in f.readlines():
        if not program:
            program += line
        else:
            program += line
    compiler: Compiler = Compiler()
    
    compiler.parse(program)
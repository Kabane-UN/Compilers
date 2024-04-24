from typing import Generator
from dataclasses import dataclass
from typing import Any
from pprint import pprint
class Token:
    pass


    
class IsToken(Token):
    coords: 'Fragment'
    attr: str = 'is'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(IsToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"IsToken({self.coords!r})"
class CommaToken(Token):
    coords: 'Fragment'
    attr: str = ','
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(CommaToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"CommaToken({self.coords!r})"
class DotToken(Token):
    coords: 'Fragment'
    attr: str = '.'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(DotToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"DotToken({self.coords!r})"
class TokensToken(Token):
    coords: 'Fragment'
    attr: str = 'tokens'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(TokensToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"TokensToken({self.coords!r})"
class StartToken(Token):
    coords: 'Fragment'
    attr: str = 'start'
    def __init__(self, coords: 'Fragment') -> None:
        self.coords = coords
    def __str__(self) -> str:
        return f"(StartToken: ({self.coords}), attr={self.attr})"
    def __repr__(self) -> str:
        return f"StartToken({self.coords!r})"
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

class Scanner:
    program: str
    def __init__(self, compiler: 'Compiler',
                  program: str) -> None:
        self._compiler: Compiler = compiler
        self.program = program
        self._position: Position = Position(program)
    def tokens(self) -> Generator[IdentToken|TokensToken|StartToken|IsToken|CommaToken|DotToken|EOPToken, None, None]:
        panic = False
        while self._position.read() != '':
            
            match self._position.read():
                case x if str.isspace(x):
                    self._position.next()
                case ".":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield DotToken(Fragment(opening, ending))
                case ",":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    ending: Coord = Coord(self._position)
                    yield CommaToken(Fragment(opening, ending))
                case "i":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    if self._position.read() == 's':
                        self._position.next()
                        ending: Coord = Coord(self._position)
                        yield IsToken(Fragment(opening, ending))
                    else:
                        panic = True
                        self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "Bad is Key Word")
                        self._position.next()
                case "t":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    left = ['o', 'k', 'e', 'n', 's']
                    while left:
                        if self._position.read() == left[0]:
                            left.pop(0)
                            self._position.next()
                        else:
                            break
                    else:
                        ending: Coord = Coord(self._position)
                        yield TokensToken(Fragment(opening, ending))
                        continue
                    panic = True
                    self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "Bad tokens Key Word")
                case "s":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    left = ['t', 'a', 'r', 't']
                    while left:
                        if self._position.read() == left[0]:
                            left.pop(0)
                            self._position.next()
                        else:
                            break
                    else:
                        ending: Coord = Coord(self._position)
                        yield StartToken(Fragment(opening, ending))
                        continue
                    panic = True
                    self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "Bad start Key Word")
                    
                case "<":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    if self._position.read() == '!':
                        text = ''
                        self._position.next()
                        if self._position.read() == '-':
                            self._position.next()
                            if self._position.read() == '-':
                                self._position.next()
                                while self._position.read() != "-":
                                    text += self._position.read()
                                    self._position.next()
                                    if self._position.read() == "\n":
                                        break
                                else:
                                    self._position.next()
                                    if self._position.read() == '-':
                                        self._position.next()
                                        if self._position.read() == '>':
                                            self._compiler.comments.append(Comment(text, opening))
                                            self._position.next()
                                            continue
                        panic = True
                        self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "Bad Comment")
                        continue
                    ident = ""
                    while str.isalpha(self._position.read()) or str.isdigit(self._position.read()) or self._position.read() == ' ':
                        ident+=self._position.read()
                        self._position.next()
                    else:
                        if self._position.read() == '>':
                            self._position.next()
                            ending: Coord = Coord(self._position)
                            code = self._compiler.names.contains(ident)
                            if code == -1:
                                code = self._compiler.names.add_name(ident)
                            yield IdentToken(Fragment(opening, ending), code)
                        else:
                            panic = True
                            self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "Bad Token Name")
                            self._position.next()      
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
    



class Compiler:
    names: NameDictionary = NameDictionary()
    messages: MessageList = MessageList()
    comments: list[Comment]
    def __init__(self) -> None:
        self.comments = []
        pass
    def get_scanner(self, program: str) -> Scanner:
        return Scanner(self, program)
@dataclass
class Grammar:
    pass 
@dataclass
class Axiom:
    pass 
@dataclass
class Rule:
    pass 
@dataclass
class IdentSeq:
    pass 
@dataclass
class TermInit:
    pass 
@dataclass
class CommaSeq:
    pass 

@dataclass
class Node:
    name: type
    leafs: list['Node|Token']



sintax: dict[Any, Any] = {
    (Grammar, StartToken): [Axiom, Grammar],
    (Axiom, StartToken): [StartToken, IdentToken, DotToken],
    (Grammar, IdentToken): [Rule, Grammar],
    (Rule, IdentToken): [IdentToken, IsToken, IdentSeq, DotToken],
    (IdentSeq, IdentToken): [IdentToken, IdentSeq],
    (IdentSeq, DotToken): [],
    (Grammar, TokensToken): [TermInit, Grammar],
    (TermInit, TokensToken): [TokensToken, IdentToken, CommaSeq, DotToken],
    (CommaSeq, CommaToken): [CommaToken, IdentToken, CommaSeq],
    (CommaSeq, DotToken): [],
    (Grammar, EOPToken): []
}


def parse(scanner: Scanner):
    first = Node(object, [])
    tree_stack = [first]
    stack = [Grammar]
    for token in scanner.tokens():
        while True:
            parent = tree_stack.pop()
            rule = stack.pop()
            print((rule, type(token)))
            if issubclass(rule, Token):
                if type(token) == rule:
                    parent.leafs.append(token)
                    break
                else:
                    print(f'Ожидался {rule} получен {type(token)}')
            elif (rule, type(token)) in sintax.keys():
                leaf = Node(rule, [])
                parent.leafs.append(leaf)
                to_add = sintax[(rule, type(token))]
                for i in to_add[::-1]:
                    tree_stack.append(leaf)
                    stack.append(i)
                if type(token) == EOPToken:
                    break
                
            else:
                print(f'Ожидался {rule} получен {type(token)}')
    return first.leafs[0]

with open(r"text.txt", "r") as f:
    program = ""
    for line in f.readlines():
        if not program:
            program += line
        else:
            program += line
    compiler: Compiler = Compiler()
    scanner = compiler.get_scanner(program)
    pprint(parse(scanner))




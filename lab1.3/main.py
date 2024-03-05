from typing import Generator
class Token:
    pass

class Position: pass
class Coord: pass
class Fragment:pass

class StringToken(Token):
    coords: Fragment
    attr: str
    def __init__(self, coords: Fragment, attr: str) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(StringToken: ({self.coords}), attr={self.attr})"
class NumToken(Token):
    coords: Fragment
    attr: str
    def __init__(self, coords: Fragment, attr: str) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(NumToken: ({self.coords}), attr={self.attr})"
class IdentToken(Token):
    coords: Fragment
    attr: str
    def __init__(self, coords: Fragment, attr: str) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(IdentToken: ({self.coords}), attr={self.attr})"
class EOPToken(Token):
    coords: Fragment
    attr: str
    def __init__(self, coords: Fragment, attr: str) -> None:
        self.coords = coords
        self.attr = attr
    def __str__(self) -> str:
        return f"(EOPToken: ({self.coords}), attr={self.attr})"

class Fragment:
    opening: Coord
    ending: Coord
    def __init__(self, opening: Coord, ending: Coord) -> None:
        self.opening = opening
        self.ending = ending
    def __str__(self) -> str:
        return 'from' + str(self.opening) + 'to' + str(self.ending)

class Coord:
    def __init__(self, position: Position) -> None:
        self.line: int = position.line 
        self.pos: int = position.pos
    def __str__(self) -> str:
        return f'(line: {self.line}, pos: {self.pos})'

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

class Compiler:
    pass

class Scanner:
    program: str
    def __init__(self, compiler: Compiler,
                  program: str) -> None:
        self._compiler: Compiler = compiler
        self.program = program
        self._position: Position = Position(program)
    def tokens(self) -> Generator[Token, None, None]:
        panic = False
        while self._position.read() != '':
            
            match self._position.read():
                case x if str.isspace(x):
                    self._position.next()
                case '"':
                    panic = False
                    opening: Coord = Coord(self._position)
                    o_i = self._position.index
                    self._position.next()
                    escape = False
                    res_str = ""
                    while (escape or self._position.read() != '"') \
                     and self._position.read() != "":
                        if self._position.read() == '\n':
                            panic = True
                            self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "multiline string")
                            break
                        elif not escape and self._position.read() == "\\":
                            escape = True
                        elif escape:
                            match self._position.read():
                                case "n":
                                    res_str += "\n"
                                case "t":
                                    res_str += "\t"
                                case '"':
                                    res_str += '"'
                                case "\\":
                                    res_str += "\\"
                                case _:
                                    res_str += "\\"+ self._position.read()
                            escape = False
                        else:
                            res_str += self._position.read()
                        self._position.next()
                    if panic:
                        continue
                    if self._position.read() == "":
                        panic = True
                        self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "multiline string")
                        continue
                    ending: Coord = Coord(self._position)
                    e_i = self._position.index
                    self._position.next()
                    yield StringToken(Fragment(opening, ending),
                                       res_str)
                case x if str.isalpha(x) or x == '_':
                    panic = False
                    opening: Coord = Coord(self._position)
                    name = self._position.read()
                    self._position.next()
                    go = True
                    while go:
                        if (self._position.read().isalpha() or
                             self._position.read().isdigit() or
                               self._position.read() == "_"):
                            name += self._position.read()
                            self._position.next()
                        else:
                            go = False
                    ending: Coord = Coord(self._position)
                    code = self._compiler.names.contains(name)
                    if code == -1:
                        code = self._compiler.names.add_name(name)
                    yield IdentToken(Fragment(opening, ending), code)
                case x if str.isdigit(x):
                    panic = False
                    opening: Coord = Coord(self._position)
                    o_i = self._position.index
                    number = self._position.read()
                    self._position.next()
                    go = True
                    num_counter = 0
                    is_first = True
                    
                    while go:
                        if self._position.read().isdigit():
                            number += self._position.read()
                            if num_counter > 3:
                                panic = True
                                self._compiler.messages.\
                                    add_error(Coord(self._position),
                                               "bad humber format")
                                break
                            else:
                                num_counter+=1
                                self._position.next()
                        elif self._position.read() == ".":
                            if (num_counter==3 \
                                or is_first and num_counter<3):
                                is_first = False
                                num_counter = 0
                                self._position.next()
                            else:
                                panic = True
                                self._compiler.messages.\
                                    add_error(Coord(self._position),
                                               "bad humber format")
                                break
                        else:
                            go = False
                    if not panic and  num_counter < 3 and not is_first:
                        panic = True
                        self._compiler.messages.\
                            add_error(Coord(self._position),
                                       "bad humber format")
                    if panic:
                        continue
                    ending: Coord = Coord(self._position)
                    e_i = self._position.index
                    yield NumToken(Fragment(opening, ending), 
                                   int(number))
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
    def add_error(self, coord: Position,
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
    def __init__(self) -> None:
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
    for token in scanner.tokens():
        print(token)
    print([str(i) for i in 
           scanner._compiler.messages.get_sorted()])




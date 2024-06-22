% Лабораторная работа № 2.3 «Синтаксический анализатор на основе
  предсказывающего анализа»
% 15 апреля 2024 г.
% Андрей Кабанов, ИУ9-62Б

# Цель работы

Целью данной работы является изучение алгоритма построения таблиц
 предсказывающего анализатора.

# Индивидуальный вариант

```
tokens <plus sign>, <star>, <n>.
<E>   is <T> <E 1>.
<E 1> is <plus sign> <T> <E 1>.
<E 1> is .
<T>   is <F> <T 1>.
<T 1> is <star> <F> <T 1>.
<T 1> is .
<F>   is <n>.
tokens <left paren>, <right paren>.
<F>   is <left paren> <E> <right paren>.
<!-- аксиома -->
start <E>.
```

# Реализация

## Неформальное описание синтаксиса входного языка

```
Grammar ::= (TermInit Axiom Rule)*
Axiom ::= StartToken IdentToken
Rule ::= IdentToken (IdentToken)*
TermInit ::= TokensToken (IdentToken)*
```

## Лексическая структура

```
StartToken -> start
TokensToken -> tokens
CommaToken -> ,
DotToken -> \.
IsToken -> is
IdentToken -> <[a-zA-Z-0-9 ]*>
```

## Грамматика языка

```
Grammar ::= TermInit Grammar | Axiom Grammar | Rule Grammar | eps
Axiom ::= StartToken IdentToken DotToken
Rule ::= IdentToken IsToken IdentSeq DotToken
IdentSeq ::= IdentToken IdentSeq | eps
TermInit ::= TokensToken IdentToken CommaSeq DotToken
CommaSeq ::= CommaToken IdentToken CommaSeq | eps
```

## Программная реализация

```
from typing import Generator
from dataclasses import dataclass
from typing import Any
from pprint import pprint


class Token:
    pass


class IsToken(Token):
    coords: "Fragment"
    attr: str = "is"

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(IsToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"IsToken({self.coords!r})"


class CommaToken(Token):
    coords: "Fragment"
    attr: str = ","

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(CommaToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"CommaToken({self.coords!r})"


class DotToken(Token):
    coords: "Fragment"
    attr: str = "."

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(DotToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"DotToken({self.coords!r})"


class TokensToken(Token):
    coords: "Fragment"
    attr: str = "tokens"

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(TokensToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"TokensToken({self.coords!r})"


class StartToken(Token):
    coords: "Fragment"
    attr: str = "start"

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(StartToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"StartToken({self.coords!r})"


class IdentToken(Token):
    coords: "Fragment"
    attr: int

    def __init__(self, coords: "Fragment", attr: int) -> None:
        self.coords = coords
        self.attr = attr

    def __str__(self) -> str:
        return f"(IdentToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"IdentToken({self.coords!r}, {self.attr})"


class EOPToken(Token):
    coords: "Fragment"
    attr: str

    def __init__(self, coords: "Fragment", attr: str) -> None:
        self.coords = coords
        self.attr = attr

    def __str__(self) -> str:
        return f"(EOPToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"EOPToken({self.coords!r}, {self.attr})"


class Fragment:
    opening: "Coord"
    ending: "Coord"

    def __init__(self, opening: "Coord", ending: "Coord") -> None:
        self.opening = opening
        self.ending = ending

    def __str__(self) -> str:
        return "from" + str(self.opening) + "to" + str(self.ending)

    def __repr__(self) -> str:
        return f"Fragment({self.opening!r}, {self.ending!r})"


class Coord:
    def __init__(self, position: "Position") -> None:
        self.line: int = position.line
        self.pos: int = position.pos

    def __str__(self) -> str:
        return f"(line: {self.line}, pos: {self.pos})"

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
        return "" if self.index == len(self.text) else self.text[self.index]

    def next(self):
        if self.index + 1 < len(self.text):
            if self.text[self.index] == "\n":
                self.line += 1
                self.pos = 1
                self.index += 1
            else:
                self.pos += 1
                self.index += 1
        elif self.index + 1 == len(self.text):
            self.index += 1
        else:
            raise (EOFError)

    def read_next(self):
        if self.index + 1 < len(self.text):
            return self.text[self.index + 1]
        elif self.index + 1 == len(self.text):
            return ""
        else:
            raise (EOFError)

    def __str__(self) -> str:
        return f"(line: {self.line}, pos: {self.pos})"


class Message:
    is_error: bool
    text: str
    coord: Coord

    def __init__(self, is_error: bool, text: str, coord: Coord) -> None:
        self.is_error = is_error
        self.text = text
        self.coord = coord

    def __str__(self) -> str:
        return (
            ("(Error" if self.is_error else "(Warning")
            + str(self.coord)
            + self.text
            + ")"
        )


class Comment:
    text: str
    coord: Coord

    def __init__(self, text: str, coord: Coord) -> None:
        self.text = text
        self.coord = coord

    def __str__(self) -> str:
        return "(Comment " + self.text + " )"


class Scanner:
    program: str

    def __init__(self, compiler: "Compiler", program: str) -> None:
        self._compiler: Compiler = compiler
        self.program = program
        self._position: Position = Position(program)

    def tokens(
        self,
    ) -> Generator[
        IdentToken
        | TokensToken
        | StartToken
        | IsToken
        | CommaToken
        | DotToken
        | EOPToken,
        None,
        None,
    ]:
        panic = False
        while self._position.read() != "":

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
                    if self._position.read() == "s":
                        self._position.next()
                        ending: Coord = Coord(self._position)
                        yield IsToken(Fragment(opening, ending))
                    else:
                        panic = True
                        self._compiler.messages.add_error(
                            Coord(self._position), "Bad is Key Word"
                        )
                        self._position.next()
                case "t":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    left = ["o", "k", "e", "n", "s"]
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
                    self._compiler.messages.add_error(
                        Coord(self._position), "Bad tokens Key Word"
                    )
                case "s":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    left = ["t", "a", "r", "t"]
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
                    self._compiler.messages.add_error(
                        Coord(self._position), "Bad start Key Word"
                    )

                case "<":
                    panic = False
                    opening: Coord = Coord(self._position)
                    self._position.next()
                    if self._position.read() == "!":
                        text = ""
                        self._position.next()
                        if self._position.read() == "-":
                            self._position.next()
                            if self._position.read() == "-":
                                self._position.next()
                                while self._position.read() != "-":
                                    text += self._position.read()
                                    self._position.next()
                                    if self._position.read() == "\n":
                                        break
                                else:
                                    self._position.next()
                                    if self._position.read() == "-":
                                        self._position.next()
                                        if self._position.read() == ">":
                                            self._compiler.comments.append(
                                                Comment(text, opening)
                                            )
                                            self._position.next()
                                            continue
                        panic = True
                        self._compiler.messages.add_error(
                            Coord(self._position), "Bad Comment"
                        )
                        continue
                    ident = ""
                    while (
                        str.isalpha(self._position.read())
                        or str.isdigit(self._position.read())
                        or self._position.read() == " "
                    ):
                        ident += self._position.read()
                        self._position.next()
                    else:
                        if self._position.read() == ">":
                            self._position.next()
                            ending: Coord = Coord(self._position)
                            code = self._compiler.names.contains(ident)
                            if code == -1:
                                code = self._compiler.names.add_name(ident)
                            yield IdentToken(Fragment(opening, ending), code)
                        else:
                            panic = True
                            self._compiler.messages.add_error(
                                Coord(self._position), "Bad Token Name"
                            )
                            self._position.next()
                case _:
                    if panic:
                        self._position.next()
                    else:
                        panic = True
        yield EOPToken(
            Fragment(Coord(self._position), Coord(self._position)), "End of Program"
        )


class NameDictionary:
    _names: dict[int, str]
    _num: int

    def __init__(self) -> None:
        self._names = {}
        self._num = 0

    def add_name(self, s: str) -> int:
        self._names[self._num] = s
        self._num += 1
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

    def add_error(self, coord: Coord, text: str) -> None:
        self._messages.append(Message(True, text, coord))

    def add_warning(self, coord, text: str) -> None:
        self._messages.append(Message(False, text, coord))

    def get_sorted(self):
        return sorted(self._messages, key=lambda x: x.coord.line)


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
    leafs: list["Node|Token"]


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
    (Grammar, EOPToken): [],
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
                    print(f"Ожидался {rule} получен {type(token)}")
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
                print(f"Ожидался {rule} получен {type(token)}")
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

```

# Тестирование

Входные данные

```
tokens <plus sign>, <star>, <n>.
<E>   is <T> <E 1>.
<E 1> is <plus sign> <T> <E 1>.
<E 1> is .
<T>   is <F> <T 1>.
<T 1> is <star> <F> <T 1>.
<T 1> is .
<F>   is <n>.
tokens <left paren>, <right paren>.
<F>   is <left paren> <E> <right paren>.
<!-- аксиома -->
start <E>.
```

Вывод на `stdout`

<!-- ENABLE LONG LINES -->

```
Node(name=<class '__main__.Grammar'>,
     leafs=[Node(name=<class '__main__.TermInit'>,
                 leafs=[TokensToken(Fragment(Coord(1, 1), Coord(1, 7))),
                        IdentToken(Fragment(Coord(1, 8), Coord(1, 19)), 0),
                        Node(name=<class '__main__.CommaSeq'>,
                             leafs=[CommaToken(Fragment(Coord(1, 19), Coord(1, 20))),
                                    IdentToken(Fragment(Coord(1, 21), Coord(1, 27)), 1),
                                    Node(name=<class '__main__.CommaSeq'>,
                                         leafs=[CommaToken(Fragment(Coord(1, 27), Coord(1, 28))),
                                                IdentToken(Fragment(Coord(1, 29), Coord(1, 32)), 2),
                                                Node(name=<class '__main__.CommaSeq'>,
                                                     leafs=[])])]),
                        DotToken(Fragment(Coord(1, 32), Coord(1, 33)))]),
            Node(name=<class '__main__.Grammar'>,
                 leafs=[Node(name=<class '__main__.Rule'>,
                             leafs=[IdentToken(Fragment(Coord(2, 1), Coord(2, 4)), 3),
                                    IsToken(Fragment(Coord(2, 7), Coord(2, 9))),
                                    Node(name=<class '__main__.IdentSeq'>,
                                         leafs=[IdentToken(Fragment(Coord(2, 10), Coord(2, 13)), 4),
                                                Node(name=<class '__main__.IdentSeq'>,
                                                     leafs=[IdentToken(Fragment(Coord(2, 14), Coord(2, 19)), 5),
                                                            Node(name=<class '__main__.IdentSeq'>,
                                                                 leafs=[])])]),
                                    DotToken(Fragment(Coord(2, 19), Coord(2, 20)))]),
                        Node(name=<class '__main__.Grammar'>,
                             leafs=[Node(name=<class '__main__.Rule'>,
                                         leafs=[IdentToken(Fragment(Coord(3, 1), Coord(3, 6)), 5),
                                                IsToken(Fragment(Coord(3, 7), Coord(3, 9))),
                                                Node(name=<class '__main__.IdentSeq'>,
                                                     leafs=[IdentToken(Fragment(Coord(3, 10), Coord(3, 21)), 0),
                                                            Node(name=<class '__main__.IdentSeq'>,
                                                                 leafs=[IdentToken(Fragment(Coord(3, 22), Coord(3, 25)), 4),
                                                                        Node(name=<class '__main__.IdentSeq'>,
                                                                             leafs=[IdentToken(Fragment(Coord(3, 26), Coord(3, 31)), 5),
                                                                                    Node(name=<class '__main__.IdentSeq'>,
                                                                                         leafs=[])])])]),
                                                DotToken(Fragment(Coord(3, 31), Coord(3, 32)))]),
                                    Node(name=<class '__main__.Grammar'>,
                                         leafs=[Node(name=<class '__main__.Rule'>,
                                                     leafs=[IdentToken(Fragment(Coord(4, 1), Coord(4, 6)), 5),
                                                            IsToken(Fragment(Coord(4, 7), Coord(4, 9))),
                                                            Node(name=<class '__main__.IdentSeq'>,
                                                                 leafs=[]),
                                                            DotToken(Fragment(Coord(4, 10), Coord(4, 11)))]),
                                                Node(name=<class '__main__.Grammar'>,
                                                     leafs=[Node(name=<class '__main__.Rule'>,
                                                                 leafs=[IdentToken(Fragment(Coord(5, 1), Coord(5, 4)), 4),
                                                                        IsToken(Fragment(Coord(5, 7), Coord(5, 9))),
                                                                        Node(name=<class '__main__.IdentSeq'>,
                                                                             leafs=[IdentToken(Fragment(Coord(5, 10), Coord(5, 13)), 6),
                                                                                    Node(name=<class '__main__.IdentSeq'>,
                                                                                         leafs=[IdentToken(Fragment(Coord(5, 14), Coord(5, 19)), 7),
                                                                                                Node(name=<class '__main__.IdentSeq'>,
                                                                                                     leafs=[])])]),
                                                                        DotToken(Fragment(Coord(5, 19), Coord(5, 20)))]),
                                                            Node(name=<class '__main__.Grammar'>,
                                                                 leafs=[Node(name=<class '__main__.Rule'>,
                                                                             leafs=[IdentToken(Fragment(Coord(6, 1), Coord(6, 6)), 7),
                                                                                    IsToken(Fragment(Coord(6, 7), Coord(6, 9))),
                                                                                    Node(name=<class '__main__.IdentSeq'>,
                                                                                         leafs=[IdentToken(Fragment(Coord(6, 10), Coord(6, 16)), 1),
                                                                                                Node(name=<class '__main__.IdentSeq'>,
                                                                                                     leafs=[IdentToken(Fragment(Coord(6, 17), Coord(6, 20)), 6),
                                                                                                            Node(name=<class '__main__.IdentSeq'>,
                                                                                                                 leafs=[IdentToken(Fragment(Coord(6, 21), Coord(6, 26)), 7),
                                                                                                                        Node(name=<class '__main__.IdentSeq'>,
                                                                                                                             leafs=[])])])]),
                                                                                    DotToken(Fragment(Coord(6, 26), Coord(6, 27)))]),
                                                                        Node(name=<class '__main__.Grammar'>,
                                                                             leafs=[Node(name=<class '__main__.Rule'>,
                                                                                         leafs=[IdentToken(Fragment(Coord(7, 1), Coord(7, 6)), 7),
                                                                                                IsToken(Fragment(Coord(7, 7), Coord(7, 9))),
                                                                                                Node(name=<class '__main__.IdentSeq'>,
                                                                                                     leafs=[]),
                                                                                                DotToken(Fragment(Coord(7, 10), Coord(7, 11)))]),
                                                                                    Node(name=<class '__main__.Grammar'>,
                                                                                         leafs=[Node(name=<class '__main__.Rule'>,
                                                                                                     leafs=[IdentToken(Fragment(Coord(8, 1), Coord(8, 4)), 6),
                                                                                                            IsToken(Fragment(Coord(8, 7), Coord(8, 9))),
                                                                                                            Node(name=<class '__main__.IdentSeq'>,
                                                                                                                 leafs=[IdentToken(Fragment(Coord(8, 10), Coord(8, 13)), 2),
                                                                                                                        Node(name=<class '__main__.IdentSeq'>,
                                                                                                                             leafs=[])]),
                                                                                                            DotToken(Fragment(Coord(8, 13), Coord(8, 14)))]),
                                                                                                Node(name=<class '__main__.Grammar'>,
                                                                                                     leafs=[Node(name=<class '__main__.TermInit'>,
                                                                                                                 leafs=[TokensToken(Fragment(Coord(9, 1), Coord(9, 7))),
                                                                                                                        IdentToken(Fragment(Coord(9, 8), Coord(9, 20)), 8),
                                                                                                                        Node(name=<class '__main__.CommaSeq'>,
                                                                                                                             leafs=[CommaToken(Fragment(Coord(9, 20), Coord(9, 21))),
                                                                                                                                    IdentToken(Fragment(Coord(9, 22), Coord(9, 35)), 9),
                                                                                                                                    Node(name=<class '__main__.CommaSeq'>,
                                                                                                                                         leafs=[])]),
                                                                                                                        DotToken(Fragment(Coord(9, 35), Coord(9, 36)))]),
                                                                                                            Node(name=<class '__main__.Grammar'>,
                                                                                                                 leafs=[Node(name=<class '__main__.Rule'>,
                                                                                                                             leafs=[IdentToken(Fragment(Coord(10, 1), Coord(10, 4)), 6),
                                                                                                                                    IsToken(Fragment(Coord(10, 7), Coord(10, 9))),
                                                                                                                                    Node(name=<class '__main__.IdentSeq'>,
                                                                                                                                         leafs=[IdentToken(Fragment(Coord(10, 10), Coord(10, 22)), 8),
                                                                                                                                                Node(name=<class '__main__.IdentSeq'>,
                                                                                                                                                     leafs=[IdentToken(Fragment(Coord(10, 23), Coord(10, 26)), 3),
                                                                                                                                                            Node(name=<class '__main__.IdentSeq'>,
                                                                                                                                                                 leafs=[IdentToken(Fragment(Coord(10, 27), Coord(10, 40)), 9),
                                                                                                                                                                        Node(name=<class '__main__.IdentSeq'>,
                                                                                                                                                                             leafs=[])])])]),
                                                                                                                                    DotToken(Fragment(Coord(10, 40), Coord(10, 41)))]),
                                                                                                                        Node(name=<class '__main__.Grammar'>,
                                                                                                                             leafs=[Node(name=<class '__main__.Axiom'>,
                                                                                                                                         leafs=[StartToken(Fragment(Coord(12, 1), Coord(12, 6))),
                                                                                                                                                IdentToken(Fragment(Coord(12, 7), Coord(12, 10)), 3),
                                                                                                                                                DotToken(Fragment(Coord(12, 10), Coord(12, 11)))]),
                                                                                                                                    Node(name=<class '__main__.Grammar'>,
                                                                                                                                         leafs=[])])])])])])])])])])])])
```

# Вывод

В ходе выполнения лабораторной работы были приобретены навыки написания предсказывающего
анализатора, а также была написана ll1 грамматика языка грамматики.

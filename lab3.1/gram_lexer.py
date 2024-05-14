from typing import Generator, Iterable
from sys import argv
from gram import *
from functools import reduce
import gram_parser


class IsToken(IsBaseToken):
    coords: "Fragment"
    attr: str = "is"

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(IsToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"IsToken({self.coords!r})"


class CommaToken(CommaBaseToken):
    coords: "Fragment"
    attr: str = ","

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(CommaToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"CommaToken({self.coords!r})"


class DotToken(DotBaseToken):
    coords: "Fragment"
    attr: str = "."

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(DotToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"DotToken({self.coords!r})"


class TokensToken(TokensBaseToken):
    coords: "Fragment"
    attr: str = "tokens"

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(TokensToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"TokensToken({self.coords!r})"


class StartToken(StartBaseToken):
    coords: "Fragment"
    attr: str = "start"

    def __init__(self, coords: "Fragment") -> None:
        self.coords = coords

    def __str__(self) -> str:
        return f"(StartToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"StartToken({self.coords!r})"


class IdentToken(IdentBaseToken):
    coords: "Fragment"
    attr: int

    def __init__(self, coords: "Fragment", attr: int) -> None:
        self.coords = coords
        self.attr = attr

    def __str__(self) -> str:
        return f"(IdentToken: ({self.coords}), attr={self.attr})"

    def __repr__(self) -> str:
        return f"IdentToken({self.coords!r}, {self.attr})"


class EOPToken(EOPBaseToken):
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

    def keys(self) -> set[int]:
        return set(self._names.keys())


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

    def parse(self, program: str):

        generator(
            gram_parser.parse(
                self.get_scanner(program), parse_table, GrammarBase, EOPBaseToken, Token
            ),
            self.names,
            argv[2],
        )


class HealthyGrammar:
    rules: dict[int, list[list[int]]]
    axiom: int
    nterms: set[int]
    terms: set[int]
    name_dict: NameDictionary
    follow_sets: dict[int, set[int]]
    table: dict[tuple[int, int], list[int]]

    def idents_check(self):
        if self.terms | self.nterms != self.name_dict.keys():
            raise Exception("Unknown NTerm or Term")

    def __init__(
        self,
        rules: dict[int, list[list[int]]],
        axiom: int,
        nterms: set[int],
        terms: set[int],
        name_dict: NameDictionary,
    ) -> None:
        self.nterms = nterms
        self.terms = terms
        self.name_dict = name_dict
        self.idents_check()
        for nterm in rules:
            for i in range(len(rules[nterm])):
                if not rules[nterm][i]:
                    rules[nterm][i].append(-1)
        self.rules = rules
        self.axiom = axiom
        self.follow_sets = {}
        self.gen_all_follow()
        self.is_ll_one()
        self.table = {}
        self.gen_table()

    def __str__(self) -> str:
        res = ""
        res += f"Starts with {self.name_dict[self.axiom]}\n"
        res += f"NTerms {[self.name_dict[i] for i in self.nterms]}\n"
        res += f"Terms {[self.name_dict[i] for i in self.terms]}\n"
        res += "\n"
        for rule in self.rules.keys():
            res += f'{self.name_dict[rule]} := {[[self.name_dict[j] if j != -1 else "eps" for j in i] for i in self.rules[rule]]}\n'
        for rule in self.rules.keys():
            for sub_rule in self.rules[rule]:
                res += f"First for {self.to_str(sub_rule)} is {self.to_str(self.gen_first(sub_rule))}\n"
        for nterm in self.nterms:
            res += f"Follow for {self.name_dict[nterm]} is {self.to_str(self.follow_sets[nterm])}\n"
        return res

    def name_to_class(self, id: int):
        def replace_spaces(s: str):
            return s.replace(" ", "_")

        if id in self.nterms:
            return replace_spaces(self.name_dict[id]) + "Base"
        elif id in self.terms:
            return replace_spaces(self.name_dict[id]) + "BaseToken"
        else:
            return "EOPBaseToken"

    def table_to_str(self) -> str:
        str_table = "parse_table = {\n"
        for key in self.table.keys():
            str_table += (
                f"\t({self.name_to_class(key[0])}, {self.name_to_class(key[1])}): "
            )
            str_table += (
                "["
                + ", ".join(map(lambda x: self.name_to_class(x), self.table[key]))
                + "], \n"
            )
        str_table += "}\n"
        return str_table

    def gen_classes(self):
        str_classes = "from abc import ABC\nfrom typing import Any\n\n"
        str_classes += f"class Token(ABC):\n\tattr: Any\n...\n\n"

        for i in self.nterms:
            str_classes += f"class {self.name_to_class(i)}(ABC):\n\t...\n\n"
        for i in self.terms:
            str_classes += f"class {self.name_to_class(i)}(Token):\n\t...\n\n"
        str_classes += f"class {self.name_to_class(-2)}(Token, ABC):\n\t...\n\n"
        return str_classes

    def gen(self):
        return self.gen_classes() + "\n" + self.table_to_str() + "\n"

    def to_str(self, idents: Iterable[int]) -> str:
        return str(
            [
                self.name_dict[i] if i > -1 else "eps" if i > -2 else "EOP"
                for i in idents
            ]
        )

    def gen_first(self, rule, marked=None) -> set[int]:
        if rule:
            if rule[0] in self.terms:
                return set([rule[0]])
            elif rule[0] == -1:
                return set([-1])
            if rule[0] in self.nterms:
                if not marked:
                    marked = []
                marked.append(rule[0])
                res = set()
                alter = self.rules[rule[0]]
                for rule1 in alter:
                    marked1 = marked.copy()
                    if not rule1[0] in marked1:
                        first_for = self.gen_first(rule1, marked1)
                        for f_term in first_for:
                            res.add(f_term)
                if -1 not in res:
                    return res
                else:
                    new_res = set()
                    res = set(filter(lambda x: x != -1, res))
                    if len(rule) > 1:
                        marked1 = marked.copy()
                        if not rule[1:] in marked1:
                            new_first = self.gen_first(rule[1:], marked1)
                            new_res = res.union(new_first)
                            new_res = set(res)
                            return new_res
                    res.add(-1)
                    return res

            return set()
        return set()

    def gen_follow(self, nterm) -> set[int]:
        follow = set()
        if nterm == self.axiom:
            follow.add(-2)
        for current in self.nterms:
            right_rules = self.rules[current]
            for sub_rule in right_rules:
                if nterm in sub_rule:
                    while nterm in sub_rule:
                        nterm_index = sub_rule.index(
                            next(filter(lambda x: x == nterm, sub_rule))
                        )
                        sub_rule = sub_rule[nterm_index + 1 :]
                        res = None
                        if sub_rule:
                            res = self.gen_first(sub_rule, None)
                            if -1 in res:
                                res = set(filter(lambda x: x != -1, res))
                                current_follow = self.gen_follow(current)
                                res = res.union(current_follow)
                        else:
                            if nterm != current:
                                res = self.gen_follow(current)
                        if res:
                            for i in res:
                                follow.add(i)
        return follow

    def gen_all_follow(self) -> None:
        for nterm in self.nterms:
            self.follow_sets[nterm] = self.gen_follow(nterm)

    def is_ll_one(self):
        for nterm in self.nterms:
            if len(self.rules[nterm]) <= 1:
                continue
            if reduce(
                lambda x, y: x & y, [self.gen_first(i) for i in self.rules[nterm]]
            ):
                raise Exception("Not LL1")
            for i in range(len(self.rules[nterm]) - 1):
                first1 = self.gen_first(self.rules[nterm][i])

                for j in range(i + 1, len(self.rules[nterm])):
                    first2 = self.gen_first(self.rules[nterm][j])
                    if (
                        -1 in first1
                        and self.follow_sets[nterm] & first2
                        or -1 in first2
                        and self.follow_sets[nterm] & first1
                    ):
                        raise Exception("Not LL1")

    def gen_table(self):
        for nterm in self.nterms:
            for rule in self.rules[nterm]:
                for a in self.gen_first(rule):
                    if a != -1 and not (nterm, a) in self.table.keys():
                        self.table[(nterm, a)] = rule
                    elif a != -1:
                        self.table[(nterm, a)] += rule
                    else:
                        for b in self.follow_sets[nterm]:
                            if not (nterm, b) in self.table.keys():
                                self.table[(nterm, b)] = rule if rule != [-1] else []
                            else:
                                self.table[(nterm, b)] += rule if rule != [-1] else []


def analyse_rules(
    rules: dict[int, list[list[int]]], new_rules: dict[int, list[list[int]]]
) -> dict[int, list[list[int]]]:
    rules_keys = rules.keys()
    new_rules_keys = new_rules.keys()
    for new_rules_key in new_rules_keys:
        if not new_rules_key in rules_keys:
            rules[new_rules_key] = new_rules[new_rules_key]
        else:
            rules[new_rules_key] += new_rules[new_rules_key]
    return rules


def analyse_axiom(axiom: int | None, new_axiom: int | None) -> None | int:
    if axiom and new_axiom:
        raise Exception("To many axioms")
    else:
        return axiom if axiom else new_axiom


def analyse_comma_seq(tree) -> list[int]:
    idents = []
    if tree.leafs:
        idents.append(tree.leafs[1].attr)
        idents += analyse_comma_seq(tree.leafs[2])
    return idents


def analyse_ident_seq(tree) -> list[int]:
    idents = []
    if tree.leafs:
        idents.append(tree.leafs[0].attr)
        idents += analyse_ident_seq(tree.leafs[1])
    return idents


def cure_grammar(
    tree,
) -> tuple[dict[int, list[list[int]]], int | None, list[int], list[int]]:
    rules: dict[int, list[list[int]]] = {}
    axiom = None
    nterm_names: list[int] = []
    term_names: list[int] = []
    if tree.name == GrammarBase:
        for leaf in tree.leafs:
            res_rules, res_axiom, res_nterm_names, res_term_names = cure_grammar(leaf)
            rules = analyse_rules(rules, res_rules)
            axiom = analyse_axiom(axiom, res_axiom)
            nterm_names += res_nterm_names
            term_names += res_term_names
    elif tree.name == TermInitBase:
        term_names.append(tree.leafs[1].attr)
        for term in analyse_comma_seq(tree.leafs[2]):
            term_names.append(term)

    elif tree.name == RuleBase:
        nterm = tree.leafs[0].attr
        nterm_names.append(nterm)
        right_rule = analyse_ident_seq(tree.leafs[2])
        rules[nterm] = [right_rule]
    elif tree.name == AxiomBase:
        axiom = tree.leafs[1].attr
    return rules, axiom, nterm_names, term_names


def generator(tree, name_dict: NameDictionary, gram_name: str):
    rules, axiom, nterm_names, term_names = cure_grammar(tree)
    if not axiom:
        raise Exception("No axiom")
    grammar = HealthyGrammar(rules, axiom, set(nterm_names), set(term_names), name_dict)
    with open(gram_name + ".py", "w") as f:
        f.write(grammar.gen())


with open(argv[1], "r") as f:
    program = ""
    for line in f.readlines():
        if not program:
            program += line
        else:
            program += line
    compiler: Compiler = Compiler()

    compiler.parse(program)

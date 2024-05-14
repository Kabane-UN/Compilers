from abc import ABC
from typing import Any


class Token(ABC):
    attr: Any


...


class GrammarBase(ABC): ...


class TermInitBase(ABC): ...


class AxiomBase(ABC): ...


class RuleBase(ABC): ...


class IdentSeqBase(ABC): ...


class CommaSeqBase(ABC): ...


class IsBaseToken(Token): ...


class DotBaseToken(Token): ...


class CommaBaseToken(Token): ...


class TokensBaseToken(Token): ...


class StartBaseToken(Token): ...


class IdentBaseToken(Token): ...


class EOPBaseToken(Token, ABC): ...


parse_table = {
    (GrammarBase, TokensBaseToken): [TermInitBase, GrammarBase],
    (GrammarBase, StartBaseToken): [AxiomBase, GrammarBase],
    (GrammarBase, IdentBaseToken): [RuleBase, GrammarBase],
    (GrammarBase, EOPBaseToken): [],
    (TermInitBase, TokensBaseToken): [
        TokensBaseToken,
        IdentBaseToken,
        CommaSeqBase,
        DotBaseToken,
    ],
    (AxiomBase, StartBaseToken): [StartBaseToken, IdentBaseToken, DotBaseToken],
    (RuleBase, IdentBaseToken): [
        IdentBaseToken,
        IsBaseToken,
        IdentSeqBase,
        DotBaseToken,
    ],
    (IdentSeqBase, IdentBaseToken): [IdentBaseToken, IdentSeqBase],
    (IdentSeqBase, DotBaseToken): [],
    (CommaSeqBase, CommaBaseToken): [CommaBaseToken, IdentBaseToken, CommaSeqBase],
    (CommaSeqBase, DotBaseToken): [],
}

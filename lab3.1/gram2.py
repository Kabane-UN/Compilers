from abc import ABC
from typing import Any


class Token(ABC):
    attr: Any


...


class ExprBase(ABC): ...


class TermBase(ABC): ...


class SubAddSeqBase(ABC): ...


class FactorBase(ABC): ...


class MulDivSeqBase(ABC): ...


class AddBaseToken(Token): ...


class SubBaseToken(Token): ...


class MulBaseToken(Token): ...


class DivBaseToken(Token): ...


class NumBaseToken(Token): ...


class RightParenBaseToken(Token): ...


class LeftParenBaseToken(Token): ...


class EOPBaseToken(Token, ABC): ...


parse_table = {
    (ExprBase, NumBaseToken): [TermBase, SubAddSeqBase],
    (ExprBase, LeftParenBaseToken): [TermBase, SubAddSeqBase],
    (TermBase, NumBaseToken): [FactorBase, MulDivSeqBase],
    (TermBase, LeftParenBaseToken): [FactorBase, MulDivSeqBase],
    (SubAddSeqBase, AddBaseToken): [AddBaseToken, TermBase, SubAddSeqBase],
    (SubAddSeqBase, SubBaseToken): [SubBaseToken, TermBase, SubAddSeqBase],
    (SubAddSeqBase, RightParenBaseToken): [],
    (SubAddSeqBase, EOPBaseToken): [],
    (FactorBase, NumBaseToken): [NumBaseToken],
    (FactorBase, LeftParenBaseToken): [
        LeftParenBaseToken,
        ExprBase,
        RightParenBaseToken,
    ],
    (MulDivSeqBase, MulBaseToken): [MulBaseToken, FactorBase, MulDivSeqBase],
    (MulDivSeqBase, DivBaseToken): [DivBaseToken, FactorBase, MulDivSeqBase],
    (MulDivSeqBase, AddBaseToken): [],
    (MulDivSeqBase, SubBaseToken): [],
    (MulDivSeqBase, RightParenBaseToken): [],
    (MulDivSeqBase, EOPBaseToken): [],
}

# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ..row import Row


class Trailer:

    def __init__(self):
        self.content = "00000005         000003000000000000000000000000000000000000                                                                                                                                                                                     "

    def setAmountInCents(self, amount):
        structs = [
            (23, 41, 18, numeric, amount),                     # Soma dos valores dos lotes
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),                   # Código do banco debitado
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)                          # Indica index do lote
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
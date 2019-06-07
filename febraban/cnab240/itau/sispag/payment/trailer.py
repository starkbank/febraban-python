# coding: utf-8

from ....characterType import numeric
from ....row import Row


class Trailer:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            ( 7,   8, 1,      numeric, "5"),
            (17,  23, 6,      numeric, "3"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

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

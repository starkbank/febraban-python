# coding: utf-8

from ....row import Row
from ....characterType import numeric


class TrailerLot:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            ( 3,   7,  4, numeric, "1"),
            ( 7,   8,  1, numeric, "5"),
            (41,  59, 18, numeric, "0"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setLotNumberOfRegisters(self, sum):
        structs = [
            (17,  23,  6, numeric, sum),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSumOfValues(self, sum):
        structs = [
            (23, 41, 18, numeric, sum),                     # Soma dos valores dos lotes
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

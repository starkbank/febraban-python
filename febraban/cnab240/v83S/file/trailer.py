# coding: utf-8

from ..row import Row
from ...characterType import numeric


class Trailer:

    def __init__(self):
        self.content = "00099999         000001000005                                                                                                                                                                                                                   "

    def setNumberOfLotsAndRegisters(self, num):
        structs = [
            (17, 23, 6, numeric, num),
            (23, 29, 6, numeric, 2+3*num),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0,   3,  3, numeric, bank.bankId),              # Código do banco debitado
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
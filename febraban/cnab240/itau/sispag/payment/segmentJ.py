# coding: utf-8

from datetime import date
from ....row import Row
from ....characterType import numeric, alphaNumeric


class SegmentJ:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (  7,   8,  1,      numeric,   "3"),         # TIPO DE REGISTRO
            (  8,  13,  5,      numeric,     1),          # INDEX DO REGISTRO
            ( 13,  14,  1, alphaNumeric,   "J"),         # CÓDIGO DE SEGMENTO
            ( 14,  17,  3,      numeric, "000"),       # TIPO DE MOVIMENTO
            (144, 152,  8,      numeric, date.today().strftime("%d%m%Y")),
            (114, 144, 23,      numeric,   "0"),
            (167, 182, 15,      numeric, "0"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBarCode(self, barCode):
        structs = [
            ( 17,  20,  3, numeric, barCode.bankId),
            ( 20,  21,  1, numeric, barCode.currency),
            ( 21,  22,  1, numeric, barCode.dac),
            ( 22,  26,  4, numeric, barCode.dueFactor),
            ( 26,  36, 10, numeric, barCode.amount),
            ( 36,  61, 25, numeric, barCode.freeField),
            ( 99, 114, 15, numeric, barCode.amount),                      # VALOR NOMINAL DO TÍTULO
            (152, 167, 15, numeric, barCode.amount),                      # VALOR DO PAGAMENTO
            ( 91,  99,  8, numeric, barCode.dueDate.strftime("%d%m%Y")),  # DATA DE VENCIMENTO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setScheduleDate(self, date):
        structs = [
            (144, 152,  8, numeric, date)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (182, 202, 20, alphaNumeric, identifier),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

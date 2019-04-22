from ....row import Row
from ....characterType import numeric, alphaNumeric


class SegmentR:

    def __init__(self):
        self.content = "0000000000000  000000000000000000000000000000000000000000000000000                                                                                                                                    00000000000000000 000000000000  0         "
        self.defaultValues()

    def defaultValues(self):
        structs = [
            ( 3,  7, 4,      numeric, "1"),
            ( 7,  8, 1,      numeric, "3"),
            (13, 14, 1, alphaNumeric, "R"),
            (15, 17, 2,      numeric, "01"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index)                                                # Indica index do lote
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFine(self, date, fine):
        structs = [
            (65,  66,  1,      numeric, "2"),                                        # 1-Valor em reais/ 2-Porcentagem
            (66,  74,  8, alphaNumeric, date),
            (74,  89, 13, alphaNumeric, fine)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)


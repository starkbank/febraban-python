from febraban.cnab240.row import Row
from febraban.cnab240.characterType import numeric


class Trailer:
    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (3, 7, 4, numeric, "9999"),
            (7, 8, 1, numeric, "9"),
            (29, 35, 6, numeric, "000000"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0,   3,  3, numeric, bank.bankId),   # Debit bank code
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setNumberOfLotsAndRegisters(self, sum, num):
        structs = [
            (17, 23, 6, numeric, num),
            (23, 29, 6, numeric, sum),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

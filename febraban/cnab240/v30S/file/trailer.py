from ..row import Row
from ...characterType import numeric


class Trailer:

    def __init__(self):
        self.content = "00000000         000000000000000000                                                                                                                                                                                                             "
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (3, 7, 4, numeric, "9999"),
            (7, 8, 1, numeric, "9"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setNumberOfLotsAndRegisters(self, num):
        structs = [
            (17, 23, 6, numeric, 1),
            (23, 29, 6, numeric, 4 + 2*num),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0,   3,  3, numeric, bank.bankId),    # Codigo do banco debitado
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
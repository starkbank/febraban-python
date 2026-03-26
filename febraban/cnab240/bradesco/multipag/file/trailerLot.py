from febraban.cnab240.row import Row
from febraban.cnab240.characterType import numeric


class TrailerLot:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            ( 3,   7,  4, numeric, "1"),
            ( 7,   8,  1, numeric, "5"),
            (41,  59, 18, numeric, "000000000000000000"),
            (59,  65, 6, numeric, "000000"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setLotNumberOfRegisters(self, num):
        structs = [
            (17,  23,  6, numeric, num),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSumOfValues(self, sum):
        structs = [
            (23, 41, 18, numeric, sum),         # Sum of values of lots
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSumOfValuesNonBarCodeTax(self, sum, otherSum):
        structs = [
            (23, 41, 18, numeric, sum),         # Sum of main values of lots
            (41, 59, 18, numeric, otherSum),    # Sum of other entities values of lots
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),    # Debit bank code
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)           # Indicates lot index
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

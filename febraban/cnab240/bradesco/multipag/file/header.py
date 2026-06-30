from febraban.cnab240.row import Row
from febraban.cnab240.characterType import alphaNumeric, alphaNumericRightAligned, numeric


class Header:
    def __init__(self, sequenceNumber=1):
        self.content = " " * 240
        self.defaultValues()
        self.setFileSequenceNumber(sequenceNumber)

    def defaultValues(self):
        structs = [
            ( 3,     7, 4, numeric, "0000"),      # Service lot
            ( 7,     8, 1, numeric, "0"),         # Record type
            ( 163, 166, 3, numeric, "089"),       # Layout version
            ( 142, 143, 1, numeric, "1"),         # 1 - Remittance / 2 - Return
            ( 166, 171, 5, numeric, "1600"),      # File recording density
            ( 157, 163, 6, numeric, "000000"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFileSequenceNumber(self, number):
        structs = [
            (157, 163, 6, numeric, number),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setGeneratedFileDate(self, datetime):
        structs = [
            (143, 151, 8, numeric, datetime.strftime("%d%m%Y")),   # File generation date
            (151, 157, 6, numeric, datetime.strftime("%H%M%S")),   # File generation time
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSender(self, user):
        structs = [
            (17,  18,  1,      numeric, "1" if len(user.identifier) == 11 else "2"),
            (18,  32, 14,      alphaNumericRightAligned, user.identifier),
            (72, 102, 30, alphaNumeric, user.name)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            ( 0,   3,  3, numeric, bank.bankId),
            (52,  57,  5, numeric, bank.branchCode),
            (58,  70, 12, numeric, bank.accountNumber),
            (70,  71,  1, alphaNumeric, bank.accountVerifier[:1]),
            (102,  132,  30, alphaNumeric, bank.bankName),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBankAgreement(self, agreement):
        structs = [
            (32, 52, 20, alphaNumeric, agreement),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

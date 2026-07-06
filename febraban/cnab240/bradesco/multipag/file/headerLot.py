from febraban.cnab240.row import Row
from febraban.cnab240.characterType import alphaNumeric, alphaNumericRightAligned, numeric

class HeaderLot:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (  3,   7, 4,      numeric, "1"),
            (  7,   8, 1,      numeric, "1"),
            (  8,   9, 1, alphaNumeric, "C"),
            (  9,   11, 2, numeric, "01"),
            ( 13,  16, 3,      numeric, "012"),
            ( 222,  224, 2,      numeric, "01"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSender(self, user):
        structs = [
            (17,  18,  1,      numeric, "1" if len(user.identifier) == 11 else "2"),
            (18,  32, 14,      alphaNumericRightAligned, user.identifier),
            (72, 102, 30, alphaNumeric, user.name)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setGeneratedFileDate(self, datetime):
        structs = [
            (191, 199, 8, numeric, datetime.strftime("%d%m%Y")),   # Recording date
            (199, 207, 8, numeric, datetime.strftime("%d%m%Y")),   # Credit date
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            ( 0,   3,  3, numeric, bank.bankId),
            (52,  57,  5, numeric, bank.branchCode),
            (58,  70, 12, numeric, bank.accountNumber),
            (70,  71,  1, numeric, bank.accountVerifier[:1]),
            (71,  72,  1, alphaNumeric, ""),
            (102,  132,  30, alphaNumeric, bank.bankName),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderAddress(self, address):
        structs = [
            (142, 192, 50, alphaNumeric, "%s %s %s" % (address.streetLine1, address.streetLine2, address.district)),
            (192, 212, 20, alphaNumeric, address.city),
            (212, 220,  8,      numeric, address.zipCode),
            (220, 222,  2, alphaNumeric, address.stateCode),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInfo(self, kind, method):
        structs = [
            ( 9, 11, 2, numeric, kind),
            (11, 13, 2, numeric, method)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBankAgreement(self, agreement):
        structs = [
            (32, 52, 20, alphaNumeric, agreement),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

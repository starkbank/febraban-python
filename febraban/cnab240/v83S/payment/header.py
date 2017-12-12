# coding: utf-8

from ..row import Row
from ...characterType import numeric, alphaNumeric


class Header:

    def __init__(self):
        self.content = "00000001C0000040 000000000000000                    00000 000000000000 0                                                                                                    00000                                   00000000                    "

    def setSender(self, user):
        structs = [
            (17,  18,  1,      numeric, "1" if len(user.identifier) == 11 else "2"),
            (18,  32, 14,      numeric, user.identifier),
            (72, 102, 30, alphaNumeric, user.name)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            ( 0,   3,  3, numeric, bank.bankId),
            (52,  57,  5, numeric, bank.branchCode),
            (58,  70, 12, numeric, bank.accountNumber),
            (71,  72,  1, numeric, bank.accountVerifier),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderAddress(self, address):
        structs = [
            (142, 172, 30, alphaNumeric, address.streetName),
            (172, 177,  5,      numeric, address.number),
            (192, 212, 20, alphaNumeric, address.city),
            (212, 220,  8,      numeric, address.zipcode),
            (220, 222,  2, alphaNumeric, address.state),
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
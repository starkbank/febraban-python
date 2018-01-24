# coding: utf-8

from ..row import Row
from ...characterType import numeric, alphaNumeric


class Header:

    def __init__(self):
        self.content = "00000000      081000000000000000                    00000 000000000000 0                                                                      10312201719400900000000000000                                                                     "

    def setGeneratedFileDate(self):
        import datetime
        now = datetime.datetime.now()
        structs = [
            (143, 151, 8, numeric, now.strftime("%d%m%Y")),   # Dia que o arquivo foi gerado
            (151, 157, 6, numeric, now.strftime("%H%M%S")),   # Horario que o arquivo foi gerado
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

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

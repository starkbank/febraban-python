# coding: utf-8

from ....row import Row
from ....characterType import numeric, alphaNumeric


class Header:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (   3,   8, 5, numeric, "0"),                          # Tipo de registro
            (  14,  17, 3, numeric, "81"),                         # Versão do Layout
            ( 142, 143, 1, numeric, "1"),                          # 1 - Remessa / 2 - Retorno
            ( 157, 166, 9, numeric, "0"),
            ( 166, 171, 5, numeric, "0"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setGeneratedFileDate(self, datetime):
        structs = [
            (143, 151, 8, numeric, datetime.strftime("%d%m%Y")),   # Dia que o arquivo foi gerado
            (151, 157, 6, numeric, datetime.strftime("%H%M%S")),   # Horario que o arquivo foi gerado
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

# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ..row import Row


class SegmentA:

    def __init__(self):
        self.content = "0000000300001A00000000000000 000000000000 0                                                  00000000REA000000000000000000000000000000                    00000000000000000000000                    00000000000000000000                       "

    def setSenderBank(self, bank):
        structs = [
            (0,   3,  3, numeric, bank.bankId),              # Código do banco debitado
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReceiver(self, user):
        structs = [
            ( 43,  73, 30,  alphaNumeric, user.name),        # Nome FAvorecido
            (203, 217, 14,       numeric, user.identifier),  # CPF/CNPJ Favorecido
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReceiverBank(self, bank):
        structs = [
            (20, 23,  3,  numeric, bank.bankId),             # Código do banco do Favorecido
            (23, 28,  5,  numeric, bank.branchCode),         # Agencia Favorecido
            (29, 41, 12,  numeric, bank.accountNumber),      # Conta Favorecido
            (42, 43,  1,  numeric, bank.accountVerifier),    # DAC FAvorecido
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmountInCents(self, amount):
        structs = [
            (119, 134, 15, numeric, amount)                  # Valor ao Favorecido
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)                        # Indica index do lote
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setScheduleDate(self, date):
        structs = [
            (93, 101, 8, numeric, date)                      # Data para transferencia
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInfo(self, reason):
        structs = [
            (217, 219, 2, alphaNumeric, reason)              # Motivo da transferencia
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (73, 93, 20, alphaNumeric, identifier)           # Id da empresa na transação
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
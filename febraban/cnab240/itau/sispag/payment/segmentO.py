# coding: utf-8
# Pagamento de Contas de Concessionárias e Tributos com código de barras # Página 28
from datetime import date
from febraban.cnab240.row import Row
from febraban.cnab240.characterType import numeric, alphaNumeric


class SegmentO:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (  3,   7,  4,      numeric,   "1"),
            (  7,   8,  1,      numeric,   "3"),         # Tipo de Registro
            (  8,  13,  5,      numeric,     1),         # N. sequencial de registro
            ( 13,  14,  1, alphaNumeric,   "O"),         # Código de Segmento
            ( 14,  17,  3,      numeric,   "0"),         # Tipo de Movimento
            (103, 106,  3, alphaNumeric, "REA"),         # Tipo da moeda
            (144, 159, 15,      numeric,   "0"),
            (136, 144,  8,      numeric,   date.today().strftime("%d%m%Y")),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDealerName(self, dealerName):                    # NOME DA CONCESSIONÁRIA / CONTRIBUINTE
        structs = [
            (65, 95, 30, alphaNumeric, dealerName),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDueDate(self, dueDate):
        structs = [
            (95, 103, 8, numeric, dueDate),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setCurrencyAmount(self, currencyAmount):            # QUANTIDADE DE MOEDA # NOTA 19
        structs = [
            (106, 121, 15, numeric, currencyAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmount(self, amount):
        structs = [
            (121, 136, 15, numeric, amount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBarCode(self, barCode, dac):                     # 17, 66 (Nota 18) Página 60
        structs = [
            (17,  18,  1, numeric, 8),
            (18,  19,  1, numeric, barCode.segmentId),      # IPTU = 1
            (19,  20,  1, numeric, 6),                      # 6 = Real
            (20,  21,  1, numeric, dac),                    # DAC (DV)
            (21,  32, 11, numeric, barCode.amount),         # IPTU amount
            (32,  36,  4, numeric, barCode.companyId),      # Identificacao empresa / orgao
            (36,  61, 25, numeric, barCode.freeField),      # Campo livre
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setLineNumber(self, lineNumber):
        structs = [
            (17,  65,  48, numeric, lineNumber),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBankIdentifier(self, identifier, dac):
        structs = [
            (40, 48, 8, numeric, identifier),                # Numero dado pelo Banco
            (48, 49, 1, numeric, dac)                        # Verificador do numero dado pelo Banco
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (174, 194, 20, alphaNumeric, identifier),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def ourNumber(self, ourNumber):                           # Nosso número: Nota 12
        structs = [                                           # Somente para cancelamento ou alteração
            (215, 230, 15, alphaNumeric, ourNumber),          # Retornado pelo Itau a cada pagamento
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setOccurences(self, occurrenceId):                    # Nota 8
        structs = [
            (230, 240, 10, alphaNumeric, occurrenceId)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

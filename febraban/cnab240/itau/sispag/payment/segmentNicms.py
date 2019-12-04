# coding: utf-8
# Página 32
# Pagamento de Tributos sem código de barras (GPS - Guia da Previdencia Social)
from datetime import date
from febraban.cnab240.row import Row
from febraban.cnab240.characterType import numeric, alphaNumeric


class SegmentNICMS:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            ( 3,   7,  4,      numeric,   "1"),
            ( 7,   8,  1,      numeric,   "3"),             # Tipo de Registro
            ( 8,  13,  5,      numeric,     1),             # N. sequencial de registro
            (13,  14,  1, alphaNumeric,   "N"),             # Código de Segmento
            (14,  17,  3,      numeric,   "0"),             # Tipo de Movimento
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

    def setTypeTaxId(self, id):
        structs = [
            (17, 19, 2, numeric, id)                       # IDENTIFICAÇÃO DO TRIBUTO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPaymentId(self, paymentId):
        structs = [
            (19, 23, 4, numeric, paymentId)                # CÓDIGO DE PAGAMENTO, NOTA 20
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdType(self, idType):
        structs = [
            (23, 24, 1, numeric, idType),                  # TIPO DE INSCRIÇÃO DO CONTRIBUINTE #1=CNPJ, 2=CEI
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxId(self, CNPJ):
        structs = [
            (24, 38, 14, numeric, CNPJ),                   # CPF ou CNPJ DO CONTRIBUINTE
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setStateRegistration(self, regId):
        structs = [
            (38, 50, 12, numeric, regId),                  # INSCRIÇÃO ESTADUAL
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDebtNum(self, debtNumber):
        structs = [
            (50, 63, 13, numeric, debtNumber),             # DIVIDA ATIVA/No ETIQUETA
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setRefMonth(self, refMonth):
        structs = [
            (63, 69, 6, numeric, refMonth),                # MÊS E ANO DA COMPETÊNCIA (MMAAAA)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setNotificationNumber(self, notificationNumber):
        structs = [
            (69, 82, 13, numeric, notificationNumber),     # NÚMERO PARCELA/NOTIFICAÇÃO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setRecipe(self, recipeAmount):
        structs = [
            (82, 96, 14, numeric, recipeAmount),                 # VALOR DA RECEITA
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInterest(self, interest):
        structs = [
            (96, 110, 14, numeric, interest),              # VALOR DO JUROS
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFine(self, fine):
        structs = [
            (110, 124, 14, numeric, fine),                 # VALOR DA MULTA
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmount(self, amount):
        structs = [
            (124, 138, 14, numeric, amount),               # VALOR DO PAGAMENTO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDueDate(self, dueDate):                         # DATA DE VENCIMENTO
        structs = [
            (138, 146,  8,   numeric, dueDate.strftime("%d%m%Y")),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPaymentDate(self):                                # DATA DE PAGAMENTO
        structs = [
            (146, 154,  8,      numeric,   date.today().strftime("%d%m%Y")),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxPayer(self, taxPayer):
        structs = [
            (165, 195, 30, alphaNumeric, taxPayer)          # NOME DO CONTRIBUINTE, NOTA 22
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (195, 215, 20, alphaNumeric, identifier)        # Id da empresa na transação
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

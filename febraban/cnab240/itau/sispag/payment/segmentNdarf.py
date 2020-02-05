# coding: utf-8
# Pagamento de Tributos sem código de barras (DARF NORMAL) # Página 32
from datetime import date
from ....row import Row
from ....characterType import numeric, alphaNumeric


class SegmentNDarf:

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

    def setTypeTaxId(self, id):
        structs = [
            (17, 19, 2, numeric, id)                       # IDENTIFICAÇÃO DO TRIBUTO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPaymentId(self, paymentId):
        structs = [
            (19, 23, 4, numeric, paymentId)                # CÓDIGO DA RECEITA (DARF)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSubscriptionId(self, subscriptionId):
        structs = [
            (23, 24, 1, numeric, subscriptionId),           # TIPO DE INSCRIÇÃO DO CONTRIBUINTE 1=CPF, 2=CNPJ
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxId(self, CNPJ):
        structs = [
            (24, 38, 14, numeric, CNPJ),                    # CNPJ do contribuinte
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setEvaluationDate(self, evalDate):                  # PERÍODO DE APURAÇÃO (DDMMAAAA)
        structs = [
            (38, 46,  8,   numeric, evalDate.strftime("%d%m%Y")),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReferenceNumber(self, refNum):                  # NÚMERO DE REFERÊNCIA
        structs = [
            (46, 63,  17,   numeric, refNum),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setMainAmount(self, mainAmount):
        structs = [
            (63, 77, 14, numeric, mainAmount),             # VALOR PRINCIPAL
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFineAmount(self, fineAmount):
        structs = [
            (77, 91, 14, numeric, fineAmount),             # VALOR DA MULTA
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInterestAmount(self, interestAmount):           # VALOR DOS JUROS/ENCARGOS
        structs = [
            (91, 105, 14, numeric, interestAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTotalAmount(self, amount):                      # VALOR TOTAL
        structs = [
            (105, 119, 14, numeric, amount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setdueDate(self, dueDate):                         # DATA DE VENCIMENTO
        structs = [
            (119, 127,  8,   numeric, dueDate.strftime("%d%m%Y")),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPaymentDate(self):                              # DATA DO PAGAMENTO
        structs = [
            (127, 135,  8,   numeric, date.today().strftime("%d%m%Y")),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxPayer(self, taxPayer):
        structs = [
            (165, 195, 30, alphaNumeric, taxPayer)          # NOME DO CONTRIBUINTE, NOTA 22
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (195, 215, 20, alphaNumeric, identifier)        # ID DA EMPRESA NA TRANSAÇÃO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

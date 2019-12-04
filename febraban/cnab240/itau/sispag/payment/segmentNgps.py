# coding: utf-8
# Pagamento de Tributos sem código de barras (GPS - Guia da Previdencia Social)
from datetime import date
from febraban.cnab240.row import Row
from febraban.cnab240.characterType import numeric, alphaNumeric


class SegmentNGPS:

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
            (19, 23, 4, numeric, paymentId)                # CÓDIGO DE PAGAMENTO, NOTA 20
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setRefMonth(self, refMonth):
        structs = [
            (23, 29, 6, numeric, refMonth),                # MÊS E ANO DA COMPETÊNCIA (MMAAAA)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxId(self, CNPJ):
        structs = [
            (29, 43, 14, numeric, CNPJ),                    # NIT, PIS, CEI ou CNPJ
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmount(self, amount):
        structs = [
            (43, 57, 14, numeric, amount),                  # VALOR PREVISTO DO PAGAMENTO DO INSS
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setOtherAmount(self, otherAmount):                  # VALOR DE OUTRAS ENTIDADES
        structs = [
            (57, 71, 14, numeric, otherAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setActualAmount(self, actualAmount):                # VALOR ATUALIZAÇÃO MONETÁRIA
        structs = [
            (71, 85, 14, numeric, actualAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setCollectedAmount(self, collectedAmount):          # VALOR ARRECADADO
        structs = [
            (85, 99, 14, numeric, collectedAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setRaisedDate(self):                                # DATA DA ARRECADAÇÃO/ EFETIVAÇÃO DO PAGAMENTO
        structs = [
            (99, 107,  8,      numeric,   date.today().strftime("%d%m%Y")),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setCompanyInfo(self, info=None):                    # INFORMAÇÕES COMPLEMENTARES, NOTA 21
        structs = [
            (115, 165, 50, alphaNumeric, info),
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

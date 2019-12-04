# coding: utf-8
# Pagamento de FGTS com código de barras # Página 32
from datetime import date
from febraban.cnab240.row import Row
from febraban.cnab240.characterType import numeric, alphaNumeric


class SegmentNFGTS:

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
            (17, 19, 2, numeric, id)                       # IDENTIFICAÇÃO DO TRIBUTO = 11
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPaymentId(self, paymentId):
        structs = [
            (19, 23, 4, numeric, paymentId)                # CÓDIGO DA RECEITA
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxType(self, CNPJ):
        structs = [
            (23, 24, 1, numeric, CNPJ),                    # CNPJ=1
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxId(self, CNPJ):
        structs = [
            (24, 38, 14, numeric, CNPJ),                   # CNPJ DO CONTRIBUINTE
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBarcode(self, barcode):                         # CODIGO DE BARRAS FGTS
        structs = [
            (38, 86, 48, alphaNumeric, barcode),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFgtsIdentifier(self, identifier):
        structs = [
            (86, 102, 16, numeric, identifier)             # IDENTIFICADOR DO FGTS
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmount(self, amount):
        structs = [
            (151, 165, 14, numeric, amount),               # VALOR DO PAGAMENTO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setLacre(self, lacre):                             # LACRE DE CONECTIVIDADE SOCIAL
        structs = [
            (102, 111, 9, numeric, lacre),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDigLacre(self, digLacre):                       # DIGITO DO LACRE DE CONECTIVIDADE SOC.
        structs = [
            (111, 113, 2, numeric, digLacre),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPaymentDate(self):                              # DATA DO PAGAMENTO
        structs = [
            (143, 151,  8,      numeric,   date.today().strftime("%d%m%Y")),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxPayer(self, taxPayer):
        structs = [
            (113, 143, 30, alphaNumeric, taxPayer)         # NOME DO CONTRIBUINTE
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (195, 215, 20, alphaNumeric, identifier)       # Id da empresa na transação
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
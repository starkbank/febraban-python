# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ...row import RowElement, Row


class Header(Row):

    def __init__(self):
        Row.__init__(self)
        self.elements = [
            RowElement(
                index=0,
                description="N.o DO BANCO NA CÂMARA DE COMPENSAÇÃO",
                numberOfCharacters=3,
                charactersType=numeric
            ),
            RowElement(
                index=1,
                description="LOTE DE SERVIÇO",
                numberOfCharacters=4,
                charactersType=numeric
            ),
            RowElement(
                index=2,
                description="REGISTRO HEADER DE LOTE",
                numberOfCharacters=1,
                charactersType=numeric,
                value="1"
            ),
            RowElement(
                index=3,
                description="TIPO DE OPERAÇÃO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
                value="R"
            ),
            RowElement(
                index=4,
                description="IDENTIFICAÇÃO DO TIPO DE SERVIÇO",
                numberOfCharacters=2,
                charactersType=numeric,
                value="01"
            ),
            RowElement(
                index=5,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=2,
                charactersType=numeric,
            ),
            RowElement(
                index=6,
                description="N.o DA VERSÃO DO LAYOUT DO LOTE",
                numberOfCharacters=3,
                charactersType=numeric,
                value="030"
            ),
            RowElement(
                index=7,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=8,
                description="TIPO DE INSCRIÇÃO DA EMPRESA",
                numberOfCharacters=1,
                charactersType=numeric
            ),
            RowElement(
                index=9,
                description="N.o DE INSCRIÇÃO DA EMPRESA",
                numberOfCharacters=15,
                charactersType=numeric
            ),
            RowElement(
                index=10,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=20,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=11,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=12,
                description="AGÊNCIA MANTENEDORA DA CONTA",
                numberOfCharacters=4,
                charactersType=numeric
            ),
            RowElement(
                index=13,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=14,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=7,
                charactersType=numeric,
            ),
            RowElement(
                index=15,
                description="NÚMERO DA CONTA CORRENTE",
                numberOfCharacters=5,
                charactersType=numeric
            ),
            RowElement(
                index=16,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=17,
                description="DÍGITO DE AUTO-CONFERÊNCIA AG./CONTA EMPRESA",
                numberOfCharacters=1,
                charactersType=numeric
            ),
            RowElement(
                index=18,
                description="NOME DA EMPRESA",
                numberOfCharacters=30,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=19,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=80,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=20,
                description="NÚMERO SEQUENCIAL DO ARQUIVO RETORNO",
                numberOfCharacters=8,
                charactersType=numeric
            ),
            RowElement(
                index=21,
                description="DATA DE GRAVAÇÃO DO ARQUIVO",
                numberOfCharacters=8,
                charactersType=numeric #DDMMAAAA
            ),
            RowElement(
                index=22,
                description="DATA DO CRÉDITO",
                numberOfCharacters=8,
                charactersType=numeric #DDMMAAAA
            ),
            RowElement(
                index=23,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=33,
                charactersType=alphaNumeric
            )
        ]

    def setSender(self, user):
        self.elements[8].setValue("1" if len(user.identifier) == 11 else "2")  # 1 - CPF/ 2 - CNPJ
        self.elements[9].setValue(user.identifier)
        self.elements[18].setValue(user.name)

    def setSenderBank(self, bank):
        self.elements[0].setValue(bank.bankId)
        self.elements[12].setValue(bank.branchCode)
        self.elements[15].setValue(bank.accountNumber)
        self.elements[17].setValue(bank.accountVerifier)

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)

    def setIssueDate(self, date):
        self.elements[21].setValue(date)
        self.elements[22].setValue(date)
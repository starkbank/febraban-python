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
                charactersType=numeric,
            ),
            RowElement(
                index=2,
                description="REGISTRO HEADER DE ARQUIVO",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=3,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=9,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=4,
                description="TIPO DE INSCRIÇÃO DA EMPRESA",
                numberOfCharacters=1,
                charactersType=numeric
            ),
            RowElement(
                index=5,
                description="N.o DE INSCRIÇÃO DA EMPRESA",
                numberOfCharacters=14,
                charactersType=numeric
            ),
            RowElement(
                index=6,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=20,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=7,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=8,
                description="AGÊNCIA MANTENEDORA DA CONTA",
                numberOfCharacters=4,
                charactersType=numeric
            ),
            RowElement(
                index=9,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=10,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=7,
                charactersType=numeric,
            ),
            RowElement(
                index=11,
                description="NÚMERO DA CONTA CORRENTE DA EMPRESA",
                numberOfCharacters=5,
                charactersType=numeric
            ),
            RowElement(
                index=12,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=13,
                description="DÍGITO DE AUTO-CONFERÊNCIA AG./CONTA EMPRESA",
                numberOfCharacters=1,
                charactersType=numeric
            ),
            RowElement(
                index=14,
                description="NOME POR EXTENSO DA EMPRESA 'MÃE'",
                numberOfCharacters=30,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=15,
                description="NOME POR EXTENSO DO BANCO COBRADOR",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
                value="BANCO ITAU SA"
            ),
            RowElement(
                index=16,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=17,
                description="CÓDIGO REMESSA / RETORNO",
                numberOfCharacters=1,
                charactersType=numeric,
                value="1" #1-Remessa, #2-Retorno
            ),
            RowElement(
                index=18,
                description="DATA DE GERAÇÃO DO ARQUIVO",
                numberOfCharacters=8,
                charactersType=numeric #DDMMAAAA
            ),
            RowElement(
                index=19,
                description="HORA DE GERAÇÃO DO ARQUIVO",
                numberOfCharacters=6,
                charactersType=numeric, #HHMMSS
            ),
            RowElement(
                index=20,
                description="NÚMERO SEQUENCIAL DO ARQUIVO RETORNO",
                numberOfCharacters=6,
                charactersType=numeric
            ),
            RowElement(
                index=21,
                description="N.o DA VERSÃO DO LAYOUT DO ARQUIVO",
                numberOfCharacters=3,
                charactersType=numeric,
                value="030"
            ),
            RowElement(
                index=22,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                index=23,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=54,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=24,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                index=25,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=12,
                charactersType=alphaNumeric,
            )
        ]

    def setUser(self, user):
        self.elements[4].setValue("1" if len(user.identifier) == 11 else "2")  # 1 - CPF/ 2 - CNPJ
        self.elements[5].setValue(user.identifier)
        self.elements[14].setValue(user.name)

    def setUserBank(self, bank):
        self.elements[0].setValue(bank.bankId)
        self.elements[8].setValue(bank.branchCode)
        self.elements[11].setValue(bank.accountNumber)
        self.elements[13].setValue(bank.accountVerifier)
        self.elements[15].setValue(bank.bankName)

    def update(self):
        import datetime
        now = datetime.datetime.now()
        self.elements[18].setValue(now.strftime("%d%m%Y"))  # Dia que o arquivo foi gerado
        self.elements[19].setValue(now.strftime("%H%M%S"))  # Horario que o arquivo foi gerado

    def setReturnFileIdentifier(self, id):
        self.elements[20].setValue(id)

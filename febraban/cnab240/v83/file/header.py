
# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ...row import RowElement, Row


class Header(Row):

    def __init__(self):
        Row.__init__(self)
        self.elements = [
            RowElement(
                index=0,
                description="Banco - Código do Banco na Compensação",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                index=1,
                description="Lote - Lote de Serviço",
                numberOfCharacters=4,
                charactersType=numeric,
                value='0000'
            ),
            RowElement(
                index=2,
                description="Registro - Tipo de Registro",
                numberOfCharacters=1,
                charactersType=numeric,
                value='0'
            ),
            RowElement(
                index=3,
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=6,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=4,
                description="No DA VERSÃO DO LAYOUT DO ARQUIVO",
                numberOfCharacters=3,
                charactersType=numeric,
                value='081'
            ),
            RowElement(
                index=5,
                description="Empresa - Tipo de Inscrição da Empresa",
                numberOfCharacters=1,
                charactersType=numeric,
                value='2' # 1-CPF, 2-CNPJ
            ),
            RowElement(
                index=6,
                description="Empresa - Número de Inscrição da Empresa",
                numberOfCharacters=14,
                charactersType=numeric,
            ),
            RowElement(
                index=7,
                description="Empresa - Código do Convênio no Banco",
                numberOfCharacters=20,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=8,
                description="Empresa - Agência Mantenedora da Conta",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                index=9,
                description="Empresa - Dígito Verificador da Agência",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=10,
                description="Empresa - Número da Conta Corrente",
                numberOfCharacters=12,
                charactersType=numeric,
            ),
            RowElement(
                index=11,
                description="Empresa - Dígito Verificador da Conta",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=12,
                description="Empresa - Dac da agencia/conta debitada",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=13,
                description="Empresa - Nome da Empresa",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=14,
                description="Nome do Banco",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=15,
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=16,
                description="Arquivo - Código Remessa / Retorno",
                numberOfCharacters=1,
                charactersType=numeric,
                value="1" #1- REMESSA, 2- RETORNO
            ),
            RowElement(
                index=17,
                description="Arquivo - Data de Geração do Arquivo",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                index=18,
                description="Arquivo - Hora de Geração do Arquivo",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                index=19,
                description="Complemento de Registro",
                numberOfCharacters=9,
                charactersType=numeric,
            ),
            RowElement(
                index=20,
                description="Arquivo - Densidade de Gravação do Arquivo",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                index=21,
                description="Complemento de Registro",
                numberOfCharacters=69,
                charactersType=alphaNumeric,
            )
        ]

    def update(self):
        import datetime
        now = datetime.datetime.now()
        self.elements[17].setValue(now.strftime("%d%m%Y"))  # Dia que o arquivo foi gerado
        self.elements[18].setValue(now.strftime("%H%M%S"))  # Horario que o arquivo foi gerado

    def setUser(self, user):
        self.elements[6].setValue(user.identifier)
        self.elements[13].setValue(user.name)

    def setUserBank(self, bank):
        self.elements[0].setValue(bank.bankId)
        self.elements[8].setValue(bank.branchCode)
        self.elements[10].setValue(bank.accountNumber)
        self.elements[12].setValue(bank.accountVerifier)

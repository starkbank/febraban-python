# coding: utf-8

from cnab240.row import RowElement, numeric, alphaNumeric, Row


class Header(Row):

    def __init__(self):
        Row.__init__(self)
        self.elements = [
            RowElement(
                description="Banco - Código do Banco na Compensação",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                description="Lote - Lote de Serviço",
                numberOfCharacters=4,
                charactersType=numeric,
            ),
            RowElement(
                description="Registro - Tipo de Registro",
                numberOfCharacters=1,
                charactersType=numeric,
                value='0'
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=9,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Empresa - Tipo de Inscrição da Empresa",
                numberOfCharacters=1,
                charactersType=numeric,
                value='2'
            ),
            RowElement(
                description="Empresa - Número de Inscrição da Empresa",
                numberOfCharacters=14,
                charactersType=numeric,
            ),
            RowElement(
                description="Empresa - Código do Convênio no Banco",
                numberOfCharacters=20,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Empresa - Agência Mantenedora da Conta",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                description="Empresa - Dígito Verificador da Agência",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Empresa - Número da Conta Corrente",
                numberOfCharacters=12,
                charactersType=numeric,
            ),
            RowElement(
                description="Empresa - Dígito Verificador da Conta",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Empresa - Dígito Verificador da Ag/Conta",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Empresa - Nome da Empresa",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Nome do Banco",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Arquivo - Código Remessa / Retorno",
                numberOfCharacters=1,
                charactersType=numeric,
                value="1"
            ),
            RowElement(
                description="Arquivo - Data de Geração do Arquivo",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                description="Arquivo - Hora de Geração do Arquivo",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                description="Arquivo - Número Seqüencial do Arquivo",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                description="Arquivo - No da Versão do Layout do Arquivo",
                numberOfCharacters=3,
                charactersType=numeric,
                value="103"
            ),
            RowElement(
                description="Arquivo - Densidade de Gravação do Arquivo",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                description="Reservado Banco - Para Uso Reservado do Banco",
                numberOfCharacters=20,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Reservado Empresa - Para Uso Reservado da Empresa",
                numberOfCharacters=20,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=29,
                charactersType=alphaNumeric,
            ),
        ]

    def update(self):
        import datetime
        now = datetime.datetime.now()
        self.elements[16].setValue(now.strftime("%d%m%Y"))  # Dia que o arquivo foi gerado
        self.elements[17].setValue(now.strftime("%H%M%S"))  # Horario que o arquivo foi gerado

    def setUser(self, user):
        self.elements[0].setValue(user.bankId)
        self.elements[5].setValue(user.identifier)
        self.elements[7].setValue(user.branchCode)
        self.elements[9].setValue(user.accountNumber)
        self.elements[10].setValue(user.accountVerifier)
        self.elements[12].setValue(user.name)
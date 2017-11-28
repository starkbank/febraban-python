# coding: utf-8

from cnab240.row import RowElement, numeric, alphaNumeric, Row


class Header(Row):

    def __init__(self):
        Row.__init__(self)
        self.elements = [
            RowElement(
                description="Controle - Banco - Código do Banco na Compensação",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                description="Controle - Lote - Lote de Serviço",
                numberOfCharacters=4,
                charactersType=numeric,
            ),
            RowElement(
                description="Controle - Registro - Tipo de Registro",
                numberOfCharacters=1,
                charactersType=numeric,
                value="1"
            ),
            RowElement(
                description="Serviço - Tipo da Operação",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
                value="C"
            ),
            RowElement(
                description="Serviço - Tipo do Serviço",
                numberOfCharacters=2,
                charactersType=numeric
            ),
            RowElement(
                description="Serviço - Forma de Lançamento",
                numberOfCharacters=2,
                charactersType=numeric,
            ),
            RowElement(
                description="Serviço - No da Versão do Layout do Lote",
                numberOfCharacters=3,
                charactersType=numeric,
                value="046"
            ),
            RowElement(
                description="CNAB - Uso Exclusivo da FEBRABAN/CNAB",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Empresa - Tipo de Inscrição da Empresa",
                numberOfCharacters=1,
                charactersType=numeric,
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
                description="Informação 1 - Mensagem",
                numberOfCharacters=40,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Endereço da Empresa - Logradouro",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Endereço da Empresa - Número",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                description="Endereço da Empresa - Complemento",
                numberOfCharacters=15,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Endereço da Empresa - Cidade",
                numberOfCharacters=20,
                charactersType=alphaNumeric
            ),
            RowElement(
                description="Endereço da Empresa - CEP",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                description="Endereço da Empresa - Sigla do Estado",
                numberOfCharacters=2,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Indicativo da Forma de Pagamento do Serviço",
                numberOfCharacters=2,
                charactersType=numeric,
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=6,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Ocorrências - Códigos das Ocorrências p/ Retorno",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            )
        ]

    def setSender(self, user):
        self.elements[0].setValue(user.bankId)
        self.elements[9].setValue(user.identifier)
        self.elements[11].setValue(user.branchCode)
        self.elements[13].setValue(user.accountNumber)
        self.elements[14].setValue(user.accountVerifier)
        self.elements[16].setValue(user.name)

    def setSenderAddress(self, address):
        self.elements[18].setValue(address.streetName)
        self.elements[19].setValue(address.number)
        self.elements[21].setValue(address.city)
        self.elements[22].setValue(address.zipcode)
        self.elements[24].setValue(address.state)

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)

    def setInfo(self, kind, method):
        self.elements[4].setValue(kind)
        self.elements[5].setValue(method)
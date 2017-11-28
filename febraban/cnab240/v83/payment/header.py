
# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ...row import RowElement, Row


class Header(Row):

    def __init__(self):
        Row.__init__(self)
        self.elements = [
            RowElement(
                index=0,
                description="Controle - Banco - Código do Banco na Compensação",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                index=1,
                description="Controle - Lote - Lote de Serviço",
                numberOfCharacters=4,
                charactersType=numeric,
            ),
            RowElement(
                index=2,
                description="Controle - Registro - Tipo de Registro",
                numberOfCharacters=1,
                charactersType=numeric,
                value="1"
            ),
            RowElement(
                index=3,
                description="Serviço - Tipo da Operação",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
                value="C" # C-Crédito
            ),
            RowElement(
                index=4,
                description="Serviço - Tipo do Pagamento",
                numberOfCharacters=2,
                charactersType=numeric
            ),
            RowElement(
                index=5,
                description="Serviço - Forma de Pagamento",
                numberOfCharacters=2,
                charactersType=numeric,
            ),
            RowElement(
                index=6,
                description="Serviço - No da Versão do Layout do Lote",
                numberOfCharacters=3,
                charactersType=numeric,
                value="040"
            ),
            RowElement(
                index=7,
                description="CNAB - Uso Exclusivo da FEBRABAN/CNAB",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=8,
                description="Empresa - Tipo de Inscrição da Empresa",
                numberOfCharacters=1,
                charactersType=numeric,
                value='2' #1-CPF, #2-CNPJ
            ),
            RowElement(
                index=9,
                description="Empresa - Número de Inscrição da Empresa",
                numberOfCharacters=14,
                charactersType=numeric,
            ),
            RowElement(
                index=10,
                description="Empresa - Identificação do lançamento no extrato do favorecido",
                numberOfCharacters=4,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=11,
                description="Complemento de Registro",
                numberOfCharacters=16,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=12,
                description="Empresa - Agência Mantenedora da Conta",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                index=13,
                description="Empresa - Dígito Verificador da Agência",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=14,
                description="Empresa - Número da Conta Corrente",
                numberOfCharacters=12,
                charactersType=numeric,
            ),
            RowElement(
                index=15,
                description="Empresa - Dígito Verificador da Conta",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=16,
                description="Empresa - DAC da agencia/conta debitada",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=17,
                description="Empresa - Nome da Empresa",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=18,
                description="Finalidade do payment do lote",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=19,
                description="Complemento Historico C/C Debitada",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=20,
                description="Endereço da Empresa - Logradouro",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=21,
                description="Endereço da Empresa - Número",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                index=22,
                description="Endereço da Empresa - Complemento",
                numberOfCharacters=15,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=23,
                description="Endereço da Empresa - Cidade",
                numberOfCharacters=20,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=24,
                description="Endereço da Empresa - CEP",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                index=25,
                description="Endereço da Empresa - Sigla do Estado",
                numberOfCharacters=2,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=26,
                description="Complemento de Registro",
                numberOfCharacters=8,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=27,
                description="Ocorrências - Códigos das Ocorrências p/ Retorno",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            )
        ]

    def setSender(self, user):
        self.elements[9].setValue(user.identifier)
        self.elements[17].setValue(user.name)

    def setSenderBank(self, bank):
        self.elements[0].setValue(bank.bankId)
        self.elements[12].setValue(bank.branchCode)
        self.elements[14].setValue(bank.accountNumber)
        self.elements[16].setValue(bank.accountVerifier)

    def setSenderAddress(self, address):
        self.elements[20].setValue(address.streetName)
        self.elements[21].setValue(address.number)
        self.elements[23].setValue(address.city)
        self.elements[24].setValue(address.zipcode)
        self.elements[25].setValue(address.state)

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)

    def setInfo(self, kind, method):
        self.elements[4].setValue(kind)
        self.elements[5].setValue(method)
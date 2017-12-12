
# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ...row import RowElement, Row


class SegmentA(Row):

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
                description="Controle - Registro detalhe de Lote",
                numberOfCharacters=1,
                charactersType=numeric,
                value="3"
            ),
            RowElement(
                index=3,
                description="Serviço - No Seqüencial do Registro no Lote",
                numberOfCharacters=5,
                charactersType=numeric,
                value="1"
            ),
            RowElement(
                index=4,
                description="Serviço - Código de Segmento do Reg. Detalhe",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
                value="A"
            ),
            RowElement(
                index=5,
                description="Serviço - Tipo de Movimento",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                index=6,
                description="Favorecido - Código da Câmara Centralizadora",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                index=7,
                description="Favorecido - Código do Banco do Favorecido",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            #Note 11 - Start
            RowElement(
                index=8,
                description="Número de Agência Conta Creditada",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                index=9,
                description="Complemento de Registro",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=10,
                description="Número de Conta Corrente Credita",
                numberOfCharacters=12,
                charactersType=numeric,
            ),
            RowElement(
                index=11,
                description="Complemento de Registro",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=12,
                description="DAC - Agencia cretitada",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            #Note 11 - End
            RowElement(
                index=13,
                description="Favorecido - Nome do Favorecido",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=14,
                description="Crédito - No do Docum. Atribuído p/ Empresa",
                numberOfCharacters=20,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=15,
                description="Crédito - Data prevista para Pagamento",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                index=16,
                description="Crédito - Tipo da Moeda",
                numberOfCharacters=3,
                charactersType=alphaNumeric,
                value="REA" #REA ou 009
            ),
            RowElement(
                index=17,
                description="Crédito - Código ISPB - Identificação da Instituição para o SPB",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                index=18,
                description="Crédito - Complemento de Registro",
                numberOfCharacters=7,
                charactersType=numeric,
            ),
            RowElement(
                index=19,
                description="Crédito - Valor do Pagamento",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                index=20,
                description="Crédito - No do Docum. Atribuído pelo Banco",
                numberOfCharacters=15,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=21,
                description="Crédito - Complemente de Registro",
                numberOfCharacters=5,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=22,
                description="Crédito - Data Real da Efetivação Pagto",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                index=23,
                description="Crédito - Valor Real da Efetivação do Pagto",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                index=24,
                description="Finalidade Detalhe - Informação Complementar para Hist de C/C",
                numberOfCharacters=18,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=25,
                description="Complemento de Registro",
                numberOfCharacters=2,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=26,
                description="N0 do DOC/TED/OP no Retorno",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                index=27,
                description="No de Inscrição do Favorecido (CPF)/CNPJ",
                numberOfCharacters=14,
                charactersType=numeric,
            ),
            RowElement(
                index=28,
                description="Finalidade do DOC e Status do funcionario na Empresa",
                numberOfCharacters=2,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=29,
                description="Finalidade da TED",
                numberOfCharacters=5,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=30,
                description="Complemento de Registro",
                numberOfCharacters=5,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=31,
                description="Aviso ao favorecido",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=32,
                description="Ocorrências - Códigos das Ocorrências p/ Retorno",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            )
        ]

    def amountInCents(self):
        return self.elements[19].value()

    def setSenderBank(self, bank):
        self.elements[0].setValue(bank.bankId)       # Código do banco debitado

    def setReceiver(self, user):
        self.elements[13].setValue(user.name)             # Nome FAvorecido
        self.elements[27].setValue(user.identifier)       # CPF/CNPJ Favorecido

    def setReceiverBank(self, bank):
        self.elements[7].setValue(bank.bankId)            # Código do banco do Favorecido
        self.elements[8].setValue(bank.branchCode)        # Agencia Favorecido
        self.elements[10].setValue(bank.accountNumber)    # Conta Favorecido
        self.elements[12].setValue(bank.accountVerifier)  # DAC FAvorecido

    def setAmountInCents(self, amount):
        self.elements[19].setValue(amount)                # Valor ao Favorecido

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)                  # Indica index do lote

    def setScheduleDate(self, date):
        self.elements[15].setValue(date)                  # Data para transferencia

    def setInfo(self, reason):
        self.elements[28].setValue(reason)                # Motivo da transferencia

    def setIdentifier(self, identifier):
        self.elements[14].setValue(identifier)            # Identifier da empresa na transação
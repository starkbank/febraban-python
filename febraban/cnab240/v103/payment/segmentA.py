# coding: utf-8

from cnab240.row import RowElement, numeric, alphaNumeric, Row


class SegmentA(Row):

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
                value="3"
            ),
            RowElement(
                description="Serviço - No Seqüencial do Registro no Lote",
                numberOfCharacters=5,
                charactersType=numeric
            ),
            RowElement(
                description="Serviço - Código de Segmento do Reg. Detalhe",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
                value="A"
            ),
            RowElement(
                description="Serviço - Tipo de Movimento",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                description="Serviço - Código da Instrução p/ Movimento",
                numberOfCharacters=2,
                charactersType=numeric,
            ),
            RowElement(
                description="Favorecido - Código da Câmara Centralizadora",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                description="Favorecido - Código do Banco do Favorecido",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                description="Favorecido - Agência Mantenedora da Conta",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                description="Favorecido - Dígito Verificador da Agência",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Favorecido - Número da Conta Corrente",
                numberOfCharacters=12,
                charactersType=numeric,
            ),
            RowElement(
                description="Favorecido - Dígito Verificador da Conta",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Favorecido - Dígito Verificador da Ag/Conta",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Favorecido - Nome do Favorecido",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Crédito - No do Docum. Atribuído p/ Empresa",
                numberOfCharacters=20,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Crédito - Data do Pagamento",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                description="Crédito - Tipo da Moeda",
                numberOfCharacters=3,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Crédito - Quantidade da Moeda",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                description="Crédito - Valor do Pagamento",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                description="Crédito - No do Docum. Atribuído pelo Banco",
                numberOfCharacters=20,
                charactersType=alphaNumeric
            ),
            RowElement(
                description="Crédito - Data Real da Efetivação Pagto",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                description="Crédito - Valor Real da Efetivação do Pagto",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                description="Informação 2 - Outras Informações Vide formatação em G031 para identificação de Deposito Judicial e Pgto.Salários de servidores pelo SIAPE",
                numberOfCharacters=40,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Código Finalidade Doc",
                numberOfCharacters=2,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Código Finalidade TED",
                numberOfCharacters=5,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Código Finalidade Complementar",
                numberOfCharacters=2,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN/CNAB",
                numberOfCharacters=3,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Aviso ao Favorecido",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                description="Ocorrências - Códigos das Ocorrências p/ Retorno",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            )
        ]

    def amountInCents(self):
        return self.elements[19].value()

    def setSender(self, user):
        self.elements[0].setValue(user.bankId)            # Código do banco debitado

    def setReceiver(self, user):
        self.elements[8].setValue(user.bankId)            # Código do banco do Favorecido
        self.elements[9].setValue(user.branchCode)        # Agencia Favorecido
        self.elements[11].setValue(user.accountNumber)    # Conta Favorecido
        self.elements[12].setValue(user.accountVerifier)  # DAC FAvorecido
        self.elements[14].setValue(user.name)             # Nome FAvorecido
        self.elements[15].setValue(user.identifier)       # CPF/CNPJ Favorecido

    def setAmountInCents(self, amount):
        self.elements[19].setValue(amount)                # Valor ao Favorecido

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)                  # Indica index do lote

    def setScheduleDate(self, date):
        self.elements[16].setValue(date)                  # Data para transferencia

    def setInfo(self, reason):
        self.elements[25].setValue(reason)                # Motivo da transferencia
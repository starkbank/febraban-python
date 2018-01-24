from ...characterType import numeric, alphaNumeric
from ..row import Row


class SegmentP:

    def __init__(self):
        self.content = "0000000000000  0000000 000000000000 0000000000000        00000               0000000000000000000000000000000A00000000000000000000000000000000000000000000000000000000000000000000000000000000000000                         0000000000000000000 "
        self.defaultValues()

    def amountInCents(self):
        return int(self.content[85:100])

    def defaultValues(self):
        structs = [
            (  3,   7, 4,      numeric, "1"),
            (  7,   8, 1,      numeric, "3"),
            ( 13,  14, 1, alphaNumeric, "P"),
            ( 15,  17, 2,      numeric, "01"),
            ( 37,  40, 3,      numeric, "109"),               # Numero da Carteira de Cobranca
            (106, 108, 2,      numeric, "99"),                # Especie do Titulo: 99 = Real
            (108, 109, 1, alphaNumeric, "A"),                 # Aceite: A = Sim, N = Nao
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (  0,   3,  3,      numeric, bank.bankId),
            ( 18,  22,  4,      numeric, bank.branchCode),
            ( 23,  35, 12,      numeric, bank.accountNumber),
            ( 36,  37,  1,      numeric, bank.accountVerifier)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index)                        # Indica index do lote
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (62, 72, 10, alphaNumeric, identifier)           # Codigo interno da empresa. Ex: Num de nota fiscal
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBankIdentifier(self, identifier, dac):
        structs = [
            (40, 48, 8, numeric, identifier),                # Numero dado pelo Banco
            (48, 49, 1, numeric, dac)                        # Verificador do numero dado pelo Banco
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmountInCents(self, amount):
        structs = [
            (85, 100, 15, numeric, amount),                  # Valor do Boleto
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setExpirationDate(self, date):
        structs = [
            (77, 85, 8, numeric, date),                      # Data de vencimento do boleto
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIssueDate(self, date):
        structs = [
            (109, 117, 8, numeric, date),                    # Data de emissao do boleto
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
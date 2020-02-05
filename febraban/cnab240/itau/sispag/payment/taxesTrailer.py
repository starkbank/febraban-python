# coding: utf-8
# Pagamento de Tributos sem código de barras e FGTS-GRF/GRRF/GRDE com código de barras
from ....characterType import numeric
from ....row import Row


class TaxesTrailer:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (7,   8,  1, numeric, "5"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),                   # CÓDIGO BANCO NA COMPENSAÇÃO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)                          # LOTE DE SERVIÇO
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setLotNumberOfRegisters(self, count):                  # QTDE REGISTROS DO LOTE
        structs = [
            (17,  23,  6, numeric, count),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmountInCents(self, amount):
        structs = [
            (23, 37, 14, numeric, amount),                     # SOMA VALOR PRINCIPAL DOS PGTOS DO LOTE # NOTA 17
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSumOthersAmountInCents(self, otherAmount):
        structs = [
            (37, 51, 14, numeric, otherAmount),                # SOMA VALORES DE OUTRAS ENTIDADES DO LOTE
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setActualAmountInCents(self, actualAmount):
        structs = [
            (51, 65, 14, numeric, actualAmount),               # SOMA VALORES ATUALIZ. MONET/MULTA/MORA
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSumAmountInCents(self, sumAmount):
        structs = [
            (65, 79, 14, numeric, sumAmount),                  # SOMA VALOR DOS PAGAMENTOS DO LOTE
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

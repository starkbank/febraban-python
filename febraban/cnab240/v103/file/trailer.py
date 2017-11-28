# coding: utf-8

from cnab240.row import RowElement, numeric, alphaNumeric, Row


class Trailer(Row):

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
                value="9999"
            ),
            RowElement(
                description="Registro - Tipo de Registro",
                numberOfCharacters=1,
                charactersType=numeric,
                value="9"
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=9,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Totais - Quantidade de Lotes do Arquivo",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                description="Totais - Quantidade de Registros do Arquivo",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                description="Totais - Qtde de Contas p/ Conc. (Lotes)",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=205,
                charactersType=alphaNumeric,
            ),
        ]

    def update(self, lots):
        self.setNumberOfLotes(num=len(lots))
        self.setNumberOfRegisters(num=2+3*len(lots))

    def setUser(self, user):
        self.elements[0].setValue(user.bankId)

    def setNumberOfLotes(self, num):
        self.elements[4].setValue(num)

    def setNumberOfRegisters(self, num):
        self.elements[5].setValue(num)

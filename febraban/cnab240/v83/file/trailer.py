
# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ...row import RowElement, Row


class Trailer(Row):

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
                value="9999"
            ),
            RowElement(
                index=2,
                description="Registro - Tipo de Registro",
                numberOfCharacters=1,
                charactersType=numeric,
                value="9"
            ),
            RowElement(
                index=3,
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=9,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=4,
                description="Totais - Quantidade de Lotes do Arquivo",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                index=5,
                description="Totais - Quantidade de Registros do Arquivo",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                index=6,
                description="Complemento de Registro",
                numberOfCharacters=211,
                charactersType=alphaNumeric,
            ),
        ]

    def update(self, lots):
        self.setNumberOfLotes(num=len(lots))
        self.setNumberOfRegisters(num=2+3*len(lots))

    def setUserBank(self, bank):
        self.elements[0].setValue(bank.bankId)

    def setNumberOfLotes(self, num):
        self.elements[4].setValue(num)

    def setNumberOfRegisters(self, num):
        self.elements[5].setValue(num)
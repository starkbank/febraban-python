# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ...row import RowElement, Row


class Trailer(Row):

    def __init__(self):
        Row.__init__(self)
        self.elements = [
            RowElement(
                index=0,
                description="N.o DO BANCO NA CÂMARA DE COMPENSAÇÃO",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                index=1,
                description="LOTE DE SERVIÇO",
                numberOfCharacters=4,
                charactersType=numeric,
                value="9999"
            ),
            RowElement(
                index=2,
                description="REGISTRO TRAILER DE ARQUIVO",
                numberOfCharacters=1,
                charactersType=numeric,
                value="9"
            ),
            RowElement(
                index=3,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=9,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=4,
                description="QUANTIDADE DE LOTES DO ARQUIVO",
                numberOfCharacters=6,
                charactersType=numeric
            ),
            RowElement(
                index=5,
                description="QUANTIDADE DE REGISTROS DO ARQUIVO",
                numberOfCharacters=6,
                charactersType=numeric
            ),
            RowElement(
                index=6,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=6,
                charactersType=numeric
            ),
            RowElement(
                index=7,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=205,
                charactersType=alphaNumeric
            )
        ]

    def update(self, lots):
        self.setNumberOfLotes(num=len(lots))
        self.setNumberOfRegisters(num=2+4*len(lots))

    def setUserBank(self, bank):
        self.elements[0].setValue(bank.bankId)

    def setNumberOfLotes(self, num):
        self.elements[4].setValue(num)

    def setNumberOfRegisters(self, num):
        self.elements[5].setValue(num)
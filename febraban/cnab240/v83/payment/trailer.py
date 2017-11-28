
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
            ),
            RowElement(
                index=2,
                description="Registro - Tipo de Registro",
                numberOfCharacters=1,
                charactersType=numeric,
                value='5'
            ),
            RowElement(
                index=3,
                description="Complmento de Registro",
                numberOfCharacters=9,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=4,
                description="Totais - Quantidade de Registros do Lote",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                index=5,
                description="Totais - Somatória dos Valores",
                numberOfCharacters=18,
                charactersType=numeric,
            ),
            RowElement(
                index=6,
                description="Complemento de Registro",
                numberOfCharacters=18,
                charactersType=numeric,
            ),
            RowElement(
                index=7,
                description="Complemento de Registro",
                numberOfCharacters=171,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=8,
                description="Ocorrências - Códigos das Ocorrências para Retorno",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            ),
        ]

    def update(self, segment):
        self.setNumberOfRegisters(num=3)
        self.setSumOfValues(sum=segment.amountInCents())

    def setNumberOfRegisters(self, num):
        self.elements[4].setValue(num)

    def setSumOfValues(self, sum):
        self.elements[5].setValue(sum)

    def setSenderBank(self, bank):
        self.elements[0].setValue(bank.bankId)

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)
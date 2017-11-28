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
            ),
            RowElement(
                description="Registro - Tipo de Registro",
                numberOfCharacters=1,
                charactersType=numeric,
                value='5'
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=9,
                charactersType=alphaNumeric,
            ),
            RowElement(
                description="Totais - Quantidade de Registros do Lote",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                description="Totais - Somatória dos Valores",
                numberOfCharacters=18,
                charactersType=numeric,
            ),
            RowElement(
                description="Totais - Somatória de Quantidade de Moedas",
                numberOfCharacters=18,
                charactersType=numeric,
            ),
            RowElement(
                description="Número Aviso de Débito",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                description="CNAB - Uso Exclusivo FEBRABAN / CNAB",
                numberOfCharacters=165,
                charactersType=alphaNumeric,
            ),
            RowElement(
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

    def setSender(self, user):
        self.elements[0].setValue(user.bankId)

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)

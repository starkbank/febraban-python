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
            ),
            RowElement(
                index=2,
                description="REGISTRO TRAILER DO LOTE",
                numberOfCharacters=1,
                charactersType=numeric,
                value="5"
            ),
            RowElement(
                index=3,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=9,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=4,
                description="QUANTIDADE DE REGISTROS DO LOTE",
                numberOfCharacters=6,
                charactersType=numeric
            ),
            RowElement(
                index=5,
                description="QTDE. DE TÍTULOS EM COBRANÇA SIMPLES",
                numberOfCharacters=6,
                charactersType=numeric,
            ),
            RowElement(
                index=6,
                description="VALOR TOTAL TÍTULOS EM COBRANÇA SIMPLES",
                numberOfCharacters=17,
                charactersType=numeric
            ),
            RowElement(
                index=7,
                description="QTDE. DE TÍTULOS EM COBRANÇA VINCULADA",
                numberOfCharacters=6,
                charactersType=numeric
            ),
            RowElement(
                index=8,
                description="VALOR TOTAL TÍTULOS EM COBRANÇA VINCULADA",
                numberOfCharacters=17,
                charactersType=numeric
            ),
            RowElement(
                index=9,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=46,
                charactersType=numeric
            ),
            RowElement(
                index=10,
                description="REFERÊNCIA DO AVISO BANCÁRIO",
                numberOfCharacters=8,
                charactersType=numeric
            ),
            RowElement(
                index=11,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=117,
                charactersType=alphaNumeric
            )
        ]

    def update(self, segment):
        self.setNumberOfRegisters(num=4)
        self.setSumOfValues(sum=segment.amountInCents())

    def setNumberOfRegisters(self, num):
        self.elements[4].setValue(num)

    def setSumOfValues(self, sum):
        self.elements[6].setValue(sum)

    def setSenderBank(self, bank):
        self.elements[0].setValue(bank.bankId)

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)
        self.elements[5].setValue(index)
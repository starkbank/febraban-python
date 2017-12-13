# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ...row import RowElement, Row


class SegmentQ(Row):

    def __init__(self):
        Row.__init__(self)
        self.elements = [
            RowElement(
                index=0,
                description="N.o DO BANCO NA CÂMARA DE COMPENSAÇÃO",
                numberOfCharacters=3,
                charactersType=numeric
            ),
            RowElement(
                index=1,
                description="LOTE DE SERVIÇO",
                numberOfCharacters=4,
                charactersType=numeric
            ),
            RowElement(
                index=2,
                description="REGISTRO DETALHE",
                numberOfCharacters=1,
                charactersType=numeric,
                value="3"
            ),
            RowElement(
                index=3,
                description="N.o SEQUENCIAL DO REGISTRO NO LOTE",
                numberOfCharacters=5,
                charactersType=numeric,
                value="2"
            ),
            RowElement(
                index=4,
                description="CÓD. SEGMENTO DO REGISTRO DETALHE",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
                value="Q"
            ),
            RowElement(
                index=5,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=6,
                description="IDENTIFICAÇÃO DA OCORRÊNCIA",
                numberOfCharacters=2,
                charactersType=numeric,
                value= "01"
            ),
            RowElement(
                index=7,
                description="TIPO DE INSCRIÇÃO DO PAGADOR",
                numberOfCharacters=1,
                charactersType=numeric
            ),
            RowElement(
                index=8,
                description="N.o DE INSCRIÇÃO DO PAGADOR",
                numberOfCharacters=15,
                charactersType=numeric
            ),
            RowElement(
                index=9,
                description="NOME DO PAGADOR",
                numberOfCharacters=30,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=10,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=11,
                description="RUA, NÚMERO, E COMPLEMENTO DO PAGADOR",
                numberOfCharacters=40,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=12,
                description="BAIRRO DO PAGADOR",
                numberOfCharacters=15,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=13,
                description="CEP DO PAGADOR",
                numberOfCharacters=8,
                charactersType=numeric
            ),
            RowElement(
                index=14,
                description="CIDADE DO PAGADOR",
                numberOfCharacters=15,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=15,
                description="UNIDADE DA FEDERAÇÃO DO PAGADOR",
                numberOfCharacters=2,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=16,
                description="TIPO DE INSCRIÇÃO SACADOR/AVALISTA",
                numberOfCharacters=1,
                charactersType=numeric
            ),
            RowElement(
                index=17,
                description="NÚMERO DE INSCRIÇÃO DO SACADOR/AVALISTA",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                index=18,
                description="NOME DO SACADOR/AVALISTA",
                numberOfCharacters=30,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=19,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=20,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=3,
                charactersType=numeric,
            ),
            RowElement(
                index=21,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=28,
                charactersType=alphaNumeric,
            )
        ]

    def setSenderBank(self, bank):
        self.elements[0].setValue(bank.bankId)                                  # Código do banco debitado

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)                                        # Indica index do lote

    def setPayer(self, user):
        self.elements[7].setValue("1" if len(user.identifier) == 11 else "2")   # 1 - CPF/ 2 - CNPJ
        self.elements[8].setValue(user.identifier)                              # CPF/CNPJ do Pagador
        self.elements[9].setValue(user.name)                                    # Nome do Pagador

    def setPayerAddress(self, address):
        self.elements[11].setValue("%s %s %s" % (address.streetName, address.number, address.complement))
        self.elements[12].setValue(address.district)
        self.elements[13].setValue(address.zipcode)
        self.elements[14].setValue(address.city)
        self.elements[15].setValue(address.state)
# coding: utf-8

from ...characterType import numeric, alphaNumeric
from ...row import RowElement, Row


class SegmentP(Row):

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
                value="1"

            ),
            RowElement(
                index=4,
                description="CÓD. SEGMENTO DO REGISTRO DETALHE",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
                value="P"
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
                value="01"
            ),
            RowElement(
                index=7,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=8,
                description="AGÊNCIA MANTENEDORA DA CONTA",
                numberOfCharacters=4,
                charactersType=numeric
            ),
            RowElement(
                index=9,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=10,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=7,
                charactersType=numeric,
            ),
            RowElement(
                index=11,
                description="NÚMERO DA CONTA CORRENTE DA EMPRESA",
                numberOfCharacters=5,
                charactersType=numeric
            ),
            RowElement(
                index=12,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=13,
                description="DÍGITO DE AUTO-CONFERÊNCIA AG./CONTA EMPRESA",
                numberOfCharacters=1,
                charactersType=numeric
            ),
            RowElement(
                index=14,
                description="NÚMERO DA CARTEIRA NO BANCO",
                numberOfCharacters=3,
                charactersType=numeric,
                value="109"
            ),
            RowElement(
                index=15,
                description="IDENTIFICAÇÃO DO TÍTULO NO BANCO",
                numberOfCharacters=8,
                charactersType=numeric
            ),
            RowElement(
                index=16,
                description="DÍGITO DE AUTO-CONFERÊNCIA NOSSO NÚMERO",
                numberOfCharacters=1,
                charactersType=numeric
            ),
            RowElement(
                index=17,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=8,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=18,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                index=19,
                description="NÚMERO DO DOCUMENTO DE COBRANÇA (DUPL.NP...)",
                numberOfCharacters=10,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=20,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=5,
                charactersType=alphaNumeric,
            ),
            RowElement(
                index=21,
                description="DATA DE VENCIMENTO DO TÍTULO",
                numberOfCharacters=8,
                charactersType=numeric #DDMMAAAA
            ),
            RowElement(
                index=22,
                description="VALOR NOMINAL DO TÍTULO",
                numberOfCharacters=15,
                charactersType=numeric
            ),
            RowElement(
                index=23,
                description="AGÊNCIA ONDE O TÍTULO SERÁ COBRADO",
                numberOfCharacters=5,
                charactersType=numeric,
            ),
            RowElement(
                index=24,
                description="DÍGITO AUTO-CONFERÊNCIA AGÊNCIA COBRADORA",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=25,
                description="ESPÉCIE DO TÍTULO",
                numberOfCharacters=2,
                charactersType=numeric,
                value="99"
            ),
            RowElement(
                index=26,
                description="IDENTIFICAÇÃO DE TÍTULO ACEITO/NÃO ACEITO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
                value="A"
            ),
            RowElement(
                index=27,
                description="DATA DA EMISSÃO DO TÍTULO",
                numberOfCharacters=8,
                charactersType=numeric #DDMMAAAA
            ),
            RowElement(
                index=28,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=29,
                description="DATA BASE P/COBRANÇA DE JUROS DE MORA",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                index=30,
                description="VALOR DE MORA POR DIA DE ATRASO",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                index=31,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=32,
                description="DATA LIMITE DO 1o DESCONTO",
                numberOfCharacters=8,
                charactersType=numeric,
            ),
            RowElement(
                index=33,
                description="VALOR DO 1o DESCONTO A SER CONCEDIDO",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                index=34,
                description="VALOR DO IOF A SER RECOLHIDO P/NOTAS SEGURO",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                index=35,
                description="VALOR DO ABATIMENTO",
                numberOfCharacters=15,
                charactersType=numeric,
            ),
            RowElement(
                index=36,
                description="IDENTIFICAÇÃO DO TÍTULO NA EMPRESA",
                numberOfCharacters=25,
                charactersType=alphaNumeric
            ),
            RowElement(
                index=37,
                description="CÓDIGO PARA NEGATIVAÇÃO OU PROTESTO",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=38,
                description="NÚMERO DE DIAS PARA NEGATIVAÇÃO OU PROTESTO",
                numberOfCharacters=2,
                charactersType=numeric,
            ),
            RowElement(
                index=39,
                description="CÓDIGO PARA BAIXA",
                numberOfCharacters=1,
                charactersType=numeric,
            ),
            RowElement(
                index=40,
                description="NÚMERO DE DIAS PARA BAIXA",
                numberOfCharacters=2,
                charactersType=numeric,
            ),
            RowElement(
                index=41,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=13,
                charactersType=numeric,
            ),
            RowElement(
                index=42,
                description="COMPLEMENTO DE REGISTRO",
                numberOfCharacters=1,
                charactersType=alphaNumeric,
            )
        ]

    def amountInCents(self):
        return self.elements[22].value()

    def setSenderBank(self, bank):
        self.elements[0].setValue(bank.bankId)            # Código do banco debitado
        self.elements[8].setValue(bank.branchCode)        # Agencia do Usuário
        self.elements[11].setValue(bank.accountNumber)    # Conta do Usuário
        self.elements[13].setValue(bank.accountVerifier)  # DAC Conta do Usuário

    def setPositionInLot(self, index):
        self.elements[1].setValue(index)                  # Indica index do lote

    def setBankIdentifier(self, identifier, dac):
        self.elements[15].setValue(identifier)            # Número dado pelo Banco
        self.elements[16].setValue(dac)                   # Verificador do número dado pelo Banco

    def setIdentifier(self, identifier):
        self.elements[19].setValue(identifier)            # Código interno da empresa. Ex: Num de nota fiscal

    def setAmountInCents(self, amount):
        self.elements[22].setValue(amount)                # Valor do Boleto

    def setExpirationDate(self, date):
        self.elements[21].setValue(date)                  # Data de vencimento do boleto

    def setIssueDate(self, date):
        self.elements[27].setValue(date)                  # Data de emissão do boleto


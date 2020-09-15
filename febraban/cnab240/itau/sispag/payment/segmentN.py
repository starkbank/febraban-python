# coding: utf-8
# Pagamento de Contas de Concessionárias e Tributos sem código de barras # Página 31
from ....row import Row
from ....characterType import numeric, alphaNumeric


class SegmentN:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (  3,   7,  4,      numeric,   "1"),
            (  7,   8,  1,      numeric,   "3"),  # Tipo de Registro
            ( 13,  14,  1, alphaNumeric,   "N"),  # Código de Segmento
            ( 14,  17,  3,      numeric,   "0"),  # Tipo de Movimento
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setLot(self, lot):
        structs = [
            (3,  7, 4, numeric, lot),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxPaymentIdentifier(self, id):
        structs = [
            (17, 19, 2, numeric, id),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setRevenueCode(self, code):
        structs = [
            (19, 23, 4, numeric, code),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxIdType(self, taxIdType):
        structs = [
            (23, 24, 1, numeric, taxIdType),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxId(self, taxId):
        structs = [
            (24, 38, 14, numeric, taxId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReferenceDate(self, referenceDate):
        structs = [
            (38, 46, 8, numeric, referenceDate),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReferenceNumber(self, referenceNumber):
        structs = [
            (46, 63, 17, numeric, referenceNumber),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setNominalAmount(self, dueDate):
        structs = [
            (63, 77, 14, numeric, dueDate),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFineAmount(self, fineAmount):
        structs = [
            (77, 91, 14, numeric, fineAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInterestAmount(self, interestAmount):
        structs = [
            (91, 105, 14, numeric, interestAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTotalAmount(self, totalAmount):
        structs = [
            (105, 119, 14, numeric, totalAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDueDate(self, dueDate):
        structs = [
            (119, 127, 8, numeric, dueDate),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setScheduleDate(self, paymentDate):
        structs = [
            (127, 135, 8, numeric, paymentDate),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (195, 215, 20, alphaNumeric, identifier),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

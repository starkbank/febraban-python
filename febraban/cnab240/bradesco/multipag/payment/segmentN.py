# coding: utf-8
from febraban.cnab240.row import Row
from febraban.cnab240.characterType import alphaNumeric, numeric


class SegmentN:
    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (  3,   7,  4,      numeric,   "1"),
            (  7,   8,  1,      numeric,   "3"),  # Type of record
            ( 13,  14,  1, alphaNumeric,   "N"),  # Segment code
            ( 14,  15,  1,      numeric,   "0"),  # Movement type
            ( 15,  17,  2,      numeric,   "00"), # Movement instruction code
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setLot(self, lot):
        structs = [
            (3,  7, 4, numeric, lot),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (17, 37, 20, alphaNumeric, identifier),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setOurNumber(self, ourNumber):
        structs = [
            (37, 57, 20, alphaNumeric, ourNumber),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setContributorName(self, name):
        structs = [
            (57, 87, 30, alphaNumeric, name),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPaymentDate(self, date):
        structs = [
            (87, 95, 8, numeric, date),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTotalAmount(self, amount):
        structs = [
            (95, 110, 15, numeric, amount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setRevenueCode(self, code):
        structs = [
            (110, 116, 6, alphaNumeric, code),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxIdType(self, taxIdType):
        structs = [
            (116, 118, 2, numeric, taxIdType),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxId(self, taxId):
        structs = [
            (118, 132, 14, alphaNumeric, taxId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setTaxPaymentIdentifier(self, id):
        structs = [
            (132, 134, 2, alphaNumeric, id),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReferenceDate(self, referenceDate):
        structs = [
            (134, 142, 8, numeric, referenceDate),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReferenceNumber(self, referenceNumber):
        structs = [
            (142, 159, 17, numeric, referenceNumber),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setNominalAmount(self, nominalAmount):
        structs = [
            (159, 174, 15, numeric, nominalAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFineAmount(self, fineAmount):
        structs = [
            (174, 189, 15, numeric, fineAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInterestAmount(self, interestAmount):
        structs = [
            (189, 204, 15, numeric, interestAmount),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setDueDate(self, dueDate):
        structs = [
            (204, 212, 8, numeric, dueDate),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

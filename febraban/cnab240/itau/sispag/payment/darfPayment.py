from .barCodePayment import BarCodePayment
from .nonBarCodePayment import NonBarCodePayment


class DarfBarCodePayment(BarCodePayment):
    pass


class DarfPayment(NonBarCodePayment):
    def setPayment(self, **kwargs):
        self.setSender(kwargs.get("sender"))
        self.setTaxPaymentIdentifier("02")
        self.setRevenueCode(kwargs.get("revenueCode"))
        self.setTaxIdInfo(kwargs.get("taxId"))
        self.setReferenceDate(kwargs.get("referenceDate"))
        self.setReferenceNumber(kwargs.get("referenceNumber"))
        self.setNominalAmount(kwargs.get("amount"))
        self.setFineAmount(kwargs.get("fine"))
        self.setInterestAmount(kwargs.get("interest"))
        self.setTotalAmount(kwargs.get("totalAmount"))
        self.setDueDate(kwargs.get("dueDate"))
        self.setScheduleDate(kwargs.get("scheduleDate"))
        self.setIdentifier(kwargs.get("identifier"))

    def setTaxPaymentIdentifier(self, id):
        self.segmentN.setTaxPaymentIdentifier(id)

    def setRevenueCode(self, code):
        self.segmentN.setRevenueCode(code)

    def setTaxIdInfo(self, taxId):
        taxId = "".join(c for c in taxId if c.isdigit())
        taxIdType = "1" if len(taxId) == 11 else "2"
        self.segmentN.setTaxIdType(taxIdType)
        self.segmentN.setTaxId(taxId)

    def setReferenceDate(self, referenceDate):
        self.segmentN.setReferenceDate(referenceDate)

    def setReferenceNumber(self, referenceNumber):
        self.segmentN.setReferenceNumber(referenceNumber)

    def setNominalAmount(self, amount):
        self.segmentN.setNominalAmount(amount)
        self.amount = int(amount)

    def setInterestAmount(self, interestAmount):
        self.segmentN.setInterestAmount(interestAmount)
        self.additionAmount += int(interestAmount)

    def setFineAmount(self, fineAmount):
        self.segmentN.setFineAmount(fineAmount)
        self.additionAmount += int(fineAmount)

    def setTotalAmount(self, totalAmount):
        self.segmentN.setTotalAmount(totalAmount)
        self.totalAmount = int(totalAmount)

    def setDueDate(self, dueDate):
        self.segmentN.setDueDate(dueDate)

    def setScheduleDate(self, paymentDate):
        self.segmentN.setScheduleDate(paymentDate)

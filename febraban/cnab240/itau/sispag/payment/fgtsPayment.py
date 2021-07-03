from febraban.cnab240.itau.sispag import NonBarCodePayment


class FgtsPayment(NonBarCodePayment):

    def setPayment(self, **kwargs):
        self.setSender(kwargs.get("sender"))
        self.setTaxPaymentIdentifier("11")
        self.setRevenueCode("115")
        self.setTaxIdInfo(kwargs.get("taxId"))
        self.setFgtsScheduleDate(kwargs.get("scheduleDate"))
        self.setIdentifier(kwargs.get("identifier"))
        self.setBarCode(kwargs.get("barCode"))
        self.setFgtsAmount(kwargs.get("amount"))
        self.setFgtsNullValues()

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

    def setFgtsAmount(self, amount):
        self.segmentN.setFgtsAmount(amount)
        self.amount = int(amount)

    def setDueDate(self, dueDate):
        self.segmentN.setDueDate(dueDate)

    def setFgtsScheduleDate(self, paymentDate):
        self.segmentN.setFgtsScheduleDate(paymentDate)

    def setBarCode(self, barCode):
        self.segmentN.setBarCode(barCode)

    def setFgtsNullValues(self):
        self.segmentN.setFgtsNullValues()

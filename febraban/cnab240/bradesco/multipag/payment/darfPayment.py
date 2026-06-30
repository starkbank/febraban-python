from febraban.cnab240.bradesco.multipag.payment.nonBarCodePayment import NonBarCodePayment


class DarfPayment(NonBarCodePayment):

    def setPayment(self, **kwargs):
        self.setSender(kwargs.get("sender"))
        self.setTaxPaymentIdentifier("16")
        self.setRevenueCode(kwargs.get("revenueCode"))
        self.setTaxIdInfo(kwargs.get("taxId"))
        self.setReferenceDate(kwargs.get("referenceDate"))
        self.setReferenceNumber(kwargs.get("referenceNumber"))
        self.setNominalAmount(kwargs.get("amount"))
        self.setFineAmount(kwargs.get("fine"))
        self.setInterestAmount(kwargs.get("interest"))
        self.setTotalAmount(kwargs.get("totalAmount"))
        self.setDueDate(kwargs.get("dueDate"))
        self.setIdentifier(kwargs.get("identifier"))
        self.setOurNumber(kwargs.get("ourNumber",""))
        self.setRevenueCode(kwargs.get("revenueCode"))    

    def setRevenueCode(self, code):
        self.segmentN.setRevenueCode(code)

    def setIdentifier(self, identifier):
        self.segmentN.setIdentifier(identifier)

    def setOurNumber(self, ourNumber):
        self.segmentN.setOurNumber(ourNumber)

    def setTaxPaymentIdentifier(self, id):
        self.segmentN.setTaxPaymentIdentifier(id)


    def setTaxIdInfo(self, taxId):
        taxId = "".join(c for c in taxId if c.isalnum()).upper()
        taxIdType = "2" if len(taxId) == 11 else "1"
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

    def setPaymentDate(self, paymentDate):
        self.segmentN.setPaymentDate(paymentDate)

    def setContributorName(self, name):
        self.segmentN.setContributorName(name)


    def setRevenueCode(self, code):
        self.segmentN.setRevenueCode(code)

    def setTaxIdType(self, taxIdType):
        self.segmentN.setTaxIdType(taxIdType)

    def setTaxId(self, taxId):
        self.segmentN.setTaxId(taxId)

    def amountInCents(self):
        return self.amount

    def otherAmountInCents(self):
        return self.otherAmount

    def additionAmountInCents(self):
        return self.additionAmount

    def setSender(self, user):
        self.segmentN.setSenderBank(user.bank)

    def setPositionInLot(self, index):
        self.segmentN.setPositionInLot(index)

    def setLot(self, lot):
        self.segmentN.setLot(lot)

from .header import Header
from .segmentNDarf import SegmentNDarf
from .taxesTrailer import TaxesTrailer


class DarfPayment:  # DARF NORMAL

    def __init__(self):
        self.header = Header(layoutNum="030")
        self.segmentN = SegmentNDarf()
        self.trailer = TaxesTrailer()
        self.trailer.setSumOthersAmountInCents(otherAmount="00000000000000")

    def setPayment(self, **kwargs):
        self.setSender(kwargs.get("sender"))
        self.setTypeTaxId()
        self.setSubscriptionId()
        self.setPaymentId(kwargs.get("taxCode"))
        self.setReferenceNumber(refNum="00000000000000001")  # ToDo check if is necessary
        self.setTaxId(kwargs.get("taxId"))
        self.setEvaluationDate(kwargs.get("referenceDate"))
        self.setDueDate(kwargs.get("dueDate"))
        self.setPaymentDate()
        self.setAmount(kwargs.get("amount"))
        self.setMainAmount(kwargs.get("amount"))
        self.setInterestAmount(kwargs.get("interestAmount"))
        self.setFineAmount(kwargs.get("fineAmount"))
        self.setActualAmount(kwargs.get("amount"), kwargs.get("interestAmount"), kwargs.get("fineAmount"))
        self.setTaxPayer(kwargs.get("sender"))
        self.setIdentifier(kwargs.get("identifier"))
        self.setInfo()

    def toString(self):
        return "\r\n".join((
            self.header.content,
            self.segmentN.content,
            self.trailer.content,
        ))

    def setSender(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.header.setSenderAddress(user.address)
        self.segmentN.setSenderBank(user.bank)
        self.trailer.setSenderBank(user.bank)

    def setTypeTaxId(self, id="02"):
        self.segmentN.setTypeTaxId(id)

    def setSubscriptionId(self, subsciptionId="2"):
        self.segmentN.setSubscriptionId(subsciptionId)

    def setPaymentId(self, paymentId):
        self.segmentN.setPaymentId(paymentId)

    def setTaxId(self, CNPJ):
        self.segmentN.setTaxId(CNPJ)

    def setEvaluationDate(self, evalDate):
        self.segmentN.setEvaluationDate(evalDate)

    def setReferenceNumber(self, refNum):
        self.segmentN.setReferenceNumber(refNum)

    def setMainAmount(self, mainAmount):
        self.segmentN.setMainAmount(mainAmount)

    def setFineAmount(self, fineAmount):
        self.segmentN.setFineAmount(str(fineAmount))

    def setInterestAmount(self, interestAmount):
        self.segmentN.setInterestAmount(str(interestAmount))

    def setAmount(self, amount):
        self.segmentN.setTotalAmount(amount)
        self.trailer.setSumAmountInCents(amount)
        self.trailer.setAmountInCents(amount)

    def setActualAmount(self, amount, interestAmount, fineAmount):
        actualAmount = amount
        if interestAmount and fineAmount:
            actualAmount = int(interestAmount) + int(fineAmount) + int(amount)
        self.trailer.setActualAmountInCents(str(actualAmount))

    def setDueDate(self, dueDate):
        self.segmentN.setdueDate(dueDate)

    def setPaymentDate(self):
        self.segmentN.setPaymentDate()

    def setTaxPayer(self, sender):
        self.segmentN.setTaxPayer(sender.name)

    def setPositionInLot(self, index):
        self.header.setPositionInLot(index)
        self.trailer.setPositionInLot(index)
        self.trailer.setLotNumberOfRegisters(3)

    def setIdentifier(self, identifier):
        self.segmentN.setIdentifier(identifier)

    def setInfo(self, kind="22", method="16"):
        """
        This method set config information in the payment
        Args:
            kind:   String - Kind of payment - 22 Tributos, Nota 4
            method: String - Payment method  - 16 DARF NORMAL. Nota 5
        """
        self.header.setInfo(kind, method)

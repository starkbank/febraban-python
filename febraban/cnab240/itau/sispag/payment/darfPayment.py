from febraban.cnab240.itau.sispag.payment.header import Header
from febraban.cnab240.itau.sispag.payment.segmentNdarf import SegmentNdarf
from febraban.cnab240.itau.sispag.payment.taxesTrailer import TaxesTrailer


class DarfPayment:  # DARF NORMAL

    def __init__(self):
        self.header = Header(layoutNum="030")
        self.segmentN = SegmentNdarf()
        self.trailer = TaxesTrailer()
        self.trailer.setSumOthersAmountInCents(otherAmount="00000000000000")

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
        self.segmentN.setFineAmount(fineAmount)
        self.trailer.setActualAmountInCents(actualAmount=fineAmount)

    def setInterestAmount(self, interestAmount):
        self.segmentN.setInterestAmount(interestAmount)

    def setAmount(self, amount):
        self.segmentN.setTotalAmount(amount)
        self.trailer.setSumAmountInCents(amount)
        self.trailer.setAmountInCents(amount)

    def setDueDate(self, dueDate):
        self.segmentN.setdueDate(dueDate)

    def setPaymentDate(self):
        self.segmentN.setPaymentDate()

    def setTaxPayer(self, payer):
        self.segmentN.setTaxPayer(payer)

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

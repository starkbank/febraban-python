from .header import Header
from .segmentNGps import SegmentNGps
from .taxesTrailer import TaxesTrailer

# GPS Codigo de Pagamento: 2100 = Empresas em geral - CNPJ


class GpsPayment:

    def __init__(self):
        self.header = Header(layoutNum="030")
        self.segmentN = SegmentNGps()
        self.trailer = TaxesTrailer()

    def setPayment(self, **kwargs):
        self.setTypeTaxId()
        self.setPaymentId()
        self.setReferenceMonth(kwargs.get("referenceDate"))
        self.setSender(kwargs.get("sender"))
        self.setInfo()
        self.setAmount(kwargs.get("amount"))
        actualAmount =self.getActualAmount(kwargs.get("amount"), kwargs.get("interestAmount"), kwargs.get("fineAmount"))
        self.setOtherAmount(otherAmount=actualAmount)
        self.setActualAmount(actualAmount)
        self.setCollectedAmount(kwargs.get("incomeAmount"))
        self.setTaxId(kwargs.get("taxId"))
        self.setIdentifier(kwargs.get("identifier"))
        self.setTaxPayer(kwargs.get("sender").name)
        self.setRaisedDate()

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

    def setTypeTaxId(self, id="01"):
        self.segmentN.setTypeTaxId(id)

    def setPaymentId(self, id="2100"):                  # (Nota 20)
        self.segmentN.setPaymentId(id)

    def setReferenceMonth(self, refMonth):
        self.segmentN.setRefMonth(refMonth)

    def setRaisedDate(self):
        self.segmentN.setRaisedDate()

    def setAmount(self, amount):
        self.segmentN.setAmount(amount)
        self.trailer.setAmountInCents(amount)

    def setCollectedAmount(self, collectedAmount):
        self.segmentN.setCollectedAmount(collectedAmount)
        self.trailer.setSumAmountInCents(collectedAmount)

    def getActualAmount(self, amount, interestAmount, fineAmount):
        actualAmount = amount
        if interestAmount and fineAmount:
            actualAmount = int(interestAmount) + int(fineAmount) + int(amount)
        return str(actualAmount)

    def setActualAmount(self, actualAmount):
        self.trailer.setActualAmountInCents(str(actualAmount))

    def setOtherAmount(self, otherAmount):
        self.segmentN.setOtherAmount(otherAmount)
        self.trailer.setSumOthersAmountInCents(otherAmount)

    def setPositionInLot(self, index):
        self.header.setPositionInLot(index)
        self.trailer.setPositionInLot(index)
        self.trailer.setLotNumberOfRegisters(3)

    def setTaxId(self, CNPJ):
        self.segmentN.setTaxId(CNPJ)

    def setTaxPayer(self, payer):
        self.segmentN.setTaxPayer(payer)

    def setIdentifier(self, identifier):
        self.segmentN.setIdentifier(identifier)

    def setInfo(self, kind="22", method="17"):
        """
        This method set config information in the payment
        Args:
            kind:   String - Kind of payment - 22 Tributos, Nota 4
            method: String - Payment method  - 17 GPS - GUIA DA PREVIDENCIA SOCIAL. Nota 5
        """
        self.header.setInfo(kind, method)

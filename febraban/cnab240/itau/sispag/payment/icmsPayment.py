from febraban.cnab240.itau.sispag.payment.header import Header
from febraban.cnab240.itau.sispag.payment.segmentNicms import SegmentNICMS
from febraban.cnab240.itau.sispag.payment.taxesTrailer import TaxesTrailer


class IcmsPayment:

    def __init__(self):
        self.header = Header(layoutNum="030")
        self.segmentN = SegmentNICMS()
        self.trailer = TaxesTrailer()

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

    def setIdentifier(self, identifier):
        self.segmentN.setIdentifier(identifier)

    def setTypeTaxId(self, id="05"):
        self.segmentN.setTypeTaxId(id)

    def setPaymentId(self, paymentId):
        self.segmentN.setPaymentId(paymentId)

    def setIdType(self, idType):
        self.segmentN.setIdType(idType)

    def setTaxId(self, taxId):
        self.segmentN.setTaxId(taxId)

    def setStateRegistration(self, regId):
        self.segmentN.setStateRegistration(regId)

    def setDebNum(self, debtNum):
        self.segmentN.setDebtNum(debtNum)

    def setFine(self, fine):
        self.segmentN.setFine(fine)

    def setNotificationNumber(self, notificationNumber):
        self.segmentN.setNotificationNumber(notificationNumber)

    def setInterest(self, interest):
        self.segmentN.setInterest(interest)

    def setRefMonth(self, refMonth):
        self.segmentN.setRefMonth(refMonth)

    def setDueDate(self, dueDate):
        self.segmentN.setDueDate(dueDate)

    def setPaymentDate(self):
        self.segmentN.setPaymentDate()

    def setRecipe(self, recipeAmount):
        self.segmentN.setRecipe(recipeAmount)

    def setAmount(self, amount):
        self.segmentN.setAmount(amount)

    def setPositionInLot(self, index):
        self.header.setPositionInLot(index)
        self.segmentN.setPositionInLot(index)
        self.trailer.setPositionInLot(index)
        self.trailer.setLotNumberOfRegisters(3)

    def setInfo(self, kind="22", method="19"):
        """
        This method set config information in the payment
        Args:
            kind:   String - Kind of payment - 22 Tributos, Nota 4
            method: String - Payment method  - 19 IPTU/ISS/OUTROS TRIBUTOS MUNICIPAIS. Nota 5
        """
        self.header.setInfo(kind, method)

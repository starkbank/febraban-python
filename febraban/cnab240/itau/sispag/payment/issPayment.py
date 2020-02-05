from .header import Header
from .segmentO import SegmentO
from .trailer import Trailer
from ....libs.dac import DAC
from ....libs.barCode import IptuBarCode


class IssPayment:

    def __init__(self):
        self.header = Header(layoutNum="030")
        self.segmentO = SegmentO()
        self.trailer = Trailer()

    def setPayment(self, **kwargs):
        self.barCode = IptuBarCode(kwargs.get("barCode"))
        self.setSender(kwargs.get("sender"))
        self.setBarCode(self.barCode)
        self.setDueDate(kwargs.get("dueDate"))
        self.setCurrencyAmount(kwargs.get("amount"))
        self.setAmount(kwargs.get("amount"))
        self.setIdentifier(kwargs.get("identifier"))
        self.setInfo()

    def toString(self):
        return "\r\n".join((
            self.header.content,
            self.segmentO.content,
            self.trailer.content,
        ))

    def setSender(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.header.setSenderAddress(user.address)
        self.segmentO.setSenderBank(user.bank)
        self.trailer.setSenderBank(user.bank)

    def setIdentifier(self, identifier):
        self.segmentO.setIdentifier(identifier)

    def setBarCode(self, barCode):
        dac = DAC.calculateDacIptu(
            productId=barCode.productId,
            segmentId=barCode.segmentId,
            currency=barCode.currency,
            amount=barCode.amount,
            company=barCode.companyId,
            freeField=barCode.freeField
        )
        self.segmentO.setBarCode(barCode, dac)
        self.trailer.setAmountInCents(barCode.amount)

    def setLineNumber(self, lineNumber):
        self.segmentO.setLineNumber(lineNumber)

    def setDueDate(self, dueDate):
        self.segmentO.setDueDate(dueDate.strftime("%d%m%Y"))

    def setCurrencyAmount(self, currencyAmount):
        self.segmentO.setCurrencyAmount(currencyAmount)

    def setAmount(self, amount):
        self.segmentO.setAmount(amount)
        self.trailer.setAmountInCents(amount)

    def setPositionInLot(self, index):
        self.header.setPositionInLot(index)
        self.segmentO.setPositionInLot(index)
        self.trailer.setPositionInLot(index)
        self.trailer.setLotNumberOfRegisters(3)

    def setInfo(self, kind="22", method="19"):
        """
        kind:   String - Kind of payment - 22 Tributos, Nota 4
        method: String - Payment method  - 19 IPTU/ISS/OUTROS TRIBUTOS MUNICIPAIS. Nota 5
        """
        self.header.setInfo(kind, method)

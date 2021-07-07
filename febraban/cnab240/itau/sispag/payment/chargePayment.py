from .segmentJ import SegmentJ
from .segmentJ52 import SegmentJ52


class ChargePayment:

    def __init__(self):
        self.segmentJ = SegmentJ()
        self.segmentJ52 = SegmentJ52()
        self.amount = 0
        self.discountAmount = 0
        self.additionAmount = 0
        self.totalAmount = 0

    def setPayment(self, **kwargs):
        self.setSender(kwargs["sender"])
        self.setReceiverTaxId(kwargs["receiverTaxId"])
        self.setBarCode(kwargs["barCode"])
        self.setIdentifier(kwargs["identifier"])
        self.setScheduleDate(kwargs["scheduleDate"].strftime("%d%m%Y"))
        self.setAmounts(
            kwargs.get("discountAmount"),
            kwargs.get("addedAmount"),
            kwargs.get("totalAmount"),
        )

    def toString(self):
        return "\r\n".join((
            self.segmentJ.content,
            self.segmentJ52.content,
        ))

    def amountInCents(self):
        return self.amount

    def totalAmountInCents(self):
        return self.totalAmount

    def setSender(self, user):
        """Sets the sender for the payment. The sender represents a user, its bank and its address."""
        self.segmentJ.setSenderBank(user.bank)
        self.segmentJ52.setSender(user)
        self.segmentJ52.setSenderBank(user.bank)

    def setReceiverTaxId(self, receiverTaxId):
        """Sets the receiver for the payment. Only the receiver's taxId is necessary."""
        self.segmentJ52.setReceiverTaxId(receiverTaxId)

    def setIdentifier(self, identifier):
        """Sets the charge identifier that will be returned from the bank. Used for matching results."""
        self.segmentJ.setIdentifier(identifier)

    def setScheduleDate(self, paymentDate):
        """Sets the payment date to be sent to the bank."""
        self.segmentJ.setScheduleDate(paymentDate)

    def setBarCode(self, barCode):
        self.segmentJ.setBarCode(barCode)
        self.amount = int(barCode.amount)

    def setAmounts(self, discountAmount, addedAmount, totalAmount):
        self.segmentJ.setAmounts(discountAmount, addedAmount, totalAmount)
        self.discountAmount = discountAmount
        self.additionAmount = addedAmount
        self.totalAmount = totalAmount

    def setPositionInLot(self, index):
        index = 2 * index - 1
        self.segmentJ.setPositionInLot(index)
        self.segmentJ52.setPositionInLot(index + 1)

    def setLot(self, lot):
        self.segmentJ.setLot(lot)
        self.segmentJ52.setLot(lot)

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
        barCode = kwargs["barCode"]
        dueDate = kwargs.get("dueDate") or barCode.dueDate
        self.setSender(kwargs["sender"])
        self.setReceiverTaxId(kwargs["receiverTaxId"])
        self.setBarCode(barCode)
        self.setIdentifier(kwargs["identifier"])
        self.setScheduleDate(kwargs["scheduleDate"].strftime("%d%m%Y"))
        self.setDueDate(dueDate.strftime("%d%m%Y"))
        self.setAmounts(
            discountAmount=kwargs["discountAmount"],
            addedAmount=kwargs["addedAmount"],
            totalAmount=kwargs["totalAmount"],
            nominalAmount=kwargs.get("nominalAmount")
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

    def setDueDate(self, dueDate):
        """Sets the payment due date extracted from either CIP or the barcode itself"""
        self.segmentJ.setDueDate(dueDate)

    def setBarCode(self, barCode):
        self.segmentJ.setBarCode(barCode)
        self.amount = int(barCode.amount)

    def setAmounts(self, discountAmount, addedAmount, totalAmount, nominalAmount=None):
        self.segmentJ.setAmounts(
            discountAmount=discountAmount,
            addedAmount=addedAmount,
            totalAmount=totalAmount
        )
        self.discountAmount = discountAmount
        self.additionAmount = addedAmount
        self.totalAmount = totalAmount

        if not self.amount and nominalAmount:
            self.segmentJ.setNominalAmount(nominalAmount=nominalAmount)
            self.amount = nominalAmount

    def setPositionInLot(self, index):
        index = 2 * index - 1
        self.segmentJ.setPositionInLot(index)
        self.segmentJ52.setPositionInLot(index + 1)

    def setLot(self, lot):
        self.segmentJ.setLot(lot)
        self.segmentJ52.setLot(lot)

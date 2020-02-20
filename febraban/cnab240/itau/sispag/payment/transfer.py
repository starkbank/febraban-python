from .segmentA import SegmentA


class Transfer:

    def __init__(self):
        self.segmentA = SegmentA()

    def toString(self):
        return self.segmentA.content

    def amountInCents(self):
        return self.segmentA.amountInCents()

    def setSender(self, user):
        self.segmentA.setSenderBank(user.bank)

    def setReceiver(self, user):
        self.segmentA.setReceiver(user)
        self.segmentA.setReceiverBank(user.bank)

    def setAmountInCents(self, value):
        self.segmentA.setAmountInCents(value)

    def setPositionInLot(self, index):
        self.segmentA.setPositionInLot(index)

    def setScheduleDate(self, date):
        self.segmentA.setScheduleDate(date)

    def setInfo(self, reason="10"):
        """
        This method set config information in the payment

        Args:
            reason: String - Payment reason  - 10 Credito em Conta Corrente, read: NOTES 26
        """
        self.segmentA.setInfo(reason)

    def setIdentifier(self, identifier):
        self.segmentA.setIdentifier(identifier)

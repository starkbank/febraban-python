from .header import Header
from .segmentA import SegmentA
from .trailer import Trailer


class PaymentV83:

    def __init__(self):
        self.header = Header()
        self.segmentA = SegmentA()
        self.trailer = Trailer()

    def toString(self):
        return self.header.content + "\r\n" + self.segmentA.content + "\r\n" + self.trailer.content

    def setSender(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.header.setSenderAddress(user.address)
        self.segmentA.setSenderBank(user.bank)
        self.trailer.setSenderBank(user.bank)

    def setReceiver(self, user):
        self.segmentA.setReceiver(user)
        self.segmentA.setReceiverBank(user.bank)

    def setAmountInCents(self, value):
        self.segmentA.setAmountInCents(value)
        self.trailer.setAmountInCents(value)

    def setPositionInLot(self, index):
        self.header.setPositionInLot(index)
        self.segmentA.setPositionInLot(index)
        self.trailer.setPositionInLot(index)

    def setScheduleDate(self, date):
        self.segmentA.setScheduleDate(date)

    def setInfo(self, kind="98", method="41", reason="10"):
        """
        This method set config information in the payment

        Args:
            kind:   String - Kind of payment - 98 Diversos, read: NOTES 4
            method: String - Payment method  - 41 TED Outro titular, 43 TED Mesmo titular, 01 ITAU account. read: NOTES 5
            reason: String - Payment reason  - 10 Credito em Conta Corrente, read: NOTES 26
        """
        self.header.setInfo(kind, method)
        self.segmentA.setInfo(reason)

    def setIdentifier(self, identifier):
        self.segmentA.setIdentifier(identifier)
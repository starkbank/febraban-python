from .header import Header
from .segmentJ import SegmentJ
from .segmentJ52 import SegmentJ52
from .trailer import Trailer


class ChargePayment:

    def __init__(self):
        self.header = Header()
        self.segmentJ = SegmentJ()
        self.segmentJ52 = SegmentJ52()
        self.trailer = Trailer()

    def toString(self):
        # self.validate()
        return "\r\n".join((
            self.header.content,
            self.segmentJ.content,
            self.segmentJ52.content,
            self.trailer.content,
        ))

    def setSender(self, user):
        """Sets the sender for the payment. The sender represents a users, its bank and its address."""
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.header.setSenderAddress(user.address)
        self.segmentJ.setSenderBank(user.bank)
        self.segmentJ52.setSender(user)
        self.segmentJ52.setSenderBank(user.bank)
        self.trailer.setSenderBank(user.bank)

    def setReceiverTaxId(self, receiverTaxId):
        """Sets the receiver for the payment. Only the receiver's taxId is necessary."""
        self.segmentJ52.setReceiverTaxId(receiverTaxId)

    def setIdentifier(self, identifier):
        """Sets the charge identifier that will be returned from the bank. Used for matching results."""
        self.segmentJ.setIdentifier(identifier)

    def setScheduleDate(self, paymentDate):
        """Sets the payment date to be sent to the bank. Defaults to today."""
        self.segmentJ.setScheduleDate(paymentDate)

    def setBarCode(self, barCode):
        self.segmentJ.setBarCode(barCode)
        self.trailer.setAmountInCents(barCode.amount)

    def setPositionInLot(self, index):
        self.header.setPositionInLot(index)
        self.segmentJ.setPositionInLot(index)
        self.segmentJ52.setPositionInLot(index)
        self.trailer.setPositionInLot(index)
        self.trailer.setLotNumberOfRegisters(4)

    def setInfo(self, kind="98", method="31"):
        """
        This method set config information in the payment

        Args:
            kind:   String - Kind of payment - 20 Fornecedores, read: NOTES 4
            method: String - Payment method  - 30 Pagamento Boleto Itau, 31 Pagamento Boleto outros Bancos. read: NOTES 5
        """
        self.header.setInfo(kind, method)

    # def validate(self):
    #     self.header.validate()
    #     self.segmentJ.validate()
    #     self.segmentJ52.validate()
    #     self.trailer.validate()

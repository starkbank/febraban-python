from febraban.cnab240.itau.sispag.payment.segmentN import SegmentN


class NonBarCodePayment:
    def __init__(self):
        self.segmentN = SegmentN()
        self.amount = 0

    def setIdentifier(self, identifier):
        self.segmentN.setIdentifier(identifier)

    def setSender(self, user):
        self.segmentN.setSenderBank(user.bank)

    def setPositionInLot(self, index):
        self.segmentN.setPositionInLot(index)

    def setLot(self, lot):
        self.segmentN.setLot(lot)

    def setPayerName(self, payerName):
        self.segmentN.setPayerName(payerName)

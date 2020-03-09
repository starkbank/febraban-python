from .segmentO import SegmentO
from ....libs.dac import DAC


class UtilityPayment:

    def __init__(self):
        self.segmentO = SegmentO()
        self.amount = 0

    def toString(self):
        return "\r\n".join((
            self.segmentO.content,
        ))

    def amountInCents(self):
        return self.amount

    def setSender(self, user):
        self.segmentO.setSenderBank(user.bank)

    def setIdentifier(self, identifier):
        self.segmentO.setIdentifier(identifier)

    def setBarCode(self, barCode):
        dac = DAC.sispag(
            productId=barCode.productId,
            segmentId=barCode.segmentId,
            currency=barCode.currency,
            amount=barCode.amount,
            company=barCode.companyId,
            freeField=barCode.freeField
        )
        self.segmentO.setBarCode(barCode, dac)
        self.amount = int(barCode.amount)

    def setScheduleDate(self, paymentDate):
        self.segmentO.setScheduleDate(paymentDate)

    def setDueDate(self, dueDate):
        self.segmentO.setDueDate(dueDate)

    def setPositionInLot(self, index):
        self.segmentO.setPositionInLot(index)

from .segmentO import SegmentO


class BarCodePayment:

    def __init__(self):
        self.segmentO = SegmentO()
        self.amount = 0

    def setPayment(self, **kwargs):
        self.setSender(kwargs.get("sender"))
        self.setScheduleDate(kwargs.get("scheduleDate"))
        self.setIdentifier(kwargs.get("identifier"))
        self.setLineNumber(kwargs.get("lineNumber"))
        self.setDueDate(kwargs.get("scheduleDate"))

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

    def setLineNumber(self, lineNumber):
        self.segmentO.setLineNumber(lineNumber)
        self.amount = int(lineNumber.amount)

    def setScheduleDate(self, paymentDate):
        self.segmentO.setScheduleDate(paymentDate)

    def setDueDate(self, dueDate):
        self.segmentO.setDueDate(dueDate)

    def setPositionInLot(self, index):
        self.segmentO.setPositionInLot(index)

    def setLot(self, lot):
        self.segmentO.setLot(lot)

from ...libs.dac import DAC
from .header import Header
from .segmentP import SegmentP
from .segmentQ import SegmentQ
from .trailer import Trailer


class SlipV30:

    def __init__(self):
        self.header=Header()
        self.segmentP=SegmentP()
        self.segmentQ=SegmentQ()
        self.trailer=Trailer()

    def updateTrailer(self):
        self.trailer.update(segment=self.segmentP)

    def toString(self):
        return "%s\r\n%s\r\n%s\r\n%s" % (self.header.toString(), self.segmentP.toString(), self.segmentQ.toString(), self.trailer.toString())

    def setPositionInLot(self, index):
        self.header.setPositionInLot(index)
        self.segmentP.setPositionInLot(index)
        self.segmentQ.setPositionInLot(index)
        self.trailer.setPositionInLot(index)

    def setSender(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.segmentP.setSenderBank(user.bank)
        self.segmentQ.setSenderBank(user.bank)
        self.trailer.setSenderBank(user.bank)

    def setPayer(self, user):
        self.segmentQ.setPayer(user)
        self.segmentQ.setPayerAddress(user.address)

    def setAmountInCents(self, value):
        self.segmentP.setAmountInCents(value)

    def setExperationDate(self, date):
        self.segmentP.setExperationDate(date)

    def setIssueDate(self, date):
        self.header.setIssueDate(date)
        self.segmentP.setIssueDate(date)

    def setBankIdentifier(self, identifier, branch, accountNumber, wallet):
        dac = DAC.calculate(
            branch="{:0>4}".format(branch)[:4],
            accountNumber=accountNumber,
            wallet="{:0>3}".format(wallet)[:3],
            bankNumber="{:0>8}".format(identifier)[:8]
        )
        self.segmentP.setBankIdentifier(identifier, dac)

    def setIdentifier(self, identifier):
        self.segmentP.setIdentifier(identifier)
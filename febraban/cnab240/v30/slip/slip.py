from ...libs.dac import DAC
from .segmentP import SegmentP
from .segmentQ import SegmentQ


class SlipV30:

    def __init__(self):
        self.segmentP=SegmentP()
        self.segmentQ=SegmentQ()

    def toString(self):
        return "%s\r\n%s" % (self.segmentP.content, self.segmentQ.content)

    def amountInCents(self):
        return self.segmentP.amountInCents()

    def setPositionInLot(self, index):
        self.segmentP.setPositionInLot(index)
        self.segmentQ.setPositionInLot(index+1)

    def setSender(self, user):
        self.segmentP.setSenderBank(user.bank)
        self.segmentQ.setSenderBank(user.bank)

    def setPayer(self, user):
        self.segmentQ.setPayer(user)
        self.segmentQ.setPayerAddress(user.address)

    def setAmountInCents(self, value):
        self.segmentP.setAmountInCents(value)

    def setExpirationDate(self, datetime):
        self.segmentP.setExpirationDate(datetime.strftime("%d%m%Y"))

    def setIssueDate(self, datetime):
        self.segmentP.setIssueDate(datetime.strftime("%d%m%Y"))

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
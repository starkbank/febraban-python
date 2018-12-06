from datetime import datetime
from ....libs.fileUtils import FileUtils
from .header import Header
from .headerLot import HeaderLot
from .trailer import Trailer
from .trailerLot import TrailerLot


class FileV30:

    def __init__(self):
        self.header = Header()
        self.headerLot = HeaderLot()
        self.registers = []
        self.trailerLot = TrailerLot()
        self.trailer = Trailer()
        self.issueDate = datetime.now()
        self.amount = 0
        self.index = 1

    def add(self, register):
        register.setIssueDate(datetime=self.issueDate)
        register.setPositionInLot(index=self.index)
        self.registers.append(register.toString())
        self.amount += register.amountInCents()
        self.index += 2

    def toString(self):
        self.trailer.setNumberOfLotsAndRegisters(num=len(self.registers))
        self.trailerLot.setNumberOfLotsAndRegisters(num=len(self.registers))
        self.trailerLot.setSumOfValues(sum=self.amount)
        lotsToString = "\r\n".join(self.registers)
        return "%s\r\n%s\r\n%s\r\n%s\r\n%s\r\n" % (
            self.header.content,
            self.headerLot.content,
            lotsToString,
            self.trailerLot.content,
            self.trailer.content
        )

    def setSender(self, sender):
        self.header.setSender(sender)
        self.header.setSenderBank(sender.bank)
        self.headerLot.setSender(sender)
        self.headerLot.setSenderBank(sender.bank)
        self.trailer.setSenderBank(sender.bank)
        self.trailerLot.setSenderBank(sender.bank)

    def setIssueDate(self, datetime):
        self.issueDate = datetime
        self.header.setGeneratedFileDate(datetime)
        self.headerLot.setGeneratedFileDate(datetime)

    def output(self, fileName, path="/../", content=None):
        file = FileUtils.create(name=fileName, path=path)
        file.write(self.toString() if not content else content)
        file.close()
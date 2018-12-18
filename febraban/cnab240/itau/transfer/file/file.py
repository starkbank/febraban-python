from datetime import datetime
from ....libs.fileUtils import FileUtils
from .header import Header
from .trailer import Trailer


class File:

    def __init__(self):
        self.header = Header()
        self.lots = []
        self.trailer = Trailer()

    def add(self, lot):
        lot.setPositionInLot(index=len(self.lots)+1)
        self.lots.append(lot.toString())

    def toString(self, currentDatetime=None):
        self.header.setGeneratedFileDate(currentDatetime or datetime.now())
        self.trailer.setNumberOfLotsAndRegisters(num=len(self.lots))
        lotsToString = "\r\n".join(self.lots)
        return "%s\r\n%s\r\n%s\r\n" % (self.header.content, lotsToString, self.trailer.content)

    def setSender(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.trailer.setSenderBank(user.bank)

    def output(self, fileName, path="/../", content=None, currentDatetime=None):
        file = FileUtils.create(name=fileName, path=path)
        file.write(self.toString(currentDatetime or datetime.now()) if not content else content)
        file.close()
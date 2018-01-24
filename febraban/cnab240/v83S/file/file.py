from ...libs.fileTools import FileTools
from .header import Header
from .trailer import Trailer


class FileV83:

    def __init__(self):
        self.header = Header()
        self.lots = []
        self.trailer = Trailer()

    def add(self, lot):
        lot.setPositionInLot(index=len(self.lots)+1)
        self.lots.append(lot.toString())

    def toString(self):
        self.header.setGeneratedFileDate()
        self.trailer.setNumberOfLotsAndRegisters(num=len(self.lots))
        lotsToString = "\r\n".join(self.lots)
        return "%s\r\n%s\r\n%s\r\n" % (self.header.content, lotsToString, self.trailer.content)

    def setUser(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.trailer.setSenderBank(user.bank)

    def output(self, fileName, path="/../", content=None):
        file = FileTools.create(name=fileName, path=path)
        file.write(self.toString() if not content else content)
        file.close()
from .libs.fileTools import FileTools


class File:

    def __init__(self, header, trailer):
        self.header = header
        self.lots = []
        self.trailer = trailer

    def add(self, lot):
        self.lots.append(lot)
        lot.setPositionInLot(index=len(self.lots))

    def updateTrailers(self):
        for lot in self.lots:
            lot.updateTrailer()
        self.trailer.update(lots=self.lots)

    def toString(self):
        self.header.update()
        self.updateTrailers()
        lotsToString = "\r\n".join([lot.toString() for lot in self.lots])
        centerString = "%s\r\n" % lotsToString if lotsToString else ""
        return "%s\r\n%s%s\r\n" % (self.header.toString(), centerString, self.trailer.toString())

    def setSender(self, user):
        self.header.setUser(user)
        self.header.setUserBank(user.bank)
        self.trailer.setUserBank(user.bank)

    def output(self, fileName, path="/../"):
        file = FileTools.create(name=fileName, path=path)
        file.write(self.toString())
        file.close()
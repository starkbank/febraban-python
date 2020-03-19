from datetime import datetime
from ....itau.sispag import Transfer, ChargePayment, UtilityPayment
from ....libs.fileUtils import FileUtils
from .header import Header
from .headerLot import HeaderLot
from .trailer import Trailer
from .trailerLot import TrailerLot


class File:

    def __init__(self):
        self.header = Header()
        self.headerLot = HeaderLot()
        self.registers = []
        self.trailerLot = TrailerLot()
        self.trailer = Trailer()
        self.amount = 0
        self.index = 1

    def add(self, register):
        register.setPositionInLot(index=self.index)
        self.registers.append(register)
        self.amount += register.amountInCents()
        self.index += 1

    def setHeaderLotType(self, kind="20", method="41"):
        """
        Trasfers:
            kind:   String - Kind of payment - 20 Fornecedores, read: NOTES 4
            method: String - Payment method  - 41 TED Outro titular, 43 TED Mesmo titular, 01 ITAU account. read: NOTES 5

        Charge-payments:
            kind:   String - Kind of payment - 98 Diversos, read: NOTES 4
            method: String - Payment method  - 30 Pagamento Boleto Itau, 31 Pagamento Boleto outros Bancos. read: NOTES 5

        Utilities:
            kind:   String - Kind of payment - 98 Diversos, read: NOTES 4
            method: String - Payment method  - 13 Concessionarias. read: NOTES 5
        """
        self.headerLot.setInfo(kind, method)

    def toString(self, currentDatetime=None):
        self.header.setGeneratedFileDate(currentDatetime or datetime.now())
        self.trailer.setNumberOfLotsAndRegisters(
            sum=4 + self._count(Transfer) + 2 * self._count(ChargePayment) + self._count(UtilityPayment)
        )
        self.trailerLot.setLotNumberOfRegisters(
            sum=2 + self._count(Transfer) + 2 * self._count(ChargePayment) + self._count(UtilityPayment)
        )
        self.trailerLot.setSumOfValues(sum=self.amount)
        registersToString = "\r\n".join([register.toString() for register in self.registers])
        return "%s\r\n%s\r\n%s\r\n%s\r\n%s\r\n" % (
            self.header.content,
            self.headerLot.content,
            registersToString,
            self.trailerLot.content,
            self.trailer.content
        )

    def setSender(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.headerLot.setSender(user)
        self.headerLot.setSenderBank(user.bank)
        self.headerLot.setSenderAddress(user.address)
        self.trailer.setSenderBank(user.bank)
        self.trailerLot.setSenderBank(user.bank)

    def output(self, fileName, path="/../", content=None, currentDatetime=None):
        file = FileUtils.create(name=fileName, path=path)
        file.write(self.toString(currentDatetime or datetime.now()) if not content else content)
        file.close()

    def _count(self, cls):
        return len([register for register in self.registers if isinstance(register, cls)])

from .headerLot import HeaderLot
from .trailerLot import TrailerLot
from ....itau.sispag import Transfer, ChargePayment, BarCodePayment


class Lot:

    def __init__(self):
        self.headerLot = HeaderLot()
        self.registers = []
        self.trailerLot = TrailerLot()
        self.amount = 0
        self.index = 1
        self.count = 0

    def add(self, register):
        register.setPositionInLot(index=self.index)
        self.registers.append(register)
        self.amount += register.amountInCents()
        self.index += 1

    def setLotNumber(self, index):
        self.headerLot.setPositionInLot(index)
        self.trailerLot.setPositionInLot(index)
        for register in self.registers:
            register.setLot(index)

    def setSender(self, sender):
        self.headerLot.setSender(sender)
        self.headerLot.setSenderBank(sender.bank)
        self.headerLot.setSenderAddress(sender.address)
        self.trailerLot.setSenderBank(sender.bank)

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

        Tax-payments:
            kind:   String - Kind of payment - 22 Tributos, read: NOTES 4
            method: String - Payment method  - 91 GNRE e Tributos com Codigo de Barras,
                                               19 IPTU/ISS/Outros Tributos Municipais. read: NOTES 5,
                                               16 DARF (No barcode)

        """
        self.headerLot.setInfo(kind, method)

    def toString(self):
        self.count = 2 + self._count(Transfer) + 2 * self._count(ChargePayment) + self._count(BarCodePayment)
        self.trailerLot.setLotNumberOfRegisters(
            num=self.count
        )
        self.trailerLot.setSumOfValues(sum=self.amount)
        registersToString = "\r\n".join([register.toString() for register in self.registers])
        return "%s\r\n%s\r\n%s" % (
            self.headerLot.content,
            registersToString,
            self.trailerLot.content,
        )

    def _count(self, cls):
        return len([register for register in self.registers if isinstance(register, cls)])



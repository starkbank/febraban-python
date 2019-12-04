from febraban.cnab240.itau.sispag.payment.header import Header
from febraban.cnab240.itau.sispag.payment.segmentNfgts import SegmentNFGTS
from febraban.cnab240.itau.sispag.payment.taxesTrailer import TaxesTrailer


class FgstsPayment:

    def __init__(self):
        self.header = Header(layoutNum="030")
        self.segmentN = SegmentNFGTS()
        self.trailer = TaxesTrailer()

    def toString(self):
        return "\r\n".join((
            self.header.content,
            self.segmentN.content,
            self.trailer.content,
        ))

    def setSender(self, user):
        self.header.setSender(user)
        self.header.setSenderBank(user.bank)
        self.header.setSenderAddress(user.address)
        self.segmentN.setSenderBank(user.bank)
        self.trailer.setSenderBank(user.bank)

    def setTypeTaxId(self, id="11"):
        self.segmentN.setTypeTaxId(id)

    def setPaymentId(self, id):
        self.segmentN.setPaymentId(id)

    def setTaxId(self, CNPJ):
        self.segmentN.setTaxId(CNPJ)

    def setTaxType(self, id="2"):
        self.segmentN.setTaxType(id)

    def setBarcode(self, barcode):
        self.segmentN.setBarcode(barcode)

    def setPaymentDate(self):
        self.segmentN.setPaymentDate()

    def setAmount(self, amount):
        self.segmentN.setAmount(amount)
        self.trailer.setAmountInCents(amount)
        # self.trailer.setSumOthersAmountInCents("0")
        self.trailer.setActualAmountInCents("0")
        self.trailer.setSumAmountInCents(amount)

    def setLacre(self, lacre):
        self.segmentN.setLacre(lacre)

    def setDigLacre(self, digLacre):
        self.segmentN.setDigLacre(digLacre)

    def setPositionInLot(self, index):
        self.header.setPositionInLot(index)
        self.trailer.setPositionInLot(index)
        self.trailer.setLotNumberOfRegisters(3)

    def setTaxPayer(self, taxPayer):
        self.segmentN.setTaxPayer(taxPayer)

    def setFgtsIdentifier(self, fgtsId):
        self.segmentN.setFgtsIdentifier(fgtsId)

    def setIdentifier(self, identifier):
        self.segmentN.setIdentifier(identifier)

    def setInfo(self, kind="22", method="35"):
        """
        This method set config information in the payment
        Args:
            kind:   String - Kind of payment - 22 Tributos, Nota 4
            method: String - Payment method  - 35 FGTS - GIP. Nota 5
        """
        self.header.setInfo(kind, method)

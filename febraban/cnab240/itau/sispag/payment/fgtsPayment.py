from .header import Header
from .segmentNFgts import SegmentNFgts
from .taxesTrailer import TaxesTrailer


class FgtsPayment:

    def __init__(self):
        self.header = Header(layoutNum="030")
        self.segmentN = SegmentNFgts()
        self.trailer = TaxesTrailer()

    def setPayment(self, **kwargs):
        self.setSender(kwargs.get("sender"))
        self.setTypeTaxId()
        self.setTaxType(id="1")
        self.setPaymentId(id="115")
        self.setBarcode(kwargs.get("barCode"))
        self.setTaxId(kwargs.get("taxId"))
        self.setPaymentDate()
        self.setTaxPayer(kwargs.get("sender").name)
        # self.setFgtsIdentifier(kwargs.get("taxCode")) # ToDo verify if is necessary
        # self.setLacre("017980")  # ToDo verify if is necessary
        # self.setDigLacre("9") # ToDo verify if is necessary
        self.setInfo()
        self.setAmount(kwargs.get("amount"))
        self.setIdentifier(kwargs.get("identifier"))

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

    def setTaxType(self, id="1"):
        self.segmentN.setTaxType(id)

    def setBarcode(self, barcode):
        self.segmentN.setBarcode(barcode)

    def setPaymentDate(self):
        self.segmentN.setPaymentDate()

    def setAmount(self, amount):
        self.segmentN.setAmount(amount)
        self.trailer.setAmountInCents(amount)
        self.trailer.setActualAmountInCents(amount)
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

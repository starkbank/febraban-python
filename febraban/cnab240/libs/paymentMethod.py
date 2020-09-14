from febraban.cnab240.libs.enum import Enum


class PaymentMethod(Enum):
    # NOTA 5 (Page 38)
    utility = "13"
    darf = "16"
    gps = "17"
    das = "18"
    municipal = "19"
    darj = "21"
    gare = "22"
    ipva = "25"
    dpvat = "27"
    itau = "30"
    other = "31"
    receipt = "32"
    fgts = "35"
    tedOther = "41"
    tedSame = "43"
    salaryCard = "60"
    barcode = "91"

    @classmethod
    def taxes(cls):
        return [cls.darf, cls.gps, cls.das, cls.municipal, cls.darj, cls.gare, cls.ipva, cls.dpvat, cls.fgts]

    @classmethod
    def nonBarcodeTaxes(cls):
        return [cls.darf, cls.gps, cls.das, cls.darj, cls.gare, cls.ipva, cls.dpvat, cls.fgts]


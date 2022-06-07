from febraban.cnab240.libs.enum import Enum


class BarcodePayment(Enum):

    utility = "utility"
    iss = "iss"
    das = "das"
    gps = "gps"
    darf = "darf"
    fgts = "fgts"


class NonBarcodeTaxPayment(Enum):

    gps = "gps-n"
    darf = "darf-n"

from febraban.cnab240.libs.enum import Enum


class PaymentKind(Enum):

    # NOTA 4 (Page 38)
    dividend = "15"
    vendor = "20"
    tribute = "22"
    salary = "30"
    investmentFund = "40"
    insurance = "50"
    travel = "60"
    representative = "80"
    benefits = "90"
    diverse = "98"




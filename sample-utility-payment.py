
# coding: utf-8

from febraban.cnab240.itau.sispag import UtilityPayment, File
from febraban.cnab240.libs.barCode import LineNumberO
from febraban.cnab240.user import User, UserAddress, UserBank


sender = User(
    name="YOUR COMPANY NAME HERE",
    identifier="12345678901234",
    bank=UserBank(
        bankId="341",
        branchCode="4321",
        accountNumber="12345678",
        accountVerifier="9"
    ),
    address=UserAddress(
        streetLine1="AV PAULISTA 1000",
        city="SAO PAULO",
        stateCode="SP",
        zipCode="01310000"
    )
)

lineNumber = LineNumberO("846800000012349701090114004112370844901232603900")

file = File()
file.setHeaderLotType(
     kind="98",   # Tipo de pagamento - Diversos
     method="13"  # Concessionarias
)
file.setSender(sender)

payment = UtilityPayment()
payment.setPayment(
    sender=sender,
    scheduleDate="18032020",
    identifier="ID1234567890",
    lineNumber=lineNumber
)

file.add(register=payment)

file.output(fileName="output.REM", path="/../../")


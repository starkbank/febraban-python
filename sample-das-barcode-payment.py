# coding: utf-8

from febraban.cnab240.itau.sispag import DasPayment, File
from febraban.cnab240.itau.sispag.file.lot import Lot
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

lineNumbers = [
    "858000000275581712382016500711231320312356470477"
]

file = File()
file.setSender(sender)

lot = Lot()
lot.setSender(sender)
lot.setHeaderLotType(
    kind="22",
    method="91"
)

for lineNumber in lineNumbers:
    print lineNumber

    lineNumber = LineNumberO(lineNumber)

    payment = DasPayment()
    payment.setPayment(
        sender=sender,
        scheduleDate="27052020",
        identifier="ID1234567890",
        lineNumber=lineNumber
    )

    lot.add(register=payment)

file.addLot(lot)
file.output(fileName="output.REM", path="/../../")


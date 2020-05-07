
# coding: utf-8

from febraban.cnab240.itau.sispag import UtilityPayment, File
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
    "836000000015522801380034710717288116000212965610",
    "836400000011079401380070610530261110080671594119",
    "836100000022434201380079213410922115000104587191",
]

file = File()
file.setSender(sender)

lot = Lot()
lot.setSender(sender)
lot.setHeaderLotType(
    kind="98",
    method="13"
)

for lineNumber in lineNumbers:
    print lineNumber

    lineNumber = LineNumberO(lineNumber)

    payment = UtilityPayment()
    payment.setPayment(
        sender=sender,
        scheduleDate="20032020",
        identifier="ID1234567890",
        lineNumber=lineNumber
    )

    lot.add(register=payment)

file.addLot(lot)
file.output(fileName="output.REM", path="/../../")


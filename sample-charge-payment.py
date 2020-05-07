
# coding: utf-8

from febraban.cnab240.itau.sispag import ChargePayment, File
from febraban.cnab240.itau.sispag.file.lot import Lot
from febraban.cnab240.libs.barCode import BarCodeJ
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

barCodes = [
    "34112318100000000011090027345767456112367000",
    "34112318100000000021090027345687456112367000",
    "34112318100000000031090027345507456112367000",
]

taxIds = [
    "12345678901234",
    "12345678901234",
    "12345678901234",
]

file = File()
file.setSender(sender)

lot = Lot()
sender.name = "SENDER NAME"
lot.setSender(sender)
lot.setHeaderLotType(
    kind="98",
    method="30"
)

for barCodeString, taxId in zip(barCodes, taxIds):
    barCode = BarCodeJ(barCodeString)

    payment = ChargePayment()
    payment.setSender(sender)
    payment.setScheduleDate("26022020")
    payment.setIdentifier("ID1234567890")
    payment.setBarCode(barCode)
    payment.setReceiverTaxId(taxId)

    lot.add(register=payment)

file.addLot(lot)
file.output(fileName="output.REM", path="/../../")


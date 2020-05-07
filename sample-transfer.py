
# coding: utf-8

from febraban.cnab240.itau.sispag import Transfer, File
from febraban.cnab240.itau.sispag.file.lot import Lot
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

receiver1 = User(
    name="RECEIVER NAME HERE",
    identifier="01234567890",
    bank=UserBank(
        bankId="341",
        branchCode="1234",
        accountNumber="123456",
        accountVerifier="9"
    )
)

receiver2 = User(
    name="RECEIVER NAME HERE",
    identifier="01234567890",
    bank=UserBank(
        bankId="341",
        branchCode="1234",
        accountNumber="123456",
        accountVerifier="9"
    )
)

receivers = [receiver1, receiver2]

file = File()
file.setSender(sender)

lot = Lot()
sender.name = "SENDER NAME"
lot.setSender(sender)
lot.setHeaderLotType(
    kind="20",  #Tipo de pagamento - Fornecedores
    method="01" #TED - Outra titularidade
)

for receiver in receivers:
    payment = Transfer()
    payment.setSender(sender)
    payment.setReceiver(receiver)
    payment.setAmountInCents("10000")
    payment.setScheduleDate("06052020")
    payment.setInfo(
        reason="10"  #Crédito em Conta Corrente
    )
    payment.setIdentifier("ID1234567890")
    lot.add(register=payment)

file.addLot(lot)
file.output(fileName="output.REM", path="/../../")


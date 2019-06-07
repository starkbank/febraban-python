
# coding: utf-8

from febraban.cnab240.itau.sispag import ChargePayment, File
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

file = File()
file.setSender(sender)

payment = ChargePayment()
payment.setSender(sender)
payment.setBarCode("34192791100000020001090000229827307144464000")
payment.setScheduleDate("08062019")
payment.setIdentifier("ID1234567890")
payment.setInfo(
    kind="98",   # Tipo de pagamento - Diversos
    method="30", # Pagamento de Boleto mesmo banco
)

file.add(lot=payment)

file.output(fileName="output3.REM", path="/../../")


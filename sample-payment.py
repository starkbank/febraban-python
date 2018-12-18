
# coding: utf-8

from febraban.cnab240.itau.transfer import Payment, File
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

receiver = User(
    name="RECEIVER NAME HERE",
    identifier="12345678901",
    bank=UserBank(
        bankId="033",
        branchCode="1234",
        accountNumber="123456",
        accountVerifier="7"
    )
)

file = File()
file.setSender(sender)

payment = Payment()
payment.setSender(sender)
payment.setReceiver(receiver)
payment.setAmountInCents("12000")
payment.setScheduleDate("12102017")
payment.setInfo(
    kind="98",   #Tipo de pagamento - Diversos
    method="41", #TED - Outra titularidade
    reason="10"  #Crédito em Conta Corrente
)
payment.setIdentifier("ID1234567890")
file.add(lot=payment)

file.output(fileName="output.REM", path="/../../")
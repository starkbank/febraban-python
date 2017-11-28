
# coding: utf-8

from febraban.cnab240.user import User, UserAddress, UserBank
from febraban.cnab240.v83.file.file import FileV83
from febraban.cnab240.v83.payment.payment import PaymentV83


myself = User(
    name="YOUR COMPANY NAME HERE",
    identifier="12345678901234",
    bank=UserBank(
        bankId="341",
        branchCode="4321",
        accountNumber="12345678",
        accountVerifier="9"
    ),
    address=UserAddress(
        streetName="AV PAULISTA",
        number="1000",
        city="SAO PAULO",
        state="SP",
        zipcode="01310000"
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

file = FileV83()
file.setUser(myself)

payment = PaymentV83()
payment.setSender(myself)
payment.setReceiver(receiver)
payment.setAmountInCents("12000")
payment.setScheduleDate("12102017")
payment.setInfo(
    kind="98",   #Tipo de pagamento - Diversos
    method="41", #TED - Outra titularidade
    reason="10"  #Crédito em Conta Corrente
)

file.add(lot=payment)

file.output(fileName="output-payment.REM")
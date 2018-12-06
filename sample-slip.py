# coding: utf-8

from datetime import datetime
from febraban.cnab240.itau.slipV30 import SlipV30, FileV30
from febraban.cnab240.user import User, UserAddress, UserBank


myself = User(
    name="YOUR COMPANY NAME",
    identifier="123456789012345",
    bank=UserBank(
        bankId="341",
        branchCode="1234",
        accountNumber="33333",
        accountVerifier="4",
        bankName="BANCO ITAU SA"
    ),
    address=UserAddress(
        streetLine1="AV PAULISTA 1000",
        streetLine2="CJ 601",
        city="SAO PAULO",
        stateCode="SP",
        zipCode="01310000"
    )
)

payer = User(
    name="PAYER NAME",
    identifier="12345678901",
    address=UserAddress(
        streetLine1="AV PAULISTA 1000",
        district="BELA VISTA",
        city="SAO PAULO",
        stateCode="SP",
        zipCode="01310000"
    )
)
now = datetime.now()

file = FileV30()
file.setSender(myself)
file.setIssueDate(now)

slip = SlipV30()
slip.setSender(myself)
slip.setAmountInCents("2000")
slip.setPayer(payer)
slip.setIssueDate(now)
slip.setExpirationDate(now)
slip.setBankIdentifier(
    identifier="1",
    branch=myself.bank.branchCode,
    accountNumber=myself.bank.accountNumber,
    wallet="109"
)
slip.setIdentifier("ID456")
file.add(register=slip)

file.output(fileName="output.REM", path="/../../")

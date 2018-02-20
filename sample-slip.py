# coding: utf-8

from datetime import datetime
from febraban.cnab240.user import User, UserAddress, UserBank
from febraban.cnab240.v30.file.file import FileV30
from febraban.cnab240.v30.slip.slip import SlipV30


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
        streetName="AV PAULISTA",
        number="1000",
        complement="CJ 601",
        city="SAO PAULO",
        state="SP",
        zipcode="01310000"
    )
)

payer = User(
    name="PAYER NAME",
    identifier="12345678901",
    address=UserAddress(
        streetName="AV PAULISTA",
        number="1000",
        district="BELA VISTA",
        city="SAO PAULO",
        state="SP",
        zipcode="01310000"
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

file.output(fileName="output.REM")

# coding: utf-8

from datetime import datetime
from febraban.cnab240.itau.charge import Slip, File
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

expiration = datetime(day=25, month=07, year=2019)
interestDate = datetime(day=26, month=07, year=2019)
orignalDate = datetime(day=20, month=07, year=2019)
file = File()
file.setSender(myself)
file.setIssueDate(datetime=None)


# Update dueDate
slip1 = Slip()
slip1.setSender(myself)
slip1.setAmountInCents("133")
slip1.setBankIdentifier(
    identifier="2644",
    branch=myself.bank.branchCode,
    accountNumber=myself.bank.accountNumber,
    wallet="109"
)
slip1.setIdentifier("ID-123456")
slip1.chargeUpate(dueDate=expiration)


# Update Fine
slip2 = Slip()
slip2.setSender(myself)
slip2.setAmountInCents("133")
slip2.setBankIdentifier(
    identifier="2644",
    branch=myself.bank.branchCode,
    accountNumber=myself.bank.accountNumber,
    wallet="109"
)
slip2.setIdentifier("ID-123456")
slip2.chargeUpate(fine=300, fineDate=expiration)

# Update Interest
slip3 = Slip()
slip3.setSender(myself)
slip3.setAmountInCents("133")
slip3.setBankIdentifier(
    identifier="2644",
    branch=myself.bank.branchCode,
    accountNumber=myself.bank.accountNumber,
    wallet="109"
)
slip3.setIdentifier("ID-123456")
slip3.chargeUpate(interest=10, interestDate=interestDate)  # 10 cents/day

# Update amount
slip4 = Slip()
slip4.setBankIdentifier(
    identifier="2644",
    branch=myself.bank.branchCode,
    accountNumber=myself.bank.accountNumber,
    wallet="109"
)
slip4.setIdentifier("ID-123456")
slip4.chargeUpate(amount=135)

# Create slips
file.add(register=slip1)
file.add(register=slip2)
file.add(register=slip3)
file.add(register=slip4)

print(file.toString())

file.output(fileName="output.REM", path="/../../")

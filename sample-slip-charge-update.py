# coding: utf-8

from datetime import datetime, timedelta
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
now = datetime.now()
#expiration = now + timedelta(days=1)
expiration = datetime(day=22, month=07, year=2019)
orignalDate = datetime(day=20, month=07, year=2019)
file = File()
file.setSender(myself)
file.setIssueDate(now)

# # Update dueDate
# slip1 = Slip()
# slip1.setSender(myself)
# slip1.setAmountInCents("113")
# slip1.setPayer(payer)
# #slip1.setIssueDate(now)
# #slip1.setExpirationDate(expiration)
# slip1.setBankIdentifier(
#     identifier="2643",
#     branch=myself.bank.branchCode,
#     accountNumber=myself.bank.accountNumber,
#     wallet="109"
# )
# slip1.setIdentifier("PRD-5207112409939968")
# #slip1.setFineAndInterest(datetime=expiration, fine="0", interest="0")
# #slip1.setOverdueLimit("3")
# slip1.chargeUpate(dueDate=expiration)


# Update Fine
slip2 = Slip()
slip2.setSender(myself)
slip2.setAmountInCents("133")
slip2.setPayer(payer)
slip2.setExpirationDate(orignalDate)
slip2.setBankIdentifier(
    identifier="2644",
    branch=myself.bank.branchCode,
    accountNumber=myself.bank.accountNumber,
    wallet="109"
)
slip2.setIdentifier("PRD-5917955804102656")
slip2.chargeUpate(fine=50, fineDate=expiration)


# # Update amount
# slip3 = Slip()
# slip3.setSender(myself)
# slip3.setPayer(payer)
# # slip3.setIssueDate(now)
# slip3.setExpirationDate(orignalDate)
# slip3.setBankIdentifier(
#     identifier="2613",
#     branch=myself.bank.branchCode,
#     accountNumber=myself.bank.accountNumber,
#     wallet="109"
# )
# slip3.setIdentifier("PRD-5701383420379136")
# slip3.chargeUpate(amount=125)

# Create slips
# file.add(register=slip1)
file.add(register=slip2)
# file.add(register=slip3)

file.output(fileName="update5.REM", path="/../../")

from datetime import datetime
from febraban.cnab240.bradesco.multipag.file.lot import Lot
from febraban.cnab240.bradesco.multipag.file.file import File
from febraban.cnab240.libs.paymentKind import PaymentKind
from febraban.cnab240.libs.paymentMethod import PaymentMethod
from febraban.cnab240.user import User, UserAddress, UserBank
from febraban.cnab240.bradesco.multipag.payment.darfPayment import DarfPayment


myself = User(
    name="STARK BANK SA",
    identifier="20018183000180",
    bank=UserBank(
        bankId="237",
        branchCode="0156",
        accountNumber="000000060279",
        accountVerifier="5",
        bankName="BANCO BRADESCO SA",
        bankAgreement="610242"
    ),
    address=UserAddress(
        streetLine1="AV PAULISTA 1000",
        streetLine2="CJ 601",
        city="SAO PAULO",
        stateCode="SP",
        zipCode="01310000"
    )
)

now = datetime.now()

file = File(sequenceNumber=1)
file.setSender(myself)

lot = Lot()
lot.setSender(myself)
lot.setHeaderLotType(
    kind=PaymentKind.tribute,
    method=PaymentMethod.darf
)
for i in range(1, 10):
    darfPayment = DarfPayment()
    amount = 10000 * i
    fine = 2000
    interest = 3000
    darfPayment.setPayment(
        sender=myself,
        taxId="34169054822",
        revenueCode="2089",
        referenceDate="19012025",
        referenceNumber="1234567890",
        amount=f"{amount}",
        fine=f"{fine}",
        interest=f"{interest}",
        totalAmount=f"{amount + fine + interest}",
        identifier="1234567890",
        dueDate="31122025",
        ourNumber=f"{i}",
    )
    darfPayment.setPaymentDate(datetime.now().strftime("%d%m%Y"))
    lot.add(register=darfPayment)


file.addLot(lot)
# file.add(register=lot)
file.output(fileName="output1.REM", path="/../../")
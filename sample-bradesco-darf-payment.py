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
for i in range(1,11):
    darfPayment = DarfPayment()
    amount = 100
    fine = 0
    interest = 0
    darfPayment.setPayment(
        sender=myself,
        taxId="34169054822",
        revenueCode="6621",
        referenceDate="24032026",
        referenceNumber="",
        amount=f"{amount}",
        fine=f"{fine}",
        interest=f"{interest}",
        totalAmount=f"{amount + fine + interest}",
        identifier=f"DEV-6291233349566464-{i}",
        dueDate="24032026",
    )
    darfPayment.setPaymentDate(datetime.now().strftime("%d%m%Y"))
    lot.add(register=darfPayment)


file.addLot(lot)
# file.add(register=lot)
file.output(fileName="TESTE.REM", path="/../../")
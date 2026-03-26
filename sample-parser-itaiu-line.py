from enum import Enum

class TransactionType(Enum):

    chargePayment = "charge-payment"
    barcodePayment = "barcode-payment"

    @classmethod
    def fromCorban(cls, paymentType):
        return {
            "020": TransactionType.barcodePayment,
            "067": TransactionType.chargePayment,
            "041": TransactionType.chargePayment,
        }.get(paymentType)

class RegisterType(Enum):

    header = "header"
    details = "details"
    trailer = "trailer"

    @classmethod
    def fromCorban(cls, corbanRegisterType):
        return {
            "1": RegisterType.header,
            "2": RegisterType.details,
            "3": RegisterType.trailer,
        }.get(corbanRegisterType)

class PaymentStatus(Enum):

    success = "success"
    failed = "failed"
    sent = "sent"

    @classmethod
    def fromCorban(cls, paymentResponseStatus):
        return {
            "0001": PaymentStatus.failed,
            "0002": PaymentStatus.sent,
            "0003": PaymentStatus.success,
            "0004": PaymentStatus.failed,
            "0005": PaymentStatus.failed,
        }.get(paymentResponseStatus)


def parseLines(lines):
        payments = []

        for line in lines:
            registerType = RegisterType.fromCorban(line[0])
            if registerType != RegisterType.details:
                print(line)
                continue

            payments.append({
                "transactionType": TransactionType.fromCorban(line[79:82]),
                "barcode": line[94:138],
                "corbanId": line[82:92].lstrip("0"),
                "amount": line[138:151].lstrip("0"),
                "status": PaymentStatus.fromCorban(line[151:155]),
                "errorCode": line[155:164].lstrip("0"),
            })

        return payments
lines = open("Teste.RET", "r").readlines()
result = parseLines(lines)
for payment in result:
    print(payment)
    print("-------------------------------------------------------------------")
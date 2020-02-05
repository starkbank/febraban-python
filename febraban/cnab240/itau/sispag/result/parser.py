from .occurrences import occurrences


class PaymentResponseStatus:

    success = "success"
    failed = "failed"
    scheduled = "scheduled"
    unknown = "unknown"


class PaymentType:

    transfer = "transfer"
    chargePayment = "charge-payment"
    taxPayment = "tax-payment"


class PaymentResponse:

    def __init__(self, identifier=None, occurrences=None, content=None, authentication=None, amountInCents=None, paymentType=None):
        self.identifier = identifier
        self.occurrences = occurrences
        self.content = content or []
        self.authentication = authentication
        self.amountInCents = amountInCents
        self.type = paymentType

    def occurrencesText(self):
        return [occurrences[occurrenceId] for occurrenceId in self.occurrences]

    def occurrencesTextAtIndex(self, index):
        occurrenceId = self.occurrences[index]
        return occurrences[occurrenceId]

    def status(self):
        if "00" in self.occurrences:
            return PaymentResponseStatus.success
        if "BD" in self.occurrences:
            return PaymentResponseStatus.scheduled
        if [code in self.occurrences for code in ["RJ", "DV"]].count(True) > 0:
            return PaymentResponseStatus.failed
        return PaymentResponseStatus.unknown

    def contentText(self, breakLine="\n"):
        return breakLine.join(self.content)


class PaymentParser:

    @classmethod
    def parseFile(cls, file):
        lines = file.readlines()
        return cls.parseLines(lines)

    @classmethod
    def parseText(cls, text):
        lines = text.splitlines()[:-1]
        return cls.parseLines(lines)

    @classmethod
    def parseLines(cls, lines):
        result = []
        for line in lines:
            if line[7] in ["0", "9"]:
                continue
            elif line[7] == "1":
                currentResponse = PaymentResponse(content=[line])
            elif line[7] == "3" and line[13] == "A":
                currentResponse.content.append(line)
                currentResponse.identifier = cls._getIdentifierTransfer(line)
                currentResponse.occurrences = cls._getOccurrences(line)
                currentResponse.amountInCents = cls._getAmountTransfer(line)
                currentResponse.type = PaymentType.transfer
            elif line[7] == "3" and line[13] == "J":
                currentResponse.content.append(line)
                currentResponse.identifier = cls._getIdentifierPayment(line)
                currentResponse.occurrences = cls._getOccurrences(line)
                currentResponse.amountInCents = cls._getAmountPayment(line)
                currentResponse.type = PaymentType.chargePayment
            elif line[7] == "3" and line[13] in ["N", "O"]:
                currentResponse.content.append(line)
                currentResponse.identifier = cls._getIdentifierPayment(line)
                currentResponse.occurrences = cls._getOccurrences(line)
                currentResponse.amountInCents = cls._getAmountPayment(line)
                currentResponse.type = PaymentType.taxPayment
            elif line[7] == "3" and line[13] == "Z":
                currentResponse.content.append(line)
                currentResponse.authentication = cls._getAuthentication(line)
            elif line[7] == "5":
                currentResponse.content.append(line)
                result.append(currentResponse)
                currentResponse = PaymentResponse()
        return result

    @classmethod
    def _getOccurrences(cls, line):
        occurrencesString = line[230:240].strip()
        return cls._splitString(occurrencesString)

    @classmethod
    def _splitString(cls, string):
        return [string[i:i+2] for i in range(0, len(string), 2)]

    @classmethod
    def _getAmountTransfer(cls, line):
        return int(line[119:134].strip())

    @classmethod
    def _getAmountPayment(cls, line):
        return int(line[152:167].strip())

    @classmethod
    def _getIdentifierTransfer(self, line):
        return line[73:93].strip()

    @classmethod
    def _getIdentifierPayment(self, line):
        return line[182:202].strip()

    @classmethod
    def _getAuthentication(cls, line):
        return line[14:78].strip()

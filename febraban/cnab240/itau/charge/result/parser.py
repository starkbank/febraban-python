from .occurrences import occurrences
from .errors import errors03, errors17, errors15, errors16, errors18


class SlipResponseStatus:

    registered = "registered"
    paid = "paid"
    canceled = "canceled"
    overdue = "overdue"
    failed = "failed"
    unknown = "unknown"


class SlipResponse:

    def __init__(self, identifier=None, occurrence=None, content=None, amountInCents=None, fine=None, errors=None):
        self.identifier = identifier
        self.occurrence = occurrence
        self.amountInCents = amountInCents
        self.fine = fine
        self.content = content or []
        self.errors = errors or []

    def occurrenceText(self):
        return occurrences[self.occurrence]

    def status(self):
        if self.occurrence == "02":
            return SlipResponseStatus.registered
        if self.occurrence in ["03", "15", "16", "17", "18"]:
            return SlipResponseStatus.failed
        if self.occurrence == "06":
            return SlipResponseStatus.paid
        if self.occurrence == "08":
            return SlipResponseStatus.paid
        if self.occurrence == "09":
            return SlipResponseStatus.canceled
        return SlipResponseStatus.unknown

    def contentText(self, breakLine="\n"):
        return breakLine.join(self.content)

    def failureErrors(self):
        errorDict = {
            "03": errors03,
            "15": errors15,
            "16": errors16,
            "17": errors17,
            "18": errors18,
        }.get(self.occurrence)

        if errorDict is None:
            return []

        errorMessages = [errorDict[errorCode] for errorCode in self.errors if errorCode != "00"]

        return errorMessages

    def amountPaid(self):
        if self.status() != SlipResponseStatus.paid:
            return 0

        return self.amountInCents + self.fine


class SlipParser:

    @classmethod
    def parseFile(cls, file):
        lines = file.readlines()
        return cls._parseLines(lines)

    @classmethod
    def parseText(cls, text):
        lines = text.splitlines()[:-1]
        return cls._parseLines(lines)

    @classmethod
    def _parseLines(cls, lines):
        result = []
        for line in lines:
            if line[7] == "1":
                currentResponse = SlipResponse()
            elif line[7] == "3":
                currentResponse.content.append(line)
            if line[13] == "T":
                currentResponse.amountInCents = int(line[81:96])
                currentResponse.occurrence = line[15:17]
                currentResponse.identifier = line[105:130].strip()
                currentResponse.errors = [line[213 + i:215 + i] for i in range(0, 8, 2) if line[i:i + 2] != "  "]
            elif line[13] == "U":
                currentResponse.fine = int(line[17:32])
                result.append(currentResponse)
                currentResponse = SlipResponse()
            elif line[13] == "P":
                currentResponse.amountInCents = int(line[85:100])
                currentResponse.occurrences = [line[15:17]]
                currentResponse.identifier = line[195:220].strip()
            elif line[13] == "Q":
                result.append(currentResponse)
                currentResponse = SlipResponse()
        return result
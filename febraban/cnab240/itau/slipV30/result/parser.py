from .occurrences import occurrences


class SlipResponseStatus:

    registered = "registered"
    paid = "paid"
    canceled="canceled"
    overdue = "overdue"
    failed = "failed"
    unknown = "unknown"


class SlipResponse:

    def __init__(self, identifier=None, occurrences=None, content=None, amountInCents=None):
        self.identifier = identifier
        self.occurrences = occurrences
        self.amountInCents = amountInCents
        self.content = content or []

    def occurrencesText(self):
        return [occurrences[occurrenceId] for occurrenceId in self.occurrences]

    def occurrencesTextAtIndex(self, index):
        occurrenceId = self.occurrences[index]
        return occurrences[occurrenceId]

    def status(self):
        if "02" in self.occurrences:
            return SlipResponseStatus.registered
        if "03" in self.occurrences:
            return SlipResponseStatus.failed
        if "06" in self.occurrences:
            return SlipResponseStatus.paid
        if "08" in self.occurrences:
            return SlipResponseStatus.paid
        if "09" in self.occurrences:
            return SlipResponseStatus.canceled
        return SlipResponseStatus.unknown

    def contentText(self, breakLine="\n"):
        return breakLine.join(self.content)


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
                currentResponse.occurrences = [line[15:17]]
                currentResponse.identifier = line[105:130].strip()
            elif line[13] == "U":
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
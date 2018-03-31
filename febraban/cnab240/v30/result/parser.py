from .occurrences import occurrences


class SlipResponseStatus:

    registered = "registered"
    paid = "paid"
    overdue = "overdue"
    failed = "failed"
    unknown = "unknown"


class SlipResponse:

    def __init__(self, identifier, occurrences, content, amount):
        self.identifier = identifier
        self.occurrences = occurrences
        self.amountInCents = amount
        self.content = content

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
        return SlipResponseStatus.unknown

    def contentText(self):
        return "".join(self.content)


class SlipParser:

    @classmethod
    def parseFile(cls, file):
        lines = file.readlines()
        return cls.__parseLines(lines)

    @classmethod
    def parseText(cls, text, lineBreaker="\r\n"):
        lines = text.split(lineBreaker)[:-1]
        return cls.__parseLines(lines)

    @classmethod
    def __parseLines(cls, lines):
        result = []
        content = []
        identifier = None
        occurrences = None
        amount = None
        for line in lines:
            if line[7] == "3":
                content.append(line)
            if line[13] == "T":
                amount = int(line[81:96])
                occurrences = [line[15:17]]
                identifier = line[58:68].strip()
            elif line[13] == "U":
                result.append(SlipResponse(
                    identifier=identifier,
                    occurrences=occurrences,
                    amount=amount,
                    content=content
                ))
            elif line[13] == "P":
                amount = int(line[85:100])
                occurrences = [line[15:17]]
                identifier = line[62:72].strip()
            elif line[13] == "Q":
                result.append(SlipResponse(
                    identifier=identifier,
                    occurrences=occurrences,
                    amount=amount,
                    content=content
                ))
        return result
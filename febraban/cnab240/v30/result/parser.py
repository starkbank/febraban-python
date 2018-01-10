from .occurrences import occurrences


class SlipResponseStatus:

    registered = "registered"
    paid = "paid"
    overdue = "overdue"
    failed = "failed"
    unknown = "unknown"


class SlipResponse:

    def __init__(self, identifier, occurrences):
        self.identifier = identifier
        self.occurrences = occurrences

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


class SlipParser:

    @classmethod
    def parseFile(cls, file):
        lines = file.readlines()
        return cls.__parseLines(lines)

    @classmethod
    def parseText(cls, text):
        lines = text.split("\r\n")[:-1]
        return cls.__parseLines(lines)

    @classmethod
    def __parseLines(cls, lines):
        result = []
        for line in lines:
            if line[13] == "T":
                result.append(SlipResponse(
                    identifier=cls.__getIdentifier(line),
                    occurrences=cls.__getOccurrences(line)
                ))
        return result

    @classmethod
    def __getOccurrences(cls, line):
        return [line[15:17]]

    @classmethod
    def __getIdentifier(self, line):
        return int(line[40:48])
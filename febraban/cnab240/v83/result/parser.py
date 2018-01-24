from .occurrences import occurrences


class PaymentResponseStatus:

    success = "success"
    failed = "failed"
    scheduled = "scheduled"
    unknown = "unknown"


class PaymentResponse:

    def __init__(self, identifier, occurrences, content):
        self.identifier = identifier
        self.occurrences = occurrences
        self.content = content

    def occurrencesText(self):
        return [occurrences[occurrenceId] for occurrenceId in self.occurrences]

    def occurrencesTextAtIndex(self, index):
        occurrenceId = self.occurrences[index]
        return occurrences[occurrenceId]

    def status(self):
        if "00" in self.occurrences:
            return PaymentResponseStatus.success
        if "RJ" in self.occurrences:
            return PaymentResponseStatus.failed
        if "BD" in self.occurrences:
            return PaymentResponseStatus.scheduled
        return PaymentResponseStatus.unknown

    def contentText(self):
        return "".join(self.content)


class PaymentParser:

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
        for line in lines:
            if line[7] in ["0","9"]:
                continue
            elif line[7] == "1":
                content = [line]
                identifier = None
                occurrences = None
            elif line[7] == "3":
                content.append(line)
                identifier = cls._getIdentifier(line)
                occurrences = cls._getOccurrences(line)
            elif line[7] == "5":
                content.append(line)
                result.append(PaymentResponse(
                    identifier=identifier,
                    occurrences=occurrences,
                    content=content
                ))

        return result

    @classmethod
    def _getOccurrences(cls, line):
        occurrencesString = line[230:240].replace(" ", "")
        return cls._splitString(occurrencesString)

    @classmethod
    def _splitString(cls, string):
        return [string[i:i+2] for i in range(0, len(string), 2)]

    @classmethod
    def _getIdentifier(self, line):
        return line[73:93].replace(" ", "")
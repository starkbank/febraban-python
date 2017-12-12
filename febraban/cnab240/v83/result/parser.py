from .occurrences import occurrences


class PaymentResponseStatus:
    Success = "Success"
    Failed = "Failed"
    Scheduled = "Scheduled"
    Unknown = "Unknown"


class PaymentResponse:

    def __init__(self, identifier, occurrences):
        self.identifier = identifier
        self.occurrences = occurrences

    def occurrencesText(self):
        return [occurrences[occurrenceId] for occurrenceId in self.occurrences]

    def occurrencesTextAtIndex(self, index):
        occurrenceId = self.occurrences[index]
        return occurrences[occurrenceId]

    def status(self):
        if "00" in self.occurrences:
            return PaymentResponseStatus.Success
        if "RJ" in self.occurrences:
            return PaymentResponseStatus.Failed
        if "BD" in self.occurrences:
            return PaymentResponseStatus.Scheduled
        return PaymentResponseStatus.Unknown


class PaymentParser:

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
            if line[7] == "3":
                result.append(PaymentResponse(
                    identifier=cls.__getIdentifier(line),
                    occurrences=cls.__getOccurrences(line)
                ))
        return result

    @classmethod
    def __getOccurrences(cls, line):
        occurrencesString = line[230:240].replace(" ", "")
        return cls.__splitString(occurrencesString)

    @classmethod
    def __splitString(cls, string):
        return [string[i:i+2] for i in range(0, len(string), 2)]

    @classmethod
    def __getIdentifier(self, line):
        return line[73:93].replace(" ", "")
from .characterType import numeric, alphaNumeric
from .libs.middlewares.row import validateInit, validateValue


class Row:

    def __init__(self):
        self.elements = []

    def toString(self):
        return "".join(map(lambda elem: elem.toString(), self.elements))


class RowElement:

    @validateInit
    def __init__(self, description, numberOfCharacters, charactersType, value, index):
        self.index = index
        self.description = description
        self.numberOfCharacters = numberOfCharacters
        self.charactersType = charactersType
        self.setValue(value)

    def value(self):
        return self.__value

    @validateValue
    def setValue(self, value):
        self.__value = value

    def toString(self):
        if self.value() is None:
            return {
                numeric:      "0" * self.numberOfCharacters,
                alphaNumeric: " " * self.numberOfCharacters
            }[self.charactersType]

        return self.__formatted(
            string=str(self.value()),
            charactersType=self.charactersType,
            numberOfCharacters=self.numberOfCharacters,
            defaultCharacter= "0" if self.charactersType == numeric else " "
        )

    def __formatted(self, string, charactersType, numberOfCharacters, defaultCharacter = " "):
        """
            This method fix the received String and a default complement according the alignment
            and cut the string if it' bigger than number of characters

            Args:
                string:             String to be completed
                charactersType:     Can be .numeric or .alphaNumeric
                numberOfCharacters: Integer that represents the max string len
                defaultCharacter:   Single string with default character to be completed if string is short
            Returns:
                String formatted
        """
        if type(string) != str:              return defaultCharacter * numberOfCharacters
        if len(string) > numberOfCharacters: return string[:numberOfCharacters]
        if charactersType == numeric:        return defaultCharacter * (numberOfCharacters - len(string)) + string
        if charactersType == alphaNumeric:   return string + defaultCharacter * (numberOfCharacters - len(string))
        return string
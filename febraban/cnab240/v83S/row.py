from ..libs.middlewares.row import validateFormatter
from ..characterType import numeric, alphaNumeric


class Row:

    @classmethod
    def setStructs(cls, structs, content):
        for (start, end, len, type, value) in structs:
            replacement = cls.__formatted(
                string=str(value),
                charactersType=type,
                numberOfCharacters=len,
                defaultCharacter= {numeric:"0", alphaNumeric:" "}[type]
            )
            content = content[:start] + replacement + content[start+len:]
        return content

    @classmethod
    @validateFormatter
    def __formatted(cls, string, charactersType, numberOfCharacters, defaultCharacter=" "):
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
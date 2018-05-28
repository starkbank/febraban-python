import re
from ...characterType import alphaNumeric, numeric


def validateFormatter(func):
   def wrapper(self, string, charactersType, numberOfCharacters, defaultCharacter):
       if type(numberOfCharacters) != int:
           raise ValueError("numberOfCharacters must be Integer")

       if charactersType not in [alphaNumeric, numeric]:
           raise ValueError("charactersType must be alphaNumeric or numeric")

       if not isinstance(string, str):
           raise ValueError("Type Value not allowed. Must be String. Used: %s " % str(type(string)))

       regex = {
           alphaNumeric: r'^[A-Za-z0-9\s\-]+$',
           numeric:      r'^[0-9]+$'
       }[charactersType]
       if string and not re.match(regex, string):
           raise ValueError("You add a non %s value" % self.charactersType)
       return func(self, string, charactersType, numberOfCharacters, defaultCharacter)
   return wrapper
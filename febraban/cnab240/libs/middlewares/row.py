from re import match
from ...characterType import alphaNumeric, numeric


def validateFormatter(func):
   def wrapper(self, string, charactersType, numberOfCharacters, defaultCharacter):
       if type(numberOfCharacters) != int:
           raise ValueError("numberOfCharacters must be Integer")

       if charactersType not in [alphaNumeric, numeric]:
           raise ValueError("charactersType must be alphaNumeric or numeric")

       if not isinstance(string, str):
           raise ValueError("(%s,%s) is not an allowed value. It must be string" % (str(string), str(type(string))))

       regex = {
           alphaNumeric: r'^[A-Za-z0-9\s\-]+$',
           numeric:      r'^[0-9]+$'
       }[charactersType]
       if string and not match(regex, string):
           raise ValueError("You add %s that is a non %s value" % (string, charactersType))
       return func(self, string, charactersType, numberOfCharacters, defaultCharacter)
   return wrapper
import re
from ...characterType import alphaNumeric, numeric


def validateInit(func):
   def wrapper(self, description, numberOfCharacters, charactersType, value=None, index=0):
       if type(numberOfCharacters) != int:
           raise ValueError("numberOfCharacters must be Integer")
       if charactersType not in [alphaNumeric, numeric]:
           raise ValueError("charactersType must be alphaNumeric or numeric")
       func(self, description, numberOfCharacters, charactersType, value, index)
   return wrapper


def validateValue(func):
   def wrapper(self, value):
       if type(value) not in [str, int, type(None)]:
           raise ValueError("Type Value not allowed. Must be String, Integer or None. Used: %s " % str(type(value)))
       regex = {
           alphaNumeric: r'^[A-Za-z0-9\s]+$',
           numeric:      r'^[0-9]+$'
       }[self.charactersType]
       if value and not re.match(regex, str(value)):
           raise ValueError("You add a non %s value" % self.charactersType)
       func(self, value)
   return wrapper

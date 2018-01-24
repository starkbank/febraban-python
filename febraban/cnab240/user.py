

class User:

    def __init__(self, name, identifier, bank=None, address=None):
        self.name = name
        self.identifier = identifier
        self.bank = bank
        self.address = address


class UserBank:

    def __init__(self, bankId, branchCode, accountNumber, accountVerifier, bankName=""):
        self.bankId = bankId
        self.bankName = bankName
        self.accountNumber = accountNumber
        self.branchCode = branchCode
        self.accountVerifier = accountVerifier


class UserAddress:

    def __init__(self, streetName, number, city, state, zipcode, district="", complement=""):
        self.streetName = streetName
        self.number = number
        self.complement = complement
        self.district = district
        self.city = city
        self.state = state
        self.zipcode = zipcode


class DAC:

    @classmethod
    def calculate(cls, branch, accountNumber, wallet, bankNumber):
        x1 = branch + accountNumber + wallet + bankNumber
        x2 = "12"*(len(x1)/2) + ("1" if len(x1)%2 == 1 else "")
        out = [int(a) * int(b) for (a,b) in zip(x1, x2)]
        s = sum(map(lambda x: x/10 + x%10, out))
        return (10 - s%10)%10
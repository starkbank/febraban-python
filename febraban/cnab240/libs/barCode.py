from datetime import date, timedelta


class BarCode:

    def __init__(self, number):
        self.number = number
        self.bankId = self.number[0:3]
        self.currency = self.number[3:4]
        self.dac = self.number[4:5]
        self.dueFactor = self.number[5:9]
        self.amount = self.number[9:19]
        self.freeField = self.number[19:44]
        self.baseDate = date(year=1997, month=10, day=7)
        self.dueDate = self.baseDate + timedelta(days=int(self.dueFactor))

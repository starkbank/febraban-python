from datetime import date, timedelta


class BarCodeJ:

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


class LineNumberO:

    def __init__(self, number):
        self.number = number
        self.productId = self.number[0:1]
        self.segmentId = self.number[1:2]
        self.currency = self.number[2:3]
        self.dac = self.number[3]
        self.dv1 = self.number[11]
        self.amount = self.number[4:11] + self.number[12:16]
        self.companyId = self.number[15:19]
        self.dv2 = self.number[23]
        self.dv3 = self.number[40]
        self.freeField = self.number[19:44]
        self.dv4 = self.number[47]

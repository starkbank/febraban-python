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
        self.productId = self.number[0]
        self.segmentId = self.number[1]
        self.currency = self.number[2]
        self.dac = self.number[3]
        self.dv1 = self.number[11]
        self.amount = self.number[4:11] + self.number[12:16]
        self.companyId = self.number[16:20]
        self.dv2 = self.number[23]
        self.dv3 = self.number[35]
        self.dv4 = self.number[47]
        self.freeField = self.number[20:23] + self.number[24:35] + self.number[36:47]

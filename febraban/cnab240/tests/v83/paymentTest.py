from unittest.case import TestCase
from febraban.cnab240.user import User, UserBank, UserAddress
from febraban.cnab240.v83.payment.header import Header
from febraban.cnab240.v83.payment.segmentA import SegmentA
from febraban.cnab240.v83.payment.trailer import Trailer


user = User(
    name="JOHN SMITH",
    identifier="12345678901",
)

bank = UserBank(
    bankId="341",
    branchCode="1234",
    accountNumber="1234567",
    accountVerifier="8"
)

address = UserAddress(
    streetName="AV PAULISTA",
    number="1000",
    city="SAO PAULO",
    state="SP",
    zipcode="01310000"
)


class PaymentTest(TestCase):

    def testHeaderLengh(self):
        string = Header().content
        self.assertEqual(len(string), 240)

    def testSegmentALengh(self):
        string = SegmentA().content
        self.assertEqual(len(string), 240)

    def testTrailerLengh(self):
        string = Trailer().content
        self.assertEqual(len(string), 240)

    def testHeaderDefaultValues(self):
        content = Header().content
        self.assertEqual(content[7:8], "1")
        self.assertEqual(content[8:9], "C")
        self.assertEqual(content[13:16], "040")

    def testSegmentADefaultValues(self):
        content = SegmentA().content
        self.assertEqual(content[7:8], "3")
        self.assertEqual(content[13:14], "A")

    def testTrailerDefaultValues(self):
        content = Trailer().content
        self.assertEqual(content[7:8], "5")

    def testHeaderSets(self):
        header = Header()
        header.setSender(user)
        header.setSenderBank(bank)
        header.setSenderAddress(address)
        header.setPositionInLot(2)
        header.setInfo(kind="88", method="99")
        response = "34100021C8899040 100012345678901                    01234 000001234567 8JOHN SMITH                                                            AV PAULISTA                   01000               SAO PAULO           01310000SP                  "
        self.assertEquals(header.content, response)

    def testSegmentASets(self):
        segment = SegmentA()
        segment.setSenderBank(bank)
        segment.setReceiver(user)
        segment.setReceiverBank(bank)
        segment.setAmountInCents(44400)
        segment.setPositionInLot(3)
        segment.setScheduleDate("10122017")
        segment.setInfo("99")
        response = "3410003300001A00000034101234 000001234567 8JOHN SMITH                                        10122017REA000000000000000000000000044400                    00000000000000000000000                    0000000001234567890199                     "
        self.assertEquals(segment.content, response)

    def testTrailerSets(self):
        trailer = Trailer()
        trailer.setAmountInCents(44400)
        trailer.setSenderBank(bank)
        trailer.setPositionInLot(5)
        response = "34100055         000003000000000000044400000000000000000000                                                                                                                                                                                     "
        self.assertEquals(trailer.content, response)
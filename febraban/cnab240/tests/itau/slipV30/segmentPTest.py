from unittest.case import TestCase
from febraban.cnab240.itau.slipV30.slip.segmentP import SegmentP
from febraban.cnab240.user import User, UserBank, UserAddress


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
    streetLine1="AV PAULISTA 1000",
    city="SAO PAULO",
    stateCode="SP",
    zipCode="01310000"
)


class SegmentPTest(TestCase):

    def testSegmentPlengh(self):
        string = SegmentP().content
        self.assertEqual(len(string), 240)

    def testSegmentPdefaultValues(self):
        content = SegmentP().content
        self.assertEqual(content[3:7], "0001")
        self.assertEqual(content[7:8], "3")
        self.assertEqual(content[13:14], "P")
        self.assertEqual(content[15:17], "01")
        self.assertEqual(content[37:40], "109")
        self.assertEqual(content[106:108], "99")
        self.assertEqual(content[108:109], "A")

    def testSegmentPsets(self):
        segment = SegmentP()
        segment.setPositionInLot(1)
        segment.setSenderBank(bank)
        segment.setAmountInCents(44400)
        segment.setExpirationDate("01022018")
        segment.setIssueDate("01012018")
        segment.setBankIdentifier(identifier="99999", dac="7")
        segment.setIdentifier("DEROMIR")
        response = "3410001300001P 0101234 000001234567 8109000999997        00000               0102201800000000004440000000099A01012018000000000000000000000000000000000000000000000000000000000000000000000000000000DEROMIR                  0001590000000000000 "
        self.assertEquals(segment.content, response)
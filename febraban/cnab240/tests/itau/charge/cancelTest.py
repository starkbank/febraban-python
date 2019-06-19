from unittest.case import TestCase
from febraban.cnab240.itau.charge import SegmentP, SegmentQ, SegmentR
from febraban.cnab240.user import User, UserBank, UserAddress


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

payer = User(
    name="ARYA STARK",
    identifier="12345678901",
)

guarantor = User(
    name="SACADOR",
    identifier="09876543210"
)


class CancelTest(TestCase):

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
        segment.setAmountInCents(22500)
        segment.setExpirationDate("01022018")
        segment.setIssueDate("01012018")
        segment.setBankIdentifier(identifier="99999", dac="7")
        segment.setIdentifier("VITAO")
        segment.setOverdueLimit(overdueLimit=59)
        segment.setCancel()
        response = "3410001300001P 0201234 000001234567 8109000999997        00000               0102201800000000002250000000099A01012018000000000000000000000000000000000000000000000000000000000000000000000000000000VITAO                    0001590000000000000 "
        self.assertEquals(segment.content, response)

    def testSegmentQsets(self):
        segment = SegmentQ()
        segment.setPositionInLot(1)
        segment.setSenderBank(bank)
        segment.setPayer(payer)
        segment.setPayerAddress(address)
        segment.setGuarantor(guarantor)
        segment.setCancel()
        response = "3410001300001Q 021000012345678901ARYA STARK                              AV PAULISTA 1000                                       01310000SAO PAULO      SP1000009876543210SACADOR                                 000                            "
        self.assertEquals(segment.content, response)

    def testSegmentRsets(self):
        segment = SegmentR()
        segment.setPositionInLot(1)
        segment.setSenderBank(bank)
        segment.setCancel()
        response = "3410001300001R 020000000000000000000000000000000000000000000000000                                                                                                                                     0000000000000000 000000000000  0         "
        self.assertEqual(segment.content, response)

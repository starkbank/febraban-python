from unittest.case import TestCase
from febraban.cnab240.libs.barCode import IptuBarCode
from febraban.cnab240.itau.sispag.payment.segmentO import SegmentO
from febraban.cnab240.user import User, UserBank, UserAddress
from febraban.cnab240.libs.dac import DAC


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


class SegmentOTest(TestCase):

    def testSegmenOPlengh(self):
        string = SegmentO().content
        self.assertEqual(len(string), 240)

    def testSegmentOdefaultValues(self):
        content = SegmentO().content
        self.assertEqual(content[3:7], "0001")
        self.assertEqual(content[7:8], "3")
        self.assertEqual(content[13:14], "O")
        self.assertEqual(content[14:17], "000")
        self.assertEqual(content[103:106], "REA")

    def testSegmentOsets(self):
        barCode = IptuBarCode("84610000000362700060002000102000000457986595")
        dac = DAC.calculateDacIptu(
            productId="8",
            segmentId="4",
            wallet="6",
            amount=barCode.amount,
            company=barCode.companyId,
            freeField=barCode.freeField
        )
        segment = SegmentO()
        segment.setPositionInLot(1)
        segment.setSenderBank(bank)
        segment.setBarCode(barCode=barCode, dac=dac)
        segment.setAmount(44400)
        segment.setDueDate("01022018")
        segment.setBankIdentifier(identifier="99999", dac="1")
        segment.setIdentifier("PMSP")
        response = "3410001300001P 0101234 000001234567 8109000999997        00000               0102201800000000004440000000099A01012018000000000000000000000000000000000000000000000000000000000000000000000000000000DEROMIR                  0001590000000000000 "
        self.assertEquals(segment.content, response)

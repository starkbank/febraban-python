from unittest.case import TestCase
from febraban.cnab240.itau.sispag import File
from febraban.cnab240.itau.sispag.payment.iptuPayment import IptuPayment
from febraban.cnab240.libs.barCode import IptuBarCode, LineNumber
from febraban.cnab240.itau.sispag.payment.segmentO import SegmentO
from febraban.cnab240.user import User, UserBank, UserAddress
from febraban.cnab240.libs.dac import DAC
from datetime import datetime


sender = User(
    name="JOHN SMITH",
    identifier="12345678901",
    bank=UserBank(
        bankId="341",
        branchCode="1234",
        accountNumber="1234567",
        accountVerifier="8"
    ),
    address=UserAddress(
        streetLine1="AV PAULISTA 1000",
        city="SAO PAULO",
        stateCode="SP",
        zipCode="01310000"
    )
)

expiration = datetime(day=21, month=9, year=2019)


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

    def testSegmentOLineNumber(self):
        lineNumber = LineNumber("816600000011376744242011909212099008000021791272")

        segment = SegmentO()
        segment.setPositionInLot(1)
        segment.setSenderBank(sender.bank)
        segment.setLineNumber(lineNumber.number)
        segment.setAmount(13767)
        segment.setDealerName(dealerName="PREFEITURA MUNICIPAL DE TABOAO DA SERRA")
        segment.setCurrencyAmount(currencyAmount="0")
        segment.setDueDate("21092019")
        segment.setIdentifier("IPTU-000001")
        response = "3410001300001O000816600000011376744242011909212099008000021791272PREFEITURA MUNICIPAL DE TABOAO21092019REA00000000000000000000000001376709122019000000000000000               IPTU-000001                                                       "
        self.assertEquals(segment.content, response)

    def testSegmentOBarCode(self):
        barCode = IptuBarCode("84610000000362700060002000102000000457986595")
        dac = DAC.calculateDacIptu(
            productId="8",
            segmentId="4",
            currency="6",
            amount=barCode.amount,
            company=barCode.companyId,
            freeField=barCode.freeField
        )

        segment = SegmentO()
        segment.setPositionInLot(1)
        segment.setSenderBank(sender.bank)
        segment.setBarCode(barCode=barCode, dac=dac)
        segment.setAmount(13767)
        segment.setDealerName(dealerName="PREFEITURA MUNICIPAL DE TABOAO DA SERRA")
        segment.setCurrencyAmount(currencyAmount="0")
        segment.setDueDate("21092019")
        segment.setIdentifier("IPTU-000001")
        response = "3410001300001O00084610000000362700060002000102000000457986595    PREFEITURA MUNICIPAL DE TABOAO21092019REA00000000000000000000000001376709122019000000000000000               IPTU-000001                                                       "
        self.assertEquals(segment.content, response)

    def testIptuPaymentBarCode(self):

        file = File()
        file.setSender(sender)
        barCode = IptuBarCode("84610000000362700060002000102000000457986595")
        payment = IptuPayment()
        payment.setSender(sender)
        payment.setBarCode(barCode=barCode)
        payment.setDueDate(expiration)
        payment.setInfo()
        payment.setDealerName(dealerName="PREFEITURA MUNICIPAL DE TABOAO DA SERRA")
        payment.setCurrencyAmount(currencyAmount="0")
        payment.setAmount(amount="000000000013767")
        payment.setIdentifier("IPTU-000001")
        expected = "341    1C2219030 100012345678901                    01234 000001234567 8JOHN SMITH                                                            AV PAULISTA 1000                                  SAO PAULO           01310000SP                  \r\n3410001300001O00084610000000362700060002000102000000457986595    PREFEITURA MUNICIPAL DE TABOAO21092019REA00000000000000000000000001376709122019000000000000000               IPTU-000001                                                       \r\n341    5               000000000000013767000000000000000000                                                                                                                                                                                     "
        self.assertEquals(payment.toString(), expected)

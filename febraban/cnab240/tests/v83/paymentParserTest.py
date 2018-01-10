from unittest.case import TestCase
from febraban.cnab240.v83.result.parser import PaymentParser


class PaymentParserTest(TestCase):

    def testSlitStringFull(self):
        string = "BDRJ00AEAG"
        self.assertEqual(PaymentParser._splitString(string), ["BD", "RJ", "00", "AE", "AG"])

    def testSlitStringEmpty(self):
        string = "  "*5
        self.assertEqual(PaymentParser._splitString(string), ["  ", "  ", "  ", "  ", "  "])

    def testSlitStringMixed(self):
        string = "BDRJ00    "
        self.assertEqual(PaymentParser._splitString(string), ["BD", "RJ", "00", "  ", "  "])

    def testGetOccurrences(self):
        line = " "*230 + "BDRJ00AE  "
        result = PaymentParser._getOccurrences(line)
        self.assertEqual(result, ["BD", "RJ", "00", "AE"])

    def testGetIdentifier(self):
        line = " " * 73 + "ID123456"
        result = PaymentParser._getIdentifier(line)
        self.assertEqual(result, "ID123456")

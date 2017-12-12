import unittest
from cnab240.v83.result.parser import PaymentParser


class PaymentParserTest(unittest.TestCase):

    def testSlitStringFull(self):
        string = "BDRJ00AEAG"
        self.assertEqual(PaymentParser._splitString(string), ["BD", "RJ", "00", "AE", "AG"])

    def testSlitStringEmpty(self):
        string = "  "*5
        self.assertEqual(PaymentParser._splitString(string), ["  ", "  ", "  ", "  ", "  "])

    def testSlitStringMixed(self):
        string = "BDRJ00    "
        self.assertEqual(PaymentParser._splitString(string), ["BD", "RJ", "00", "  ", "  "])

    def testParseLineType3(self):
        line = " "*230 + "BDRJ00AE  "
        result = PaymentParser._parseLineType3(line)
        self.assertEqual([id for id, value in result], ["BD", "RJ", "00", "AE"])

from unittest.case import TestCase
from febraban.cnab240.itau.slipV30.slip.slip import SlipV30


class SlipTest(TestCase):

    def testToString(self):
        slip = SlipV30()
        response = "0000001300000P 0100000 000000000000 0109000000000        00000               0000000000000000000000000000099A00000000000000000000000000000000000000000000000000000000000000000000000000000000000000                         0001590000000000000 \r\n0000001300000Q 010000000000000000                                                                                               00000000                 0000000000000000                                        000                            "
        self.assertEqual(response, slip.toString())

    def testAmount(self):
        slip = SlipV30()
        slip.setAmountInCents(100)
        amount = slip.amountInCents()
        self.assertEqual(amount, 100)
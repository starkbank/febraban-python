from unittest.case import TestCase
from febraban.cnab240.itau.charge import Slip


class SlipTest(TestCase):

    def testToString(self):
        slip = Slip()
        response = "0000001300000P 0100000 000000000000 0109000000000        00000               0000000000000000000000000000099A00000000000000000000000000000000000000000000000000000000000000000000000000000000000000                         0001590000000000000 \r\n0000001300000Q 010000000000000000                                                                                               00000000                 0000000000000000                                        000                            "
        self.assertEqual(response, slip.toString())

    def testAmount(self):
        slip = Slip()
        slip.setAmountInCents(100)
        amount = slip.amountInCents()
        self.assertEqual(amount, 100)
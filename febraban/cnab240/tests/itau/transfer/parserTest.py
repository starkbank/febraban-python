from unittest.case import TestCase
from febraban.cnab240.itau.transfer import PaymentParser


shippingFile = \
"""
34100000      081220018183000180                    07307 000000014446 4STARK BANK S A                                                        11712201823131100000000000000                                                                     
34100011C2041040 220018183000180                    07307 000000014446 4STARK BANK S A                                                        RUA DOS INGLESES 586                              SAO PAULO           01329000SP                  
3410001300001A00000026000001 000003819671 3ANTONIO DEROMIR NEVES DA SILVASBX-469300171243520018122018REA000000000000000000000000033605                    00000000000000000000000                    0000000000442841035210                     
34100015         000003000000000000033605000000000000000000                                                                                                                                                                                     
34199999         000008000026                                                                                                                                                                                                                   
""".strip()


returnFile = \
"""
34100000      081220018183000180          003751467 07307 000000014446 4STARK BANK S A                BANCO ITAU S/A                          21212201816310100002908106250                                                                     
34100011C2001081 220018183000180                    07307 000000014446 4STARK BANK S A                                                        RUA DOS INGLESES 586                              SAO PAULO           01329000SP                  
3410001300001A00000034107307 000000014444 9STARK BANK S A                SBX-472651104727859212122018BRL000000000000000000000001000000974616333000011     12122018000000001000000STARK BANK S A      00000020018183000180            000        
34100015         000003000000000001000000000000000000000000                                                                                                                                                                                     
34199999         000008000026000000                                                                                                                                                                                                             
""".strip()


class ParserTest(TestCase):

    def testParseShippingFile(self):
        payment = PaymentParser.parseText(shippingFile)[0]
        self.assertEqual(payment.identifier, "SBX-4693001712435200")
        self.assertEqual(payment.amountInCents, 33605)
        self.assertEqual(payment.occurrences, [])

    def testReturnShippingFile(self):
        payment = PaymentParser.parseText(returnFile)[0]
        self.assertEqual(payment.identifier, "SBX-4726511047278592")
        self.assertEqual(payment.amountInCents, 1000000)
        self.assertEqual(payment.occurrences, ["00"])
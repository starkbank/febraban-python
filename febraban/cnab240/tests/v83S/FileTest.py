
import unittest
from cnab240.user import User, UserBank
from cnab240.v83S.file.header import Header
from cnab240.v83S.file.trailer import Trailer


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


class FileTest(unittest.TestCase):

    def testHeaderLengh(self):
        string = Header().content
        self.assertEqual(len(string), 240)

    def testTrailorLengh(self):
        string = Trailer().content
        self.assertEqual(len(string), 240)

    def testHeaderDefaultValues(self):
        content = Header().content
        self.assertEqual(content[3:7], "0000")
        self.assertEqual(content[7:8], "0")
        self.assertEqual(content[14:17], "081")
        self.assertEqual(content[142:143], "1")

    def testTrailerDefaultValues(self):
        content = Trailer().content
        self.assertEqual(content[3:7], "9999")
        self.assertEqual(content[7:8], "9")

    def testHeaderSets(self):
        header = Header()
        header.setSender(user)
        header.setSenderBank(bank)
        response = "34100000      081100012345678901                    01234 000001234567 8JOHN SMITH                                                            10312201719400900000000000000                                                                     "
        self.assertEquals(header.content, response)

    def testTrailerSets(self):
        trailer = Trailer()
        trailer.setSenderBank(bank)
        trailer.setNumberOfLotsAndRegisters([1,2,3])
        response = "34199999         000003000011                                                                                                                                                                                                                   "
        self.assertEquals(trailer.content, response)


if __name__ == '__main__':
    unittest.main()
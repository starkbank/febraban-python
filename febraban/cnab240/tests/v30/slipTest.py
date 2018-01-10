from unittest.case import TestCase
from datetime import datetime
from febraban.cnab240.characterType import numeric, alphaNumeric
from febraban.cnab240.v30.slip.header import Header
from febraban.cnab240.v30.slip.segmentP import SegmentP
from febraban.cnab240.v30.slip.segmentQ import SegmentQ
from febraban.cnab240.v30.slip.trailer import Trailer
from febraban.cnab240.v30.slip.slip import SlipV30
from febraban.cnab240.v30.file.file import FileV30
from febraban.cnab240.user import User, UserAddress, UserBank


class SlipTest(TestCase):

    def testHeaderLengh(self):
        string = Header().toString()
        self.assertEqual(len(string), 240)

    def testSegmentPLengh(self):
        string = SegmentP().toString()
        self.assertEqual(len(string), 240)

    def testSegmentQLengh(self):
        string = SegmentQ().toString()
        self.assertEqual(len(string), 240)

    def testTrailerLengh(self):
        string = Trailer().toString()
        self.assertEqual(len(string), 240)

    def testHeaderDefaultValues(self):
        elements = Header().elements
        self.assertEqual(elements[2].value(), "1")
        self.assertEqual(elements[3].value(), "R")
        self.assertEqual(elements[4].value(), "01")
        self.assertEqual(elements[6].value(), "030")

    def testSegmentPDefaultValues(self):
        elements = SegmentP().elements
        self.assertEqual(elements[2].value(), "3")
        self.assertEqual(elements[4].value(), "P")

    def testSegmentQDefaultValues(self):
        elements = SegmentQ().elements
        self.assertEqual(elements[2].value(), "3")
        self.assertEqual(elements[4].value(), "Q")

    def testTrailerDefaultValues(self):
        elements = Trailer().elements
        self.assertEqual(elements[2].value(), "5")

    def testHeaderPositions(self):
        elements = Header().elements
        currentPositions = [(e.numberOfCharacters, e.charactersType) for e in elements]
        rightPositions = [
            (3,  numeric),
            (4,  numeric),
            (1,  numeric),
            (1,  alphaNumeric),
            (2,  numeric),
            (2,  numeric),
            (3,  numeric),
            (1,  alphaNumeric),
            (1,  numeric),
            (15, numeric),
            (20, alphaNumeric),
            (1,  numeric),
            (4,  numeric),
            (1,  alphaNumeric),
            (7,  numeric),
            (5,  numeric),
            (1,  alphaNumeric),
            (1,  numeric),
            (30, alphaNumeric),
            (80, alphaNumeric),
            (8,  numeric),
            (8,  numeric),
            (8,  numeric),
            (33, alphaNumeric)
        ]
        self.assertEquals(rightPositions, currentPositions)

    def testSegmentPPositions(self):
        elements = SegmentP().elements
        currentPositions = [(e.numberOfCharacters, e.charactersType) for e in elements]
        rightPositions = [
            (3,  numeric),
            (4,  numeric),
            (1,  numeric),
            (5,  numeric),
            (1,  alphaNumeric),
            (1,  alphaNumeric),
            (2,  numeric),
            (1,  numeric),
            (4,  numeric),
            (1,  alphaNumeric),
            (7,  numeric),
            (5,  numeric),
            (1,  alphaNumeric),
            (1,  numeric),
            (3,  numeric),
            (8,  numeric),
            (1,  numeric),
            (8,  alphaNumeric),
            (5,  numeric),
            (10, alphaNumeric),
            (5,  alphaNumeric),
            (8,  numeric),
            (15, numeric),
            (5,  numeric),
            (1,  numeric),
            (2,  numeric),
            (1,  alphaNumeric),
            (8,  numeric),
            (1,  numeric),
            (8,  numeric),
            (15, numeric),
            (1,  numeric),
            (8,  numeric),
            (15, numeric),
            (15, numeric),
            (15, numeric),
            (25, alphaNumeric),
            (1,  numeric),
            (2,  numeric),
            (1,  numeric),
            (2,  numeric),
            (13, numeric),
            (1,  alphaNumeric),
        ]
        self.assertEquals(rightPositions, currentPositions)

    def testSegmentQPositions(self):
        elements = SegmentQ().elements
        currentPositions = [(e.numberOfCharacters, e.charactersType) for e in elements]
        rightPositions = [
            (3,  numeric),
            (4,  numeric),
            (1,  numeric),
            (5,  numeric),
            (1,  alphaNumeric),
            (1,  alphaNumeric),
            (2,  numeric),
            (1,  numeric),
            (15, numeric),
            (30, alphaNumeric),
            (10, alphaNumeric),
            (40, alphaNumeric),
            (15, alphaNumeric),
            (8,  numeric),
            (15, alphaNumeric),
            (2,  alphaNumeric),
            (1,  numeric),
            (15, numeric),
            (30, alphaNumeric),
            (10, alphaNumeric),
            (3,  numeric),
            (28, alphaNumeric)
        ]
        self.assertEquals(rightPositions, currentPositions)

    def testTrailerPositions(self):
        elements = Trailer().elements
        currentPositions = [(e.numberOfCharacters, e.charactersType) for e in elements]
        rightPositions = [
            (3,  numeric),
            (4,  numeric),
            (1,  numeric),
            (9,  alphaNumeric),
            (6,  numeric),
            (6,  numeric),
            (17, numeric),
            (6,  numeric),
            (17, numeric),
            (46, numeric),
            (8,  numeric),
            (117,alphaNumeric)
        ]
        self.assertEquals(rightPositions, currentPositions)

    def testMultipleSlipPayments(self):
        firstUser = User(
            name="",
            identifier="",
            bank=UserBank("", "", "", "", ""),
            address=UserAddress("", "", "", "", "")
        )

        secondUser = User(
            name="",
            identifier="",
            bank=UserBank("", "", "", "", ""),
            address=UserAddress("", "", "", "", "")
        )

        date = datetime.now()

        firstSlip = SlipV30()
        firstSlip.setSender(firstUser)
        firstSlip.setAmountInCents("")
        firstSlip.setPayer(secondUser)
        firstSlip.setIssueDate(datetime=date)
        firstSlip.setExpirationDate(datetime=date)
        firstSlip.setBankIdentifier(
            identifier="",
            branch=firstUser.bank.branchCode,
            accountNumber=firstUser.bank.accountNumber,
            wallet=""
        )

        secondSlip = SlipV30()
        secondSlip.setSender(firstUser)
        secondSlip.setAmountInCents("")
        secondSlip.setPayer(secondUser)
        secondSlip.setIssueDate(datetime=date)
        secondSlip.setExpirationDate(datetime=date)
        secondSlip.setBankIdentifier(
            identifier="",
            branch=firstUser.bank.branchCode,
            accountNumber=firstUser.bank.accountNumber,
            wallet=""
        )

        file = FileV30()
        file.setUser(firstUser)
        file.add(lot=firstSlip)
        file.add(lot=secondSlip)

        lines = file.toString().split("\r\n")
        self.assertEquals(int(lines[4][23:29]), 1)
        self.assertEquals(int(lines[8][23:29]), 2)
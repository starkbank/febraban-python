
import unittest

from cnab240.v103.payment.header import Header
from cnab240.v103.payment.segmentA import SegmentA
from cnab240.v103.payment.trailer import Trailer
from cnab240.row import numeric, alphaNumeric


class PaymentTest(unittest.TestCase):

    def testHeaderLengh(self):
        string = Header().toString()
        self.assertEqual(len(string), 240)

    def testSegmentALengh(self):
        string = SegmentA().toString()
        self.assertEqual(len(string), 240)

    def testTrailerLengh(self):
        string = Trailer().toString()
        self.assertEqual(len(string), 240)

    def testHeaderDefaultValues(self):
        elements = Header().elements
        self.assertEqual(elements[2].value(), "1")
        self.assertEqual(elements[3].value(), "C")
        self.assertEqual(elements[6].value(), "046")

    def testSegmentADefaultValues(self):
        elements = SegmentA().elements
        self.assertEqual(elements[2].value(), "3")
        self.assertEqual(elements[4].value(), "A")

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
            (14, numeric),
            (20, alphaNumeric),
            (5,  numeric),
            (1,  alphaNumeric),
            (12, numeric),
            (1,  alphaNumeric),
            (1,  alphaNumeric),
            (30, alphaNumeric),
            (40, alphaNumeric),
            (30, alphaNumeric),
            (5,  numeric),
            (15, alphaNumeric),
            (20, alphaNumeric),
            (8,  numeric),
            (2,  alphaNumeric),
            (2,  numeric),
            (6,  alphaNumeric),
            (10, alphaNumeric),
        ]
        self.assertEquals(rightPositions, currentPositions)

    def testSegmentAPositions(self):
        elements = SegmentA().elements
        currentPositions = [(e.numberOfCharacters, e.charactersType) for e in elements]
        rightPositions = [
            (3,  numeric),
            (4,  numeric),
            (1,  numeric),
            (5,  numeric),
            (1,  alphaNumeric),
            (1,  numeric),
            (2,  numeric),
            (3,  numeric),
            (3,  numeric),
            (5,  numeric),
            (1,  alphaNumeric),
            (12, numeric),
            (1,  alphaNumeric),
            (1,  alphaNumeric),
            (30, alphaNumeric),
            (20, alphaNumeric),
            (8,  numeric),
            (3,  alphaNumeric),
            (15, numeric),
            (15, numeric),
            (20, alphaNumeric),
            (8,  numeric),
            (15, numeric),
            (40, alphaNumeric),
            (2,  alphaNumeric),
            (5,  alphaNumeric),
            (2,  alphaNumeric),
            (3,  alphaNumeric),
            (1,  numeric),
            (10, alphaNumeric),
        ]
        self.assertEquals(rightPositions, currentPositions)

    def testTrailerPositions(self):
        elements = Trailer().elements
        currentPositions = [(e.numberOfCharacters, e.charactersType) for e in elements]
        rightPositions = [
            (3,   numeric),
            (4,   numeric),
            (1,   numeric),
            (9,   alphaNumeric),
            (6,   numeric),
            (18,  numeric),
            (18,  numeric),
            (6,   numeric),
            (165, alphaNumeric),
            (10,  alphaNumeric)
        ]
        self.assertEquals(rightPositions, currentPositions)

if __name__ == '__main__':
    unittest.main()
import unittest

from cnab240.row import RowElement, numeric, alphaNumeric


class RowTest(unittest.TestCase):

    def testShortNumericValue(self):
        item = RowElement(
            description="Anything beacuse I just want to test",
            numberOfCharacters=4,
            charactersType=numeric,
            value="1"
        )
        self.assertEqual(item.toString(), "0001")

    def testLongNumericValue(self):
        item = RowElement(
            description="Anything beacuse I just want to test",
            numberOfCharacters=2,
            charactersType=numeric,
            value="12345"
        )
        self.assertEqual(item.toString(), "12")

    def testShortAlphaNumericValue(self):
        item = RowElement(
            description="Anything beacuse I just want to test",
            numberOfCharacters=6,
            charactersType=alphaNumeric,
            value="Ab12"
        )
        self.assertEqual(item.toString(), "Ab12  ")

    def testLongAlphaNumericValue(self):
        item = RowElement(
            description="Anything beacuse I just want to test",
            numberOfCharacters=6,
            charactersType=alphaNumeric,
            value="AbZ12abcd"
        )
        self.assertEqual(item.toString(), "AbZ12a")

    def testSetValueInvalidNumeric(self):
        item = RowElement(
            description="Anything beacuse I just want to test",
            numberOfCharacters=6,
            charactersType=numeric,
        )
        self.assertRaises(ValueError, item.setValue, "124a5")

    def testSetValueInvalidAlphaNumeric(self):
        item = RowElement(
            description="Anything beacuse I just want to test",
            numberOfCharacters=6,
            charactersType=numeric,
        )
        self.assertRaises(ValueError, item.setValue, "124a#5")


if __name__ == '__main__':
    unittest.main()
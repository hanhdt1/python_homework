import unittest
import easy
import medium

class CheckEasySolutions(unittest.TestCase):
    def test_easy_day_diff(self):
        self.assertEqual(easy.day_diff("19/12/2021","2021-17-05"), 216)
        self.assertEqual(easy.day_diff("10/05/2021","2021-01-03"), 70)

    def test_easy_alpha_num(self):
        self.assertEqual(easy.alpha_num("Emma25 is Data scientist50 and AI Expert"), ["Emma25", "scientist50"])
        self.assertEqual(easy.alpha_num("tHE1 fOX iS cOMING2 fOR tHE4 cHICKEN"), ['tHE1', 'cOMING2', 'tHE4'])

class CheckMediumSolutions(unittest.TestCase):
    def test_anagram_number(self):
        self.assertTrue(medium.anagram_number(121121))
        self.assertFalse(medium.anagram_number(12134))
        self.assertTrue(medium.anagram_number(8888888888888888))

    def test_roman_to_int(self):
        self.assertEqual(medium.roman_to_int("LVIII"), 58)
        self.assertEqual(medium.roman_to_int("IX"), 9)
        self.assertEqual(medium.roman_to_int("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
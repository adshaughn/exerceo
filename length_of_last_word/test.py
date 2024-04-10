import unittest

from length_of_last_word import lengthOfLastWord


class TestLengthOfLastWord(unittest.TestCase):
    def test_singleWord(self):
        self.assertEqual(lengthOfLastWord("hi"), 2)
        self.assertEqual(lengthOfLastWord("Boba"), 4)
        self.assertEqual(lengthOfLastWord("triskaidekaphobia"), 17)

    def test_multiWord(self):
        self.assertEqual(lengthOfLastWord("hello there"), 5)
        self.assertEqual(lengthOfLastWord("luffy is still joyboy"), 6)
        self.assertEqual(lengthOfLastWord("Matcha is very very delicious"), 9)

    def test_other(self):
        self.assertEqual(lengthOfLastWord("   fly me   to   the moon  "), 4)


if __name__ == "__main__":
    unittest.main()

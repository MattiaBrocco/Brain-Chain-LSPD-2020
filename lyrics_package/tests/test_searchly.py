import unittest
from lyrics_package import searchly
# TO RUN IT: python -m unittest lyrics_package/tests/test_searchly.py


class TestLyricsInput(unittest.TestCase):

    def test_wrong_type1(self):
        with self.assertRaises(AttributeError):
            searchly.similarity(3, "a")

    def test_wrong_type2(self):
        with self.assertRaises(AttributeError):
            searchly.similarity("b", [1, 2])

    def test_no_input(self):
        """
        Missing positional arguments of a
        function is a TypeError.
        """
        with self.assertRaises(TypeError):
            searchly.similarity()

    def test_string(self):
        with self.assertRaises(Exception):
            searchly.similarity("abc\nd", "ef\th")


if __name__ == "__main__":
    unittest.main()

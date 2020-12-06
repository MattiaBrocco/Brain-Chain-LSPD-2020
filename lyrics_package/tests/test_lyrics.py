import unittest
from lyrics_package import lyrics
# TO RUN IT: python -m unittest lyrics_package/tests/test_lyrics.py


class TestLyricsInput(unittest.TestCase):

    def test_wrong_type1(self):
        with self.assertRaises(AttributeError):
            lyrics.get_lyric(3, "a")

    def test_wrong_type2(self):
        with self.assertRaises(AttributeError):
            lyrics.get_lyric("b", [1, 2])

    def test_no_input(self):
        """
        Missing positional arguments of a
        function is a TypeError.
        """
        with self.assertRaises(TypeError):
            lyrics.get_lyric()

    def test_string(self):
        with self.assertRaises(Exception):
            lyrics.get_lyric("abc\nd", "ef\th")


if __name__ == "__main__":
    unittest.main()

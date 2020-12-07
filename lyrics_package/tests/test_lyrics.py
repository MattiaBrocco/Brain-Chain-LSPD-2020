import unittest
from lyrics_package import lyrics
# TO RUN IT: python -m unittest lyrics_package/tests/test_lyrics.py
# COVERAGE: coverage run -m py.test lyrics_package/tests/test_lyrics.py

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

    def test_string_special(self):
        with self.assertRaises(Exception):
            lyrics.get_lyric("abc\nd", "ef\th")
            
    def test_str_out(self):
        p1 = lyrics.get_lyric("oasis", "wonderwall")
        p2 = lyrics.get_lyric("guarda_come_flexo", "mambolosco")
        self.assertIsInstance(p1, str)
        self.assertIsInstance(p2, str)


if __name__ == "__main__":
    unittest.main()
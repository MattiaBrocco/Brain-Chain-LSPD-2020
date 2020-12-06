import unittest
from lyrics_package import songsterr
# TO RUN IT: python -m unittest lyrics_package/tests/test_songsterr.py


class TestLyricsInput(unittest.TestCase):

    def test_wrong_type1(self):
        with self.assertRaises(AttributeError):
            songsterr.artists_songs(3, "a")

    def test_wrong_type2(self):
        with self.assertRaises(AttributeError):
            songsterr.artists_songs("b", [1, 2])

    def test_no_input(self):
        """
        Missing positional arguments of a
        function is a TypeError.
        """
        with self.assertRaises(TypeError):
            songsterr.artists_songs()

    def test_string(self):
        with self.assertRaises(Exception):
            songsterr.artists_songs("abc\nd", "ef\th")


if __name__ == "__main__":
    unittest.main()

import unittest
from lyrics_package import songsterr
# TO RUN IT: python -m unittest lyrics_package/tests/test_songsterr.py
# COVERAGE: coverage run -m py.test lyrics_package/tests/test_songsterr.py


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
            
    def test_str_out(self):
        """
        :p1 to test existing song for songsterr
        :p2 to test non-existing song
        """
        p1 = songsterr.artists_songs("oasis", "wonderwall")
        p2 = songsterr.artists_songs("guarda_come_flexo", "mambolosco")        
        self.assertIsInstance(p1, tuple)
        self.assertIsInstance(p2, str)

if __name__ == "__main__":
    unittest.main()
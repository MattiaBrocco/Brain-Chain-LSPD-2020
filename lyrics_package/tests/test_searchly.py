import unittest
import pandas as pd
from lyrics_package import searchly
# TO RUN IT: python -m unittest lyrics_package/tests/test_searchly.py
# COVERAGE: coverage run -m py.test lyrics_package/tests/test_searchly.py


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

    def test_str_out(self):
        """
        :p1 to test existing song for searchly, with multiple
        correspondances
        :p2 to test non-existing song
        :p3 to test the exact correspondence
        ** Coverage skips line 35 of searchly.similarity
        (if statement activated in the case of API error)
        """
        p1 = searchly.similarity("lady_gaga", "paparazzi")
        p2 = searchly.similarity("guarda_come_flexo", "mambolosco")
        p3 = searchly.similarity("oasis", "wonderwall")
        self.assertIsInstance(p1, pd.DataFrame)
        self.assertIsInstance(p2, str)
        self.assertIsInstance(p3, pd.DataFrame)


if __name__ == "__main__":
    unittest.main()

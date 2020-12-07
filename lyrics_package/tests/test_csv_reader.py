import os
import unittest
import pandas as pd
from lyrics_package import history
from pandas.testing import assert_frame_equal
# TO RUN IT: python -m unittest lyrics_package/tests/test_csv_reader.py
# COVERAGE: coverage run -m py.test lyrics_package/tests/test_csv_reader.py

class TestCSVReader(unittest.TestCase):
    
    def setUp(self):
        """
        The function "create_hist" requires a valid
        path, to perform the test, the temporary
        file will be created in the folder tests.
        """
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.temp_file = self.path + "\\tmp.csv"

    # Test that the function works correctly
    # To check whether the DataFrames were the same,
    # pandas.testing has been used.
    def test_history(self):
        actual = history.create_hist("a", "b", self.temp_file)
        expected = pd.DataFrame([["a", "b"]],
                                columns=["----------------",
                                         "----------------"]).head(3)
        assert_frame_equal(actual, expected)
        
    # Test that at this point "create_hist"
    # returns a non-empty dataframe
    def test_non_empty(self):
        df = history.create_hist("a", "b", self.temp_file)
        self.assertFalse(df.empty)

    def tearDown(self):
        os.remove(self.path + "\\tmp.csv")


if __name__ == "__main__":
    unittest.main()
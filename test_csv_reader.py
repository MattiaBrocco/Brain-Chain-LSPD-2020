import os
import unittest
import pandas as pd
from lyrics_package import History
from pandas.testing import assert_frame_equal
# TO RUN IT: python -m unittest Test_csv_reader.py

class TestCSVReader(unittest.TestCase):    

    def setUp(self):
        self.temporary_file = 'tmp.csv'
        f = open(self.temporary_file, 'w')
        f.close()
        
    # Test that at this point "create_hist"
    # returns an empty dataframe
    def test_no_datafile(self):
        df = History.create_hist("a", "b", self.temporary_file)
        self.assertFalse(df.empty)

    # Test that the function works correctly
    # To check whether the DataFrames were the same,
    # pandas.testing has been used.
    def test_history(self):
        actual = History.create_hist("a","b", self.temporary_file)
        expected = pd.DataFrame([["a", "b"]],
                                columns = ["----------------",
                                           "----------------"]).head(3)
        assert_frame_equal(actual,expected)
        
    def tearDown(self):
        os.remove(self.temporary_file)
       
    
if __name__ == "__main__":
    unittest.main()
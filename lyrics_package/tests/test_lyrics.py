import unittest
from lyrics_package import lyrics


class TestLyricsInput(unittest.TestCase):
    
    def test_wrong_type1(self):
        with self.assertRaises(AttributeError):
            lyrics.get_lyric(3, "a")
            
    def test_wrong_type2(self):
        with self.assertRaises(AttributeError):
            lyrics.get_lyric("b", [1, 2])

## TEST AGAINST NO INPUT, WRONG RANGE, EDGE CASE, CORNER CASE
        
if __name__ == "__main__":
    unittest.main()
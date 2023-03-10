import unittest
import SplitNumber

class TestSplitNumber(unittest.TestCase):
    def test_SplitNumber(self):
        self.assertEqual(SplitNumber.split_pairs('abcdef'), ['ab', 'cd', 'ef'])
        self.assertEqual(SplitNumber.split_pairs('a'), ['a_'])
        self.assertEqual(SplitNumber.split_pairs('abc'),['ab','c_'])
        self.assertEqual(SplitNumber.split_pairs('ab'),['ab'])
        self.assertEqual(SplitNumber.split_pairs(''),[])


if __name__ == '__main__':
    unittest.main()
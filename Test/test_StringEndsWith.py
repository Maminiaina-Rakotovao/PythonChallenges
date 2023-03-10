import unittest
import StringEndsWith

class TestStringEndsWith(unittest.TestCase):
    def test_StringEndsWith(self):
        self.assertEqual(StringEndsWith.EndsWith('samurai', 'ai'), True)
        self.assertEqual(StringEndsWith.EndsWith('abc', 'd'), False)
        self.assertEqual(StringEndsWith.EndsWith('Sunday', 'unday'), True)
        self.assertEqual(StringEndsWith.EndsWith('', ''), True)
        self.assertEqual(StringEndsWith.EndsWith('Python', ''), True)
        


if __name__ == '__main__':
    unittest.main()
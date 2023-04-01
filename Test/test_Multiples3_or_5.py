import unittest
import Multiples3_or_5

class TestMultitles(unittest.TestCase):
    def testone(self):
        self.assertEqual(Multiples3_or_5.solution(-2), 0)
        self.assertEqual(Multiples3_or_5.solution(10), 23)
        self.assertEqual(Multiples3_or_5.solution(100), 2318)
        self.assertEqual(Multiples3_or_5.solution(200), 9168)
        self.assertEqual(Multiples3_or_5.solution(20), 78)



if __name__ == '__main__':
    unittest.main()
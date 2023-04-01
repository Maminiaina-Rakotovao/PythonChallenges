import unittest
import tranpose

class TestTransp(unittest.TestCase):
    def testtranspose(self):
        self.assertEqual(tranpose.transposeMatrix([[1, 2, 3]]),[[1], [2], [3]])
        self.assertEqual(tranpose.transposeMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),[[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(tranpose.transposeMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]]),
                                                    [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]])


if __name__ == '__main__':
    unittest.main()
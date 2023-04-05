import unittest
import aims_robot

class TestPathFinding(unittest.TestCase):
           
	# test case 1
    def test_1(self):
        matrix = aims_robot.InputtoMatrix('A...xB', [])
        self.assertEqual(aims_robot.count_path(matrix), 0)
    
    # test case 2
    def test_2(self):
        matrix = aims_robot.InputtoMatrix('A......B', [])
        self.assertEqual(aims_robot.count_path(matrix), 1)
        
	# test case 3
    def test_3(self):
        matrix = aims_robot.InputtoMatrix('A..\n...\n..B', [])
        self.assertEqual(aims_robot.count_path(matrix), 2)

    # test case 4
    def test_4(self):
        matrix = aims_robot.InputtoMatrix('A...\n....\n....\nxxxB', [])
        self.assertEqual(aims_robot.count_path(matrix), 4)

    # test case 5
    def test_5(self):
        matrix = aims_robot.InputtoMatrix('A....\n.....\n.....\n.....\nxxxxB', [])
        self.assertEqual(aims_robot.count_path(matrix), 20)

    # test case 6
    def test_6(self):
        matrix = aims_robot.InputtoMatrix('A....\n.....\n.....\n.....\n....B', [])
        self.assertEqual(aims_robot.count_path(matrix), 104)

    # test case 7
    def test_7(self):
        matrix = aims_robot.InputtoMatrix('A.....x\n......x\n......x\n......x\n......B', [])
        self.assertEqual(aims_robot.count_path(matrix), 378)


if __name__ == '__main__':
    unittest.main()

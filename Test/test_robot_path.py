import unittest
import robot_path

class TestPathFinding(unittest.TestCase):
           
	# test case 1
    def test_1(self):
        matrix = robot_path.InputToMatrix('A.x.xx..xB')
        self.assertEqual(robot_path.count_paths(matrix), 0)
    
    # test case 2
    def test_2(self):
        matrix = robot_path.InputToMatrix('A......B')
        self.assertEqual(robot_path.count_paths(matrix), 1)
        
	# test case 3
    def test_3(self):
        matrix = robot_path.InputToMatrix('A..\n...\n..B')
        self.assertEqual(robot_path.count_paths(matrix), 2)

    # test case 4
    def test_4(self):
        matrix = robot_path.InputToMatrix('A...\n....\n....\nxxxB')
        self.assertEqual(robot_path.count_paths(matrix), 4)

    # test case 5
    def test_5(self):
        matrix = robot_path.InputToMatrix('A....\n.....\n.....\n.....\nxxxxB')
        self.assertEqual(robot_path.count_paths(matrix), 20)

    # test case 6
    def test_6(self):
        matrix = robot_path.InputToMatrix('A....\n.....\n.....\n.....\n....B')
        self.assertEqual(robot_path.count_paths(matrix), 104)

    # test case 7
    def test_7(self):
        matrix = robot_path.InputToMatrix('A.....x\n......x\n......x\n......x\n......B')
        self.assertEqual(robot_path.count_paths(matrix), 378)
        
	# test case 8
    def test_8(self):
        matrix = robot_path.InputToMatrix('A....\n.....\n.....\n.....\n.....\n.....\n....B')
        self.assertEqual(robot_path.count_paths(matrix), 1670)

    # test case 9
    def test_9(self):
        matrix = robot_path.InputToMatrix('A....\n.....\n.....\n.....\n.....\n.....\n.....\n....B')
        self.assertEqual(robot_path.count_paths(matrix), 6706)

if __name__ == '__main__':
    unittest.main()

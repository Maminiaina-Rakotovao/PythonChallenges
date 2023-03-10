import unittest
import VowelRemover

class TestVowelRemover(unittest.TestCase):
    def test_VowelRemover(self):
        self.assertEqual(VowelRemover.shortcut('gouyuodbye'),'gydby')
        self.assertEqual(VowelRemover.shortcut('Beautiful'),'Btfl')
        self.assertEqual(VowelRemover.shortcut('aaucxuifguo fdsop sfwqooosfsyfdso opofsopa'),'cxfg fdsp sfwqsfsyfds pfsp')
        self.assertEqual(VowelRemover.shortcut('eeefsdf ioosdf masfiodfsoiiyuo'),'fsdf sdf msfdfsy')
        self.assertEqual(VowelRemover.shortcut('aiooie oiouue ioioee'),'  ')


if __name__ == '__main__':
    unittest.main()
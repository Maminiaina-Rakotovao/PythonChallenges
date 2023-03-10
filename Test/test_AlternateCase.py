import unittest
import AlternateCase

class TestAlternateCase(unittest.TestCase):

    def test_AltCase(self):
        self.assertEqual(AlternateCase.Alternate_case('MAMY'),'mamy')
        self.assertEqual(AlternateCase.Alternate_case('HElLo yOu'),'heLlO YoU')
        self.assertEqual(AlternateCase.Alternate_case('Good to sEE You'),'gOOD TO See yOU')
        self.assertEqual(AlternateCase.Alternate_case('whAt IS YouR NAMe'),'WHaT is yOUr namE')
        self.assertEqual(AlternateCase.Alternate_case('fsstr JfdIFD MVMFffdk ODF FJDFKsfisfxx'),'FSSTR jFDifd mvmfFFDK odf fjdfkSFISFXX')
        

if __name__ == '__main__':
    unittest.main()
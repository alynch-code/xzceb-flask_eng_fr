"""test module"""
import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class test_english_to_french(unittest.TestCase):
    """class to test if function english to french works"""
    def test1(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
    def test2(self):
        self.assertNotEqual(englishToFrench(0),0)

class TestFrenchToEnglish(unittest.TestCase):
    """class to test if function french to english works"""
    def test3(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
    def test4(self):
        self.assertNotEqual(frenchToEnglish(0),0)
unittest.main()

import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrenchifnull(unittest.TestCase): 
    def nullinputtest(self): 
        self.assertNotEqual(englishToFrench('Hello'), '')
        

class TestfrenchToEnglishifnull(unittest.TestCase): 
    def nullinputtest(self): 
        self.assertNotEqual(frenchToEnglish('Bonjour'), '')



class TestenglishToFrenchtranslation(unittest.TestCase): 
    def nullinputtest(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        

class TestfrenchToEnglishtranslation(unittest.TestCase): 
    def nullinputtest(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        
unittest.main()
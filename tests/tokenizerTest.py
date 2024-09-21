import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import tokenizer 

class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase()
        self.tokenizer = tokenizer.Tokenizer()
        self.words = self.tokenizer.getWords(path="../data/harryPotterTest.txt")
        self.pairs = self.tokenizer.getPairs(path="../data/harryPotterTest.txt")
        self.tokens = self.tokenizer.createDict(path="../data/harryPotterTest.txt")

    def test_0_get_words_preprocessed(self):
        """
        - Test for invalid characters in tokenizer.
        """
        numbers = {'1','2','3','4','5','6','7','8','9'}

        for word in self.words:
            for item in numbers:
                self.assertTrue(item not in word)

        # Note, there are no approstrophies as these are conatined in words such as "I'm"
        punctuation = {"!", "\"", "#", "$", "%", "&", "(", ")", 
                       "*", "+", ",", "-", ".", "/", ":", ";", "<", 
                       "=", ">", "?", "@", "[", "\\", "]", "^", "_", 
                       "`", "{", "|", "}", "~"}
        
        for word in self.words:
            for item in punctuation:
                self.assertTrue(item not in word)

    def test_1_create_tokens_word_frequencies_0(self):
        """
        - Test for correct word frequencies for known counts > 0
        """
        self.assertEqual(self.tokens['the'], 4783)
        self.assertEqual(self.tokens['did'], 198)
        self.assertEqual(self.tokens['dumbledore'], 401)
        self.assertEqual(self.tokens["they're"], 45)
        self.assertEqual(self.tokens["i'm"], 92)
    
    def test_2_create_tokens_word_frequencies_1(self):
        """
        - Test for correct word frequencies for unknown words
        """
        self.assertEqual(self.tokens['mmmm'], 0)
        self.assertEqual(self.tokens['xylophone'], 0)
        self.assertEqual(self.tokens['soho'], 0)
        self.assertEqual(self.tokens["I'm"], 0)
        self.assertEqual(self.tokens[""], 0)
        self.assertEqual(self.tokens["'"], 0)
        self.assertEqual(self.tokens["''"], 0)
        self.assertEqual(self.tokens["'''"], 0)
        self.assertEqual(self.tokens['"'], 0)
        self.assertEqual(self.tokens['""'], 0)
        self.assertEqual(self.tokens['"""'], 0)

    def test_3_get_pairs_creates_pairs(self):
        """
        - Test for getPairs returns correct pairs
        """
        for pair in self.pairs:
            self.assertEqual(len(pair), 2)
            self.assertTrue(len(pair[0]) > 0)
            self.assertTrue(len(pair[1]) > 0)
        
        self.assertTrue(["i've", 'got'])
        self.assertTrue(['got', 'a'])
        self.assertTrue(['of', 'the'])
    
        
if __name__ == "__main__":
    unittest.main()
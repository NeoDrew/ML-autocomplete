import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import Tokenizer 

class Test(unittest.TestCase):
    tokenizer = Tokenizer.tokenizer()
    tokens = {}
    def test_0_get_words_preprocessed(self):
        """
        Test for invalid characters in tokenizer.
        """
        words = self.tokenizer.getWords(path="../data/harryPotterTest.txt")

        numbers = {1,2,3,4,5,6,7,8,9}
        self.assertTrue(numbers not in words)

        punctuation = {"!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"}
        self.assertTrue(punctuation not in words)

    def test_1_create_tokens(self):
        '''
        Test for correct word frequencies
        '''
        self.tokens = self.tokenizer.createDict(path="../data/harryPotterTest.txt")
        # Using default Harry Potter corpus
        self.assertEqual(self.tokens['the'], 4783)

        print(self.tokens['did'])
        print(self.tokens['dumbledore'])
        print(self.tokens['did'])
        print(self.tokens['did'])



if __name__ == "__main__":
    unittest.main()
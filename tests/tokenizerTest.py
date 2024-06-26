import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import tokenizer as tonkenizerClass

class Test(unittest.TestCase):
    tokenizer = tonkenizerClass.tokenizer()
    tokens = {}
    def test_0_get_words_preprocessed(self):
        words = self.tokenizer.getWords()

        numbers = {1,2,3,4,5,6,7,8,9}
        self.assertTrue(numbers not in words)

        punctuation = {"!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"}

        self.assertTrue(punctuation not in words)

    def test_1_create_tokens(self):
        self.tokens = self.tokenizer.createDict()
        # Assuming Harry Potter corpus
        self.assertEqual(self.tokens['the'], 17282)

if __name__ == "__main__":
    unittest.main()
import tokenizer
import numpy as np
import argparse
import os
from sklearn.neural_network import MLPRegressor

NUMBER_PREDICTED = 3


class SentenceComplete:
    def __init__(self, path: str):
        """
        Initialisation for SentenceComplete. Describes necessary class dependencies.

        :param string path: Path to text corpus.
        """
        self.tokenizer = tokenizer.Tokenizer()
        self.setnences = self.tokenizer.getSentences(path=path)
        self.pairs = self.tokenizer.getPairs(path=path)
        self.wordIds = {word: idx for idx, word in enumerate(self.tokenizer.getWords(path=path))}
        self.path = path
    
    def trainNN(self, showGraph=False):
        firstWord = np.array([self.wordIds[pair[0]] for pair in self.pairs]).reshape(-1, 1)
        secondWord = np.array([self.wordIds[pair[1]] for pair in self.pairs])

        
        
    def getPredictions(self, sentencePrefix: str):
        """
        Generates predictions given sentence prefix.

        :param string prefix: Prefix of sentence to be completed.
        :return: Top predictions in accordance to NUMBER_PREDICTED
        :rtype: List[String]
        """
        self.trainNN()
        lastWord = self.tokenizer.getSentences(path=self.path, sentence=sentencePrefix)[-1]
        return self.sentenceCompletionMLP.predict(lastWord)
    

# Able to run on command line.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run different test cases based on the type provided. Provide test corpus.")
    
    # Add --corpus argument
    parser.add_argument('--corpus', type=str, required=False,
                        help="Specify the directory of test corpus to run.")

    args = parser.parse_args()
    if args.corpus is None:
        exit("Invalid directory")
    if not(os.path.isfile(args.corpus)):
        exit("Invalid directory")

    
    sentenceComplete = SentenceComplete(path=args.corpus)
    print(sentenceComplete.wordIds)

    print("Press ctrl + c to exit.")
    while True:
        word = input("Enter sentence: ")
        print(sentenceComplete.getPredictions(word))

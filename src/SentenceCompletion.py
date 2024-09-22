import tokenizer
import argparse
import os

NUMBER_PREDICTED = 3


class SentenceComplete:
    def __init__(self, path: str):
        """
        Initialisation for SentenceComplete. Describes necessary class dependencies.

        :param string path: Path to text corpus.
        """
        self.tokenizer = tokenizer.Tokenizer()
        self.wordFreqDict = self.tokenizer.getNextWordFrequencies(path=path)
        self.path = path
    
    
    def getPredictions(self, sentencePrefix: str):
        """
        Generates predictions given sentence prefix.

        :param string prefix: Prefix of sentence to be completed.
        :return: Top word predictions in accordance to NUMBER_PREDICTED
        :rtype: List[String]
        """
        sentencePrefix = self.tokenizer.getSentences(sentence=sentencePrefix)
        matches = self.wordFreqDict.get(sentencePrefix[-1][-1])
        
        if matches is None:
            return []
        matchList = matches.items()

        sortedMatches = (sorted(matchList, key=lambda x: int(x[1])))[::-1]

        topMatches = []

        for i in range(NUMBER_PREDICTED):
            try:
                topMatches.append(sortedMatches[i][0])
            except:
                return topMatches
        return topMatches
    

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

    print("Press ctrl + c to exit.")
    while True:
        word = input("Enter sentence: ")
        print(sentenceComplete.getPredictions(word))

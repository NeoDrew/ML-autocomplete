import tokenizer
import re
import argparse
import os

NUMBER_PREDICTED = 3


class AutoComplete:
    def __init__(self, path: str):
        """
        Initialisation for AutoComplete. Describes necessary class dependencies.

        :param string path: Path to text corpus.
        """
        self.tokenizer = tokenizer.Tokenizer()
        self.wordDictionary = self.tokenizer.createDict(path=path)

    def getPredictions(self, prefix: str):
        """
        Generates autocompletion predictions given prefix.

        :param string prefix: Prefix of word to be AutoCompleted.
        :return: Top predictions in accordance to NUMBER_PREDICTED
        :rtype: List[String]
        """
        prefix = re.sub(r"[^a-z\s]", "", (prefix.lower()).strip())
        words = self.wordDictionary.copy()
        matches = {}

        for word in words:
            if len(word) <= len(prefix):
                continue
            if word[0 : len(prefix)] == prefix:
                matches.update({word: words.get(word)})

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
    parser.add_argument('--corpus', type=str, required=True,
                        help="Specify the directory of test corpus to run.")

    args = parser.parse_args()
    if not(os.path.isfile(args.corpus)):
        exit("Invalid directory")

    autoComplete = AutoComplete(path=args.corpus)

    print("Press ctrl + c to exit.")
    while True:
        word = input("Enter prefix: ")
        print(autoComplete.getPredictions(word))

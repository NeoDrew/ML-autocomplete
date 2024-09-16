import re
from collections import Counter


# Preprocessing Corpus
class Tokenizer:
    def createDict(self, path="../data/harryPotter.txt"):
        """
        Converts a text corpus into a word frequency dictionary.

        :param string path: Path to text corpus.
        :return: Dictionary of lowercase words and their frequencies'
        :rtype: Dict{String:Int}
        """
        tokenVector = self.getWords(path=path)
        dictionary = Counter(tokenVector)
        return dictionary

    def getWords(self, path):
        """
        Converts a text corpus into tokenized vector or words.

        :param string path: Path to text corpus.
        :return: Vector of lowercase words 
        :rtype: List[String]
        """
        with open(path, "r") as f:
            tokenVector = []
            for line in f:
                # Remove unnesscesary punctuation & case fold
                noPunctLine = re.sub(r"[^a-z\s']", "", line.lower())
                words = noPunctLine.strip().split()
                # If word is nothing coninue
                if words:
                    tokenVector.extend(words)
        
        return tokenVector
    
    def getSentences(self, path):
        """
        Converts a text corpus into tokenized vector or sentences.

        :param string path: Path to text corpus.
        :return: Vector of lowercase words 
        :rtype: List[String]
        """
        with open(path, "r") as f:
            sentences = f.read().split(".")
            sentenceVector = []
            for sentence in sentences:
                # Remove unnesscesary punctuation & case fold
                noPunctLine = re.sub(r"[^a-z\s']", "", sentence.lower())
                words = noPunctLine.strip().split()
                # If word is nothing coninue
                if words:
                    sentenceVector.append(words)
                
        return sentenceVector


if __name__ == "__main__":
    tokenizer = Tokenizer()
    print(tokenizer.getWords("../data/harryPotterTest.txt"))
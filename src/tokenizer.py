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
                noPunctLine = re.sub(r"[^\w\s']", "", line.lower())
                words = noPunctLine.strip().split()
                # If word is nothing coninue
                if not words:
                    continue
                # Removal of special characters
                if words[0][0] == "\x0c":
                    words[0] = words[0][1:]
                # If word is number, ignore
                withoutNumbers = []
                for word in words:
                    try:
                        if int(word):
                            continue
                    except:
                        withoutNumbers.append(word)

                tokenVector.extend(withoutNumbers)
        
        return tokenVector


if __name__ == "__main__":
    dictionary = Tokenizer()
    print((dictionary.createDict()))

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
                cleanWords = []
                
                # Removing pesky apostrophies
                for word in words:
                    if len(word) == 0:
                        continue
                    word = word.strip("'")
                    if len(word) > 0:
                        cleanWords.append(word)
                # If word is nothing coninue
                if cleanWords:
                    tokenVector.extend(cleanWords)
        
        return tokenVector
    
    def getSentences(self, path, sentence=None):
        """
        Converts a text corpus or input into tokenized vector or sentences.

        :param string path: Path to text corpus.
        :param string sentence: Sentence to be converted.
        :return: Vector of lowercase words
        :rtype: List[List[String]]
        """
        if sentence is None:
            with open(path, "r") as f:
                sentences = f.read().split(".")
                sentenceVector = []
                for sentence in sentences:
                    # Remove unnesscesary punctuation & case fold
                    noPunctLine = re.sub(r"[^a-z\s']", "", sentence.lower())
                    words = noPunctLine.strip().split()
                    cleanWords = []
                
                    # Removing pesky apostrophies
                    for word in words:
                        if len(word) == 0:
                            continue
                        word = word.strip("'")
                        if len(word) > 0:
                            cleanWords.append(word)
                    # If word is nothing coninue
                    if cleanWords:
                        sentenceVector.append(cleanWords)
        else:
            sentences = sentence.split(".")
            sentenceVector = []
            for sentence in sentences:
                # Remove unnesscesary punctuation & case fold
                noPunctLine = re.sub(r"[^a-z\s']", "", sentence.lower())
                words = noPunctLine.strip().split()
                # If word is nothing coninue
                if words:
                    sentenceVector.append(words)
        return sentenceVector
    
    def getPairs(self, path):
        """
        Converts a vector of sentences into pairs of consequtive words. 

        :return: Vector of pairs of lowercase words 
        :rtype: List[List[String]]
        """
        pairs = []
        for sentence in self.getSentences(path=path):
            for i in range(len(sentence)-1):
                pairs.append([sentence[i], sentence[i+1]])
        
        return pairs
    
    def getNextWordFrequencies(self, path):
        """
        Converts pairs of words from a setnece into a dictionary of words with the next words frequency.

        :return: Vector of pairs of lowercase words 
        :rtype: List[List[String]]
        """
        pairs = []
        for sentence in self.getSentences(path=path):
            for i in range(len(sentence)-1):
                pairs.append([sentence[i], sentence[i+1]])
        
        return pairs
    
if __name__ == "__main__":
    tokenizer = Tokenizer()
    print(tokenizer.getWords("../data/harryPotterTest.txt"))
import re
from collections import Counter


# Preprocessing Corpus
class tokenizer:
    def createDict(self, path="harryPotter.txt"):
        tokenPath = path
        tokenVector = self.getWords(path=tokenPath)
        dictionary = Counter(tokenVector)
        return dictionary

    def getWords(self, path="harryPotter.txt"):
        with open("../data/" + path, "r") as f:
            tokenVector = []
            for line in f:
                # Remove Punctuation & case fold
                noPunctLine = re.sub(r"[^\w\s]", "", line.lower())
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
    dictionary = tokenizer()
    print((dictionary.createDict()))

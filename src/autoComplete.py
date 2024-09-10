import tokenizer
import re
NUMBER_PREDICTED = 3
class autoComplete:
    def __init__(self, path):
        self.wordDictionary = {}
        Tokenizer = tokenizer.tokenizer()
        self.wordDictionary = Tokenizer.createDict(path=path)

    def getPredictions(self, prefix:str):
        prefix= re.sub(r"[^\w\s]", "", (prefix.lower()).strip())
        words = self.wordDictionary.copy()
        matches = {}
        
        for word in words:
            if len(word) <= len(prefix):
                continue
            if (word[0:len(prefix)] == prefix):
                matches.update({word : words.get(word)})
        
        matchList = matches.items()

        sortedMatches= (sorted(matchList,key=lambda x:int(x[1])))[::-1]

        topValues = []
        
        for i in range(NUMBER_PREDICTED):
            try:
                topValues.append(sortedMatches[i][0])
            except:
                return topValues
        return topValues

if __name__ == "__main__":
    autoC = autoComplete(path="../data/harryPotter.txt")
    print("Press ctrl + c to exit.")
    while True:
        word = input("Enter prefix: ")
        print(autoC.getPredictions(word))
import tokenizer
class app:
    def __init__(self):
        self.wordDictionary = {}
        Tokenizer = tokenizer.tokenizer()
        self.wordDictionary = Tokenizer.createDict()

    def getPredictions(self, prefix:str):
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
        
        for i in range(3):
            try:
                topValues.append(sortedMatches[i][0])
            except:
                return topValues
        return topValues


if __name__ == "__main__":
    App = app()

    a = input("enter prefix")
    print(App.getPredictions(a))


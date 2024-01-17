import re
from collections import Counter

#Preprocessing
class tokenizer:
    def createDict(self, tail="harryPotter.txt"):
        with open("../data/"+tail, "r") as f:
            c = []
            for line in f:
                noPunctLine:str= line.lower()
                noPunctLine = re.sub(r'[^\w\s]','',noPunctLine)
                words = noPunctLine.strip().split()
                if not words:
                    continue
                if words[0][0] == '\x0c':
                    words[0] = words[0][1:]
                c.extend(words)
            
        dictionary = Counter(c)
        return dictionary


if __name__ == "__main__":
    tok = tokenizer()
    print(tok.createDict())
import appC
import tokenizer
import time
import sys

class tests:
    def halfWordTest(self):
        print("Testing for correct predictions given n//2 characters...")
        appInst = appC.autoComplete()
        tokenInst = tokenizer.tokenizer()

        testWords = tokenInst.getWords(path="harryPotterTest.txt")
        testLen = len(testWords)
        updateNum = int(testLen / 200)
        correct = 0
        incorrect = 0

        i = 0
        start = time.time()
        for word in testWords:
            #If the word is of length 1, any extension is futile
            if len(word) == 1:
                continue

            if ((i % updateNum) == 0):
                print(f"-----------------{str((i/testLen) * 100)[0:5]}% complete-----------------")
                print(f"Correct: {correct}\n Incorrect: {incorrect}")
                if(incorrect > 0): print(f"Ratio {str(correct/(incorrect + correct))[0:5]}")
                else: print(f"Ratio 0.000")
            i += 1

            prediction = appInst.getPredictions(word[0:len(word)//2])

            if len(prediction)==0:
                incorrect += 1
                continue
            if(prediction[0] == word):
                correct += 1
            else:
                incorrect += 1
            
        end = time.time()
        print("-----------------100% complete-----------------")
        print(f"Correct: {correct}\n Incorrect: {incorrect}")
        print(f"Ratio {str(correct/incorrect)}")
        print(f"In {end - start} seconds.")
    
    def wordMinusOneTest(self):
        print("Testing for correct predictions given n-1 characters...")
        appInst = appC.autoComplete()
        tokenInst = tokenizer.tokenizer()

        testWords = tokenInst.getWords(path="harryPotterTest.txt")
        testLen = len(testWords)
        updateNum = int(testLen / 200)
        correct = 0
        incorrect = 0

        i = 0
        start = time.time()
        for word in testWords:
            #If the word is of length 1, any extension is futile
            if len(word) == 1:
                continue
            
            if ((i % updateNum) == 0):
                
                print(f"-----------------{str((i/testLen) * 100)[0:5]}% complete-----------------")
                print(f"Correct: {correct}\n Incorrect: {incorrect}")
                if(incorrect > 0): print(f"Ratio {str(correct/(incorrect + correct))[0:5]}")
                else: print(f"Ratio 0.000")
            i += 1

            prediction = appInst.getPredictions(word[:-1])
            
            if len(prediction)==0:
                incorrect += 1
                continue
            if(prediction[0] == word):
                correct += 1
            else:
                incorrect += 1
            
        end = time.time()
        print("-----------------100% complete-----------------")
        print(f"Correct: {correct}\n Incorrect: {incorrect}")
        print(f"Ratio {str(correct/incorrect + correct)}")
        print(f"In {end - start} seconds.")

if __name__ == "__main__":
    test = tests()

    if len(sys.argv) > 1:

        if (sys.argv[1] == 'half'):
            test.halfWordTest()

        elif (sys.argv[1] == 'minusOne'):
            test.wordMinusOneTest()
        else:
            print("Usage 'python3 tests.py --type' \n--------------------------------\n --type: half, minusOne")
    else:
        print("Usage 'python3 tests.py --type' \n--------------------------------\n --type: half, minusOne")
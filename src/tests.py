import app
import tokenizer
import time

class tests:
    def halfWordTest(self):
        appInst = app.app()
        tokenInst = tokenizer.tokenizer()

        testWords = tokenInst.getWords(path="harryPotterTest.txt")
        testLen = len(testWords)
        updateNum = int(testLen / 200)

        correct = 0
        incorrect = 0

        i = 0
        start = time.time()
        for word in testWords:
            if len(word) == 1:
                continue
            prediction = appInst.getPredictions(word[0:len(word)//2])
            # print("-----------------" + str(correct + incorrect) + "-----------------")
            

            if len(prediction)==0:
                # print(word + " : " + word[0:len(word)//2] + " : " + "N/A")
                # print("Incorrect")
                incorrect += 1
                continue
            if(prediction[0] == word):
                # print(word + " : " + word[0:len(word)//2] + " : " + prediction[0])
                # print("Correct")
                correct += 1
            else:
                # print(word + " : " + word[0:len(word)//2] + " : " + prediction[0])
                # print("Incorrect")
                incorrect += 1

            # print("✓ : ✖")
            # print(str(correct) + " : " + str(incorrect))
            if ((i % updateNum) == 0):
                print(f"-----------------{str((i/testLen) * 100)[0:5]}% complete-----------------")
                print(f"Correct: {correct}\n Incorrect: {incorrect}")
                print(f"Ratio {str(correct/incorrect)}")
            i += 1
            
        end = time.time()
        print("100% complete")
        print(f"Correct: {correct}\n Incorrect: {incorrect}")
        print(f"Ratio {str(correct/incorrect)}")
        print(f"In {end - start} seconds.")

if __name__ == "__main__":
    test = tests()
    test.halfWordTest()
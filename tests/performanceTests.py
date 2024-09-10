import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import autoComplete
import tokenizer
import time
import argparse


class performanceTests:
    def __init__(self, path):
        self.appInst = autoComplete.autoComplete(path)
        self.tokenInst = tokenizer.tokenizer()

        self.testWords = self.tokenInst.getWords(path)
        self.testLen = len(self.testWords)
        self.updateNum = int(self.testLen / 200)
        

    def halfWordTest(self, path):
        print("Testing for correct predictions given n//2 characters...")
        correct = 0
        incorrect = 0
        i = 0
        start = time.time()
        for word in self.testWords:
            # If the word is of length 1, any extension is futile
            if len(word) == 1:
                continue

            if (i % self.updateNum) == 0:
                print(
                    f"-----------------{str((i/self.testLen) * 100)[0:5]}% complete-----------------"
                )
                print(f"Correct: {correct}\n Incorrect: {incorrect}")
                if incorrect > 0:
                    print(f"Ratio {str(correct/(incorrect + correct))[0:5]}")
                else:
                    print(f"Ratio 0.000")
            i += 1

            prediction = self.appInst.getPredictions(word[0 : len(word) // 2])

            if len(prediction) == 0:
                incorrect += 1
                continue
            if prediction[0] == word:
                correct += 1
            else:
                incorrect += 1

        end = time.time()
        print("-----------------100% complete-----------------")
        print(f"Correct: {correct}\n Incorrect: {incorrect}")
        print(f"Ratio {str(correct/incorrect)}")
        print(f"In {end - start} seconds.")

    def wordMinusOneTest(self, path):
        print("Testing for correct predictions given n-1 characters...")
        correct = 0
        incorrect = 0
        i = 0
        start = time.time()
        for word in self.testWords:
            # If the word is of length 1, any extension is futile
            if len(word) == 1:
                continue

            if (i % self.updateNum) == 0:
                print(f"-----------------{str((i/self.testLen) * 100)[0:5]}% complete-----------------")
                print(f"Correct: {correct}\n Incorrect: {incorrect}")
                if incorrect > 0:
                    print(f"Ratio {str(correct/(incorrect + correct))[0:5]}")
                else:
                    print(f"Ratio 0.000")
            i += 1

            prediction = self.appInst.getPredictions(word[:-1])

            if len(prediction) == 0:
                incorrect += 1
                continue
            if prediction[0] == word:
                correct += 1
            else:
                incorrect += 1

        end = time.time()
        print("-----------------100% complete-----------------")
        print(f"Correct: {correct}\n Incorrect: {incorrect}")
        print(f"Ratio {str(correct/incorrect + correct)}")
        print(f"In {end - start} seconds.")


if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Run different test cases based on the type provided. Provide test corpus.")
    
    # Add the --type argument with possible values
    parser.add_argument('--type', type=str, required=True, choices=['half', 'minusOne'],
                        help="Specify the type of test to run: 'half' or 'minusOne'")
    
    # Add the --corpus argument
    parser.add_argument('--corpus', type=str, required=True,
                        help="Specify the directory of test corpus to run.")
    
    # Parse the arguments
    args = parser.parse_args()

    

    if not(os.path.isfile(args.corpus)):
        print("Invalid directory")
        exit()

    test = performanceTests(args.corpus)

    if args.type == "half":
        test.halfWordTest(args.corpus)
    elif args.type == "minusOne":
        test.wordMinusOneTest(args.corpus)


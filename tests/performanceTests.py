import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import AutoComplete
import Tokenizer
import time
import argparse


class PerformanceTests:
    def __init__(self, path):
        self.autoComplete = AutoComplete.AutoComplete(path)
        self.tokenizer = Tokenizer.Tokenizer()
        
        self.testWords = self.tokenizer.getWords(path)
        self.testLen = len(self.testWords)
        self.updateNum = int(self.testLen / 200)
        
    def halfWordPerformanceTest(self):
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

            prediction = self.autoComplete.getPredictions(word[0 : len(word) // 2])

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

    def minusOnePerformanceTest(self):
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

            prediction = self.autoComplete.getPredictions(word[:-1])

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

    def twoThirdWordPerformanceTest(self):
        print("Testing for correct predictions given 2n//3 characters...")
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

            prediction = self.autoComplete.getPredictions(word[0 : 2 * len(word) // 3])

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run different test cases based on the type provided. Provide test corpus.")
    
    # Add --type argument with possible values
    parser.add_argument('--type', type=str, required=True, choices=['half', 'twoThirds', 'minusOne'],
                        help="Specify the type of test to run: 'half' or 'minusOne'")
    
    # Add --corpus argument
    parser.add_argument('--corpus', type=str, required=False,
                        help="Specify the directory of test corpus to run.")
    
    args = parser.parse_args()
    if args.corpus is None:
        exit("Invalid directory")
    if not(os.path.isfile(args.corpus)):
        exit("Invalid directory")

    performanceTests = PerformanceTests(args.corpus)

    if args.type == "half":
        performanceTests.halfWordPerformanceTest()
    elif args.type == "minusOne":
        performanceTests.minusOnePerformanceTest()
    elif args.type == "twoThirds":
        performanceTests.twoThirdWordPerformanceTest()
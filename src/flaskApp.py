import os
import argparse
from flask import Flask, render_template, request
import AutoComplete
app = Flask(__name__)

parser = argparse.ArgumentParser(description="Run different test cases based on the type provided. Provide test corpus.")
    
# Add --corpus argument
parser.add_argument('--corpus', type=str, required=False,
                    help="Specify the directory of test corpus to run.")

args = parser.parse_args()
if args.corpus is None:
     exit("Invalid directory")
if not(os.path.isfile(args.corpus)):
        exit("Invalid directory")

autoComplete = AutoComplete.AutoComplete(args.corpus)

@app.route("/", methods=['GET', 'POST'])
def default():
    """
        Default method for rendering home page.

        :return: Base html page
        :rtype: Flask Template
    """
    return render_template("base.html")

@app.route('/get_text', methods=['POST'])
def get_text():
    """
        Retrieves user input from html form.

        :return: User input in html form
        :rtype: String
    """
    userInput = request.form['userInput']
    result = getAutoCompletions(userInput)
    return result

def getAutoCompletions(userInput):
    """
        Generates and formats auto completions from userInput.

        :param string userInput: Whole line of user input
        :return: String of all available auto completions
        :rtype: String
    """
    if len(userInput) == 0:
        return ""
    if str(userInput)[-1] == " ":
         return ""
    
    # Get last word of user input and generate predictions
    lastWord = userInput.split(" ")[-1]

    predictions = autoComplete.getPredictions(lastWord)
    
    # Formatting for predictions
    if len(predictions) > 0:
        if len(predictions) == 1:
            return f"Did you mean...\n {predictions[0]}?"  
        
        predStr = "Did you mean... \n"

        for i in range(len(predictions)-1):
            predStr += predictions[i] + " or "
            
        predStr += predictions[i+1] + "?"

        return predStr
    else:
         return ""

if __name__ == "__main__":
    app.run(debug="True")
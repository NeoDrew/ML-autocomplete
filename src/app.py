from flask import Flask, render_template, request
import autoComplete
app = Flask(__name__)

autoC = autoComplete.autoComplete()

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return render_template("base.html")

@app.route('/get_text', methods=['POST'])
def get_text():
    userInput = request.form['userInput']
    result = getAutoCompletions(userInput)
    return result

def getAutoCompletions(userInput): 
    print(userInput)
    if len(userInput) == 0:
        return ""
    if str(userInput)[-1] == " ":
         return ""
    
    #Get last word of user input
    lastWord = userInput.split(" ")[-1]

    predictions = autoC.getPredictions(lastWord)
    
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
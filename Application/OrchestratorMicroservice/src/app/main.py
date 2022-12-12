from flask import Flask

app = Flask(__name__)

@app.route("/app/bestnode/")
def getBestNode():
    
    BestNode= ""
    return BestNode

@app.route("/app/traimodel/")
def trainModel():
    
    return "Trained"
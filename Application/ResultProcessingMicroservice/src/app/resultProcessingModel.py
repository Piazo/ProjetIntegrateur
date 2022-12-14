from flask import Flask

app = Flask(__name__)

class resultProcessingModel : 
    @app.route("ResultProcessingModel")
    def __init__(self, num, latence):
        self.num = num
        self.latence = latence

    def getNumNode ():
        return self.num 

    def getLatenceNode():
        return self.latence

    def setNumNode(numNode):
        self.num = numNode

    def setLatenceNode(latenceNode):
        self.latence = latenceNode

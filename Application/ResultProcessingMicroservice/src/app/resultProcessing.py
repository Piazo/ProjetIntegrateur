import resultProcessingModel
from flask import Flask, request

app = Flask(__name__)

class resultProcessingControler(): 
    @app.route("/getResult")
    #Fonction qui choisit le meilleur noeur parmis ces noeuds
    def best_node():
        best = DBL_MAX 
        listNode= request.get_json(force=True)
        for key, value in listNode.items() :
            if value > best : 
                best = value
                bestNode = key
        return bestNode



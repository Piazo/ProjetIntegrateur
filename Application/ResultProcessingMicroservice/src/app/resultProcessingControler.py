import resultProcessingModel
from flask import Flask

app = Flask(__name__)

class resultProcessingControler(): 
    @app.route("ResultProcessingControler", method=['POST'])
    #Fonction qui reçoit les latences des noeuds

    #Fonction qui choisit le meilleur noeur parmis ces noeuds
    def best_node(listNode):
        best = 10000
        for i in listNode :
            if listNode[i] > best : 
                best = listNode[i]
                bestNode = i 
        return bestNode

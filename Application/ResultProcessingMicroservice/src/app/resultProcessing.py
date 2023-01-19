from flask import Flask, request

app = Flask(__name__)

class resultProcessingControler(): 
    @app.route("/getResult")
    #Fonction qui choisit le meilleur noeur parmis ces noeuds
    def best_node():
        best = 10000000
        listNode= request.get_json(force=True)
        for i in range(len(listNode)):
            value= float(listNode[i])
            if value < best : 
                best = value
                bestNode = i+1
        return str(bestNode)



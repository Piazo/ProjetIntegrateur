from urllib.request import urlopen
from flask import Flask, jsonify, request
import json
# import dataProcessing
# import modelMicroservice
# import resultProcessingControler
import requests

app = Flask(__name__)

class orchestator:
    @app.route("/app/bestnode/")
    def getBestNode():
        # get json from url
        jsonUrl = urlopen(url)
        data = json.loads(jsonUrl.read())
        #appeler fonction from dataprocessing
        listNode= []
        #appeler la fonction model pour chaque noeud
        nodeLatency=[]
        #for i in listNode:
            #node_latency.append(getlatencymodel)
        #get best node from resultprocessing
        bestNode=1
        return bestNode

    @app.route("/app/changezone/{int:zone}")
    def changezone(zone: int):
        # send messge to global orchestrator
        return 0

    @app.route("/app/getLatency", methods=['POST'])
    def getLatency():
        node = request.get_json(force=True)
        print(node)
        print(request)
        print(jsonify(node))
        res = requests.post('http://localhost:5000/predict', json=node)
        return res.text


    @app.route("/app/traimodel/")
    def trainModel():
    
        return "Trained"

from urllib.request import urlopen
from flask import Flask, jsonify, request
import json
# import dataProcessing
# import modelMicroservice
# import resultProcessingControler
import requests

app = Flask(__name__)

class orchestator:
    @app.route("/app/bestnode/", methods=['POST'])
    def getBestNode():
        # get json from url
        data = request.get_json(force=True)
        #create a list with all the nodes
        #jsonify each node + send to prediction microservice 
        #send list of latencies to result processing microservice and return the best nodes
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

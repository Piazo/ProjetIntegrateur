from urllib.request import urlopen
from flask import Flask, jsonify, request
import json
# import dataProcessing
# import modelMicroservice
# import resultProcessingControler
import requests

app = Flask(__name__)

class orchestator:
    @app.route("/app/bestnode/", methods=['GET'])
    def getBestNode():
       
        latencyList= []
        #jsonify each node + send to prediction microservice 
        for i in range(3):
            latency= requests.get('http://localhost:5000/predict/node=i+1')
            lat=latency.get_json(force=True) #tester si ça marche
            latencyList.append(requests.get(lat["latency1"]))

        #send list of latencies to result processing microservice and return the best nodes
        latencies=jsonify(latencyList)
        bestNode=requests.get('http://localhost:5001/getResult', json=latencies)
        return bestNode

    @app.route("/app/changezone/{int:zone}")
    def changezone(zone: int):
        # send messsge to global orchestrator
        url=requests.get('http://localhost:4998/getUrl/{int:zone}')
        return url

    @app.route("/app/getLatency", methods=['POST'])
    def getLatency():
        node = request.get_json(force=True)
        print(node)
        print(request)
        print(jsonify(node))
        res = requests.post('http://localhost:5000/predict', json=node)
        return res.text


# from urllib.request import urlopen
from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)

class orchestator:
    @app.route("/app/bestnode/", methods=['GET', 'POST'])
    def getBestNode():
        if request.method == "POST":
            prev = request.get_json(force=True)
        latencyList= []
        bestNode={}
        #send requests to prediction microservice 
        for i in range(3):
            latency= requests.get('http://localhost:50000/predict?node=1')
            latencyList.append(latency.text)
        print(latencyList)
        latency= requests.post('http://model1:5000/predict', json=prev)
        print(latency.text)

        #send list of latencies to result processing microservice and return the best nodes
        bestNode=requests.get('http://localhost:50001/getResult', json=latencyList)
        return bestNode.text

    @app.route("/app/changezone/", methods=['GET'])
    def changezone():
        args = request.args
        zone = args.get('zone')
        # send messsge to global orchestrator
        url=requests.get('http://localhost:50003/getUrl?zone=1')
        return url.text


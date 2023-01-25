from urllib.request import Request
from flask import Flask, jsonify, request
import json
import requests


app = Flask(__name__)

class globalOrchestrator:
    @app.route("/getUrl", methods=['GET'])
    def getNewZone():
        args = request.args
        zone = args.get('zone')
        if (zone=="1"):
            #l'orchestrator renvoie au local orchestrator l'url du local orchestrator 1 
            latency= requests.get('http://orch:5000/app/bestnode/')
        elif (zone=="2"):
            #l'orchestrator renvoie au local orchestrator l'url du local orchestrator 2 
            latency= requests.get('http://orch:5000/app/bestnode/')
        elif (zone=="3"):
            #l'orchestrator renvoie au local orchestrator l'url du local orchestrator 3 
            latency= requests.get('http://orch:5000/app/bestnode/')
        return latency
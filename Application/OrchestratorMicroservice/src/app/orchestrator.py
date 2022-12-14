from urllib.request import urlopen
from flask import Flask
import json

app = Flask(__name__)

import dataProcessing
import modelMicroservice
import resultProcessingControler

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
        for i in listNode:
            #node_latency.append(getlatencymodel)
        #get best node from resultprocessing
        bestNode=1
        return bestNode

    @app.route("/app/changezone/{int:zone}")
    def changezone(zone: int):
        # send messge to global orchestrator



    @app.route("/app/traimodel/")
    def trainModel():
    
        return "Trained"

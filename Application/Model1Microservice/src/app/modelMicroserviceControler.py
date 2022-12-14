#!/usr/bin/env python
# encoding: utf-8

from typing_extensions import Self
from flask import Flask, jsonify, request
import random
import modelMicroserviceModel

app = Flask(__name__)

class modelMicroserviceControler:

    def predictedLatency(ram, cpu, numNode):
        latency= []
        for i in range(10):
            latency[i] = abs((ram + cpu - numNode) * random.random())
        return latency

    @app.route("/predict", methods=['POST'])
    def predict():
        node = request.get_json(force=True)
        nodeInfos= modelMicroserviceModel.__init__(self, [], node["cpu"], node["numNode"], node["ram"])
        nodeInfos.setLatenceList(predictedLatency(nodeInfos.ram, nodeInfos.cpu, nodeInfos.numNode))
        print(nodeInfos.latenceList)
        return jsonify({
            "latency": predictedLatency(node["ram"], node["cpu"], node["jspQuoi"])
            })

    @app.route("/predict", methods=['GET'])
    def predicts():
        return "hihi"


    
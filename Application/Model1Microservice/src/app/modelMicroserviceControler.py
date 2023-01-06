#!/usr/bin/env python
# encoding: utf-8

from typing_extensions import Self
from flask import Flask, jsonify, request
import random
import modelMicroserviceModel

app = Flask(__name__)

class modelMicroserviceControler:

    def predictedLatency(ram, cpu, numNode):
        latency= abs((ram + cpu - numNode) * random.random())
        return latency

    @app.route("/predict", methods=['POST'])
    def predict():
        node = request.get_json(force=True)
        latency= modelMicroserviceControler.predictedLatency(node["ram"], node["cpu"], node["numNode"])
        # créer BDD pour stocker la file
        # ajouter la dernière latence à la file + supprimer la première
        return jsonify({
            "latency1": latency
            })



    
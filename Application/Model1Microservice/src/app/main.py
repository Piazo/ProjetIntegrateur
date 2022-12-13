#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, jsonify, request
import random

app = Flask(__name__)

def model(ram, cpu, jspQuoi):
    latency = abs((ram + cpu - jspQuoi) * random.random())
    return latency

@app.route("/predict", methods=['POST'])
def predict():
    node = request.get_json(force=True)
    print(model(node["ram"], node["cpu"], node["jspQuoi"]))
    return jsonify({
        "latency": model(node["ram"], node["cpu"], node["jspQuoi"])
        })

@app.route("/predict", methods=['GET'])
def predicts():
    return "hihi"
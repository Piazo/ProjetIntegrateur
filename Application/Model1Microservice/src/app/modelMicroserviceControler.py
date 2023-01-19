#!/usr/bin/env python
# encoding: utf-8


from typing_extensions import Self
from flask import Flask, jsonify, request
import random
#import modelMicroserviceModel
#import mysql.connector 


app = Flask(__name__)

class modelMicroserviceControler:

    def predictedLatency():
        latency= random.random()
        return latency

    @app.route("/predict", methods=['GET'])
    def predict(): 
        args = request.args
        node = args.get('node')
        latency= str(modelMicroserviceControler.predictedLatency())

        #Connexion à la BDD
        #conn = mysql.connector.connect(host="localhost", user="root", password="Projet2023+", database="latency")
        #cursor=conn.cursor()
        # ajouter la dernière latence à la file + supprimer la première
        #cursor.execute("""INSERT INTO latency1(id, valueLatency) VALUES(?, ?)""", (1, 0.0123456789))
        #conn.commit()
        #cursor.execute("""INSERT INTO latency1(id, valueLatency) VALUES(?, ?)""", (2, 0.0987654321))
        #conn.commit()
        #cursor.execute("""DELETE FROM latency1 where id=1""")
        #conn.commit()


        return latency





    
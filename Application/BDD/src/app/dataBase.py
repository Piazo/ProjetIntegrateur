
from urllib.request import urlopen
from pymongo import MongoClient
from flask import Flask, request
import json

app = Flask(__name__)

class dataBase:
    @app.route("/getDB")
    def get_latencies_database():
        
        client = MongoClient(host='localhost', port=27017)
        #mongodb://mongodb:27017
        db=client['database'] 
        node1_coll = db['node1_coll'] 
        node2_coll = db['node2_coll'] 
        node3_coll = db['node3_coll'] 
        latencies1= []
        latencies2= []
        latencies3= []
        last_six1 = node1_coll.find().sort("_id", -1).limit(6)
        last_six2 = node2_coll.find().sort("_id", -1).limit(6)
        last_six3 = node3_coll.find().sort("_id", -1).limit(6)
        
        for doc in last_six1:
            latencies1.append(doc.get("Moyenne"))
        for doc in last_six2:
            latencies2.append(doc.get("Moyenne"))
        for doc in last_six3:
            latencies3.append(doc.get("Moyenne"))
        
        data = [latencies1, latencies2, latencies3]

        json_data = json.dumps(data)
        
        return json_data
        

    @app.route("/insert", methods=['POST']) 
    def insert_database():
        json_data= request.get_json(force=True)
        node = str(json_data.get('node'))
        Moyenne= json_data.get('moyenne')
        data=[{"Moyenne":float(Moyenne)}]
        
        client = MongoClient(host='localhost', port=27017)
        db=client['database'] 
        if (node=='1'):
            db.node1_coll.insert_many(data)
        if (node=='2'):
            db.node2_coll.insert_many(data)
        if (node=='3'):
            db.node3_coll.insert_many(data)
        return "insert ok"
import pymongo
from urllib.request import urlopen
from pymongo import MongoClient
from flask import Flask
import json

app = Flask(__name__)

class dataBase:
    @app.route("BDDMicroservice/", methods=['POST']) 
    def get_database():
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
       # CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
        
        # Create a connection using MongoClient
        client = MongoClient(host='localhost', port=27017)
        db=client['database'] 
        node1_coll = db['node1'] 
        node2_coll = db['node2'] 
        node3_coll = db['node3']  
        return db

#  This is added so that many files can reuse the function get_database()
#  if __name__ == "__main__":   
        

    @app.route()
    def insert_database(db, data):
        db.node1_coll.insert(data)

    


# Get the database
# dbname = get_database()
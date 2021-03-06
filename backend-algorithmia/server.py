# coding: utf-8
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import config 

app = Flask(__name__)
app.config["MONGO_URI"] =config.MONGO_URI
mongo = PyMongo(app)
cors = CORS(app)
app.json_encoder = config.JSONEncoder

@app.route("/api/algorithm/")
@cross_origin()
def all():
    algo = mongo.db.algorithms
    output = []
    for doc in algo.find():
        output.append(doc)
    return jsonify(output)

@app.route("/api/algorithm/<name>")
@cross_origin()
def single(name):
    output = mongo.db.algorithms.find_one_or_404({'name':name})
    return jsonify(output)

@app.route("/api/cat/<name>")
@cross_origin()
def cat(name):
    algo = mongo.db.algorithms.find( {"$or": [ { "category": name }, { "tags": name }]})
    output = []
    for doc in algo:
        output.append(doc)
    return jsonify(output)

@app.route("/api/search/")
@cross_origin()
def search():
    q = request.args.get('q')
    algo = mongo.db.algorithms.find( { "$text": { "$search":  q} } )
    output = []
    for doc in algo:
        output.append(doc)
    return jsonify(output)
@app.route("/api/algorithm/predict/<name>")
@cross_origin()
def predict(name):
    output = {
        "result":name
    }
    return jsonify(output)

if __name__ == '__main__':
        app.run(host=config.SERVER_HOST,port=config.SERVER_PORT)
import pdb
import json
import datetime
from bson.json_util import dumps
from flask import Flask, escape, request, jsonify, make_response

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/formbuilder"
mongo = PyMongo(app)

def setup():
    mongo.db.forms.drop()
    mongo.db.rows.drop()

    mongo.db.forms.create_index([('user_id', pymongo.ASCENDING),])
    mongo.db.forms.insert_one({
        "user_id": 1,
        "id": 1,
        "name": "profile",
        "increcase": 0,
        "fields": [
            {
                "name": "name",
                "type": "input",
                "length": 50,
                "required": True
            },
            {
                "name": "email",
                "type": "email",
                "length": 500,
                "required": True
            },
            {
                "name": "position",
                "type": "input",
                "length": 100,
                "required": True
            },
            {
                "name": "company",
                "type": "input",
                "length": 100,
                "required": True
            },
            {
                "name": "bio",
                "type": "input",
                "length": 1000,
                "required": False
            }
        ]
    })

setup()


def get_database():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.form_builder
    return db

@app.route('/form/mongodb', methods=['POST'])
def submit():
    form_values = request.json
    form = mongo.db.forms.find_one({"id": 1})
    row = mongo.db.rows.insert_one(form_values)
    inserted_id = row.inserted_id
    form_values["_id"] = str(inserted_id)

    return form_values

@app.route('/form/mongodb/<id>/rows', methods=['GET'])
def fetch(id):
    db = get_database()
    page = request.args.get("page", 1)
    rows = dumps(mongo.db.rows.find(skip=(page - 1) * 100, limit=100))
    response = make_response(rows, 200)
    response.headers['Content-Type'] = 'application/json'
    return response
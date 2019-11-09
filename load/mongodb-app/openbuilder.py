from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/form/mongodb', methods=['POST'])
def submit():
    form_values = request.json
    return form_values

@app.route('/form/mongodb/<id>/rows', methods=['GET'])
def fetch(id):
    return f''
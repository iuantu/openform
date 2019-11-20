import pdb
import json
import datetime
import mysql.connector
from flask import Flask, escape, request, jsonify, make_response

app = Flask(__name__)

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="123456",
  database="formbuilder",
  auth_plugin='mysql_native_password',
)

def setup():
    cursor = db.cursor()
    cursor.execute("DROP DATABASE IF EXISTS formbuilder")
    cursor.execute("CREATE DATABASE IF NOT EXISTS formbuilder")
    cursor.execute("use formbuilder")
    cursor.execute("""CREATE TABLE IF NOT EXISTS forms(
        id bigint NOT NULL AUTO_INCREMENT,
        user_id bigint NOT NULL,
        name varchar(1000) NOT NULL,
        increcase bigint NOT NULL DEFAULT 0,
        CONSTRAINT forms_pk PRIMARY KEY (id)
    )
    """)

    cursor.execute("""CREATE INDEX user_id_index ON forms(user_id)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS fields(
        id bigint NOT NULL AUTO_INCREMENT,
        form_id bigint NOT NULL,
        name varchar(1000) NOT NULL,
        length int NOT NULL,
        required boolean NOT NULL DEFAULT false,
        CONSTRAINT field_pk PRIMARY KEY (id)
    )
    """)
    # cursor.execute("""CREATE INDEX user_id_index ON fields(user_id)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS `rows`(
        id bigint NOT NULL AUTO_INCREMENT,
        form_id bigint NOT NULL,
        user_id bigint NOT NULL,
        `values` JSON NOT NULL,
        CONSTRAINT `records_pk` PRIMARY KEY (id)
    )
    """)
    cursor.execute("""CREATE INDEX user_id_index ON `rows`(user_id)""")
    cursor.execute("""CREATE INDEX form_id_index ON `rows`(form_id)""")

    cursor.execute("""INSERT INTO forms (user_id, name) VALUES (1, "profile");""")
    cursor.execute("""INSERT INTO fields (form_id, name, length, required) VALUES (1, "name", 50, true),
    (1, "email", 500, true),
    (1, "title", 100, true),
    (1, "company", 100, true),
    (1, "bio", 1000, false)
    ;""")
    db.commit()

# try:
#     setup()
# except Exception as e:
#     print(e)

@app.route('/form/mysql', methods=['POST'])
def submit():
    form_values = request.json
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM forms WHERE id=2")
    form = cursor.fetchone()

    cursor.execute("SELECT * FROM fields WHERE form_id=1")
    fields = cursor.fetchall()
    
    statement = """INSERT INTO `rows` (form_id, user_id, `values`) VALUES (1, 1, '%s');""" % json.dumps(form_values)
    cursor.execute(statement)
    db.commit()

    form_values["id"] = cursor.lastrowid
    return form_values

@app.route('/form/mysql/<id>/rows', methods=['GET'])
def fetch(id):
    user_id = request.args.get("user_id", 1)
    page = request.args.get("page", 1)
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `rows` WHERE user_id = %d LIMIT 100 OFFSET %d" % (user_id, (page - 1) * 100))
    response = make_response(json.dumps(cursor.fetchall()), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
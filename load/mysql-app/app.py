import os
import pdb
import sys
import json
import click
import datetime
import mysql.connector
from mysql.connector import pooling
from flask import Flask, escape, request, jsonify, make_response
from mysql.connector.errors import ProgrammingError
from flask_dotenv import DotEnv

pooling.CNX_POOL_MAXSIZE = 100
POOL_SIZE=32

app = Flask(__name__)
env = DotEnv()
env.init_app(app, verbose_mode=True)

database_connect_configuration = dict(
    host=os.getenv('MYSQL_HOST', '127.0.0.1'),
    user=os.getenv('MYSQL_USER', 'root'),
    passwd=os.getenv('MYSQL_PASSWORD', ''),
    database=os.getenv('MYSQL_DATABASE', 'formbuilder'),
    auth_plugin='mysql_native_password',
)

print(database_connect_configuration)

try:
    config = database_connect_configuration.copy()
    config.update(pool_size=POOL_SIZE)
    pool = mysql.connector.pooling.MySQLConnectionPool(**config)

except ProgrammingError:
    print('database don\'t exists')
    # sys.exit(1)

# print(os.getenv('MYSQL_PASSWORD'))


@app.cli.command()
def setup():

    config = database_connect_configuration.copy()
    del config['database']
    db = mysql.connector.connect(**config)

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

@app.route('/form/mysql', methods=['POST'])
def submit():
    conn = pool.get_connection()

    form_values = request.json
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM forms WHERE id=2")
    form = cursor.fetchone()

    cursor.execute("SELECT * FROM fields WHERE form_id=1")
    fields = cursor.fetchall()

    user_id = form_values['user_id']
    form_id = form_values['form_id']

    del form_values['user_id']
    del form_values['form_id']

    parameters = {
        'user_id': user_id,
        'form_id': form_id,
        'values': json.dumps(form_values),
    }
    
    statement = "INSERT INTO `rows` (form_id, user_id, `values`) VALUES (%(form_id)d, %(user_id)d, '%(values)s');" % parameters
    
    cursor.execute(statement)
    conn.commit()

    cursor.close()
    conn.close()

    form_values["id"] = cursor.lastrowid
    return form_values


@app.route('/form/mysql/<id>/rows', methods=['GET'])
def fetch(id):
    conn = pool.get_connection()

    user_id = request.args.get("user_id", 1)
    page = request.args.get("page", 1)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `rows` WHERE user_id = %d LIMIT 100 OFFSET %d" % (user_id, (page - 1) * 100))
    response = make_response(json.dumps(cursor.fetchall()), 200)
    response.headers['Content-Type'] = 'application/json'

    cursor.close()
    conn.close()

    return response
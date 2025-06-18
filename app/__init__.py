from flask import Flask
from flask_dynamo import Dynamo

app = Flask(__name__)
app.config['DYNAMO_TABLES'] = [{'TableName': 'tasks', 'KeySchema': [{'AttributeName': 'id', 'KeyType': 'HASH'}]}]
dynamo = Dynamo(app)
dynamo.init_app(app)

from app import routes


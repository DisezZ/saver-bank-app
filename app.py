import sys
sys.path.append('/Saver Bank App/F')

from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
from F.feature_1 import feature_1
from F.index import index
from F.register import register
from F.login import login

app = Flask(__name__)

app.config['MONGO_URI']='mongodb+srv://Lutfee:9512095120@my-cluster-in0zc.gcp.mongodb.net/saver-bank-data?retryWrites=true&w=majority'
app.config['JWT_SECRET_KEY']='hjdsncjnsncijdscuasdkndlkmcjasdnckdcaqelq'

mongo=PyMongo(app)
bcrypt=Bcrypt(app)
jwt=JWTManager(app)

CORS(app)

@app.route('/')
def _index():
    tempt=index()
    return tempt

@app.route('/register/',methods=['POST','GET'])
def _register():
    tempt=register(mongo,bcrypt)
    return tempt

@app.route('/login/',methods=['POST','GET'])
def _login():
    tempt=login(mongo,bcrypt,jwt,create_access_token)
    return tempt

@app.route('/feature_1/', methods=['POST','GET'])
def _feature_1():
    tempt=feature_1(mongo)
    return tempt


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

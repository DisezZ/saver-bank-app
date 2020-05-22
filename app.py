import sys
sys.path.append('/Saver Bank App/F')

from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from F.feature_1 import feature_1
from F.index import index
from F.register import register

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/saver-bank-data'
}
app.config['MONGO_DBNAME']='saver-bank-data'
app.config['MONGO_URI']='mongodb://localhost:27017/saver-bank-data'

mongo=PyMongo(app)
bcrypt=Bcrypt(app)

@app.route('/')
def _index():
    tempt=index()
    return tempt

@app.route('/register/')
def _register():
    tempt=register(mongo,bcrypt)
    return tempt

# @app.route('/login',methods=['POST'])
# def _login():
#     tempt=login()
#     return tempt

@app.route('/feature_1/', methods=['POST'])
def _feature_1():
    tempt=feature_1(app)
    return tempt


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

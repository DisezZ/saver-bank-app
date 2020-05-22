from flask import request,jsonify
from datetime import datetime

def register(mongo,bcrypt):
    user=mongo.db.User_Data
    username=request.get_json()['username']
    email=request.get_json()['email']
    password=bcrypt.generate_password_hash(request.get_json()['password'])
    first_name=request.get_json()['first_name']
    last_name=request.get_json()['last_name']
    created=datetime.utcnow()
    if user.find_one({'username':username}) or user.find_one({'email':email}):
        return jsonify({
            "message":"Username or Email already exist",
            "status":"409"
        })
    else:
        user_id=user.insert({
        "first_name":first_name,
        "last_name":last_name,
        "username":username,
        "password":password,
        "email":email,
        "created":created
        })
        return jsonify({
            "message":"Register success",
            "status":"201"
        })
    
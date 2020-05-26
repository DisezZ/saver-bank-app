from flask import jsonify,request
def login(mongo,bcrypt,jwt,create_access_token):
    user=mongo.db.User_Data
    username=request.get_json()['username']
    password=request.get_json()['password']
    response1=user.find_one({'username':username})
    response2=user.find_one({'email':username})
    result = ""
    if response1:
        if bcrypt.check_password_hash(response1['password'],password):
            access_token=create_access_token({
                'first_name':response1['first_name'],
                'last_name':response1['last_name'],
                'email':response1['email']
            })
            result=jsonify({
                'token':access_token,
                'message':'Login Successful',
                'status':'200',
                'first_name':response1['first_name'],
                'last_name':response1['last_name'],
                'email':response1['email']
            })
        else:
            result=jsonify({
                'message':'Invalid email, username or password',
                'status':'409'
            })
    elif response2:
        if bcrypt.check_password_hash(response2['password'],password):
            access_token=create_access_token({
                'first_name':response2['first_name'],
                'last_name':response2['last_name'],
                'email':response2['email']
            })
            result=jsonify({
                'token':access_token,
                'message':'Login successful',
                'status':'200',
                'first_name':response2['first_name'],
                'last_name':response2['last_name'],
                'email':response2['email']
            })
        else:
            result=jsonify({
                'message':'Invalid email, username or password',
                'status':'409'
            })
    else:
        result=jsonify({
            'message':"This email or username didn't exists",
            'status':'409'
        })
    return result
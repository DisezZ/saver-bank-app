from flask import request,jsonify
from .hello import printf

def feature_1():
    try:
        get = request.get_json()
        # down here for calling north's functions
        
        return jsonify({'return':get['store_id']+get['years']+get['months']})
    except:
        return "An error or exception occurred" 
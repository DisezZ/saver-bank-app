from flask import request,jsonify
from .hello import printf

def feature_1():
    try:
        get = request.get_json()
        # down here for calling north's functions
        tempt=jsonify({'return':get['store_id']+get['years']+get['months']})    #Example, in this feature we have 3 variables that sended from yodjung
    except:
        print("An error or exception occurred")     # this is whre I return JSON back to Yoodjung
    return tempt
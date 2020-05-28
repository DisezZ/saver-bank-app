from flask import request,jsonify
from .AI import AI

def feature_1(mongo):
    #try:
        result=""
        get = request.get_json()
        query=mongo.db.Exist_Query
        check1=query.find_one({
            'store_id':get['store_id'],
            'years':get['years'],
            'months':get['months']
            })
        if check1:
            result=jsonify({
                'electric_predict':check1['electric_predict'],
                'base64_graph':check1['base64_graph'],
                'type':'Exist_Query'
            })
        # down here for calling north's functions
        else:
            elect_predict,encoded=AI(get['store_id'],get['years'],get['months'])
            query_id=query.insert({
                "store_id":get['store_id'],
                "years":get['years'],
                "months":get['months'],
                "electric_predict":elect_predict,
                "base64_graph":encoded.decode()
            })
            result=jsonify({
                'electric_predict':elect_predict,
                'base64_graph':encoded.decode(),
                'type':'Call_Fuction'
            })
        return result
    #except:
    #    return "An error or exception occurred" 
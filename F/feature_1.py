from flask import request,jsonify
from F.AI import AI

def feature_1(mongo):
    try:
        result=""
        get = request.get_json()
        query=mongo.db.Exist_Query
        check1=query.find_one({
            'store_id':get['store_id'],
            'years':get['years'],
            'months':get['months'],
            'date':get['date']
            })
        if check1:
            result=jsonify({
                'electric_predict':check1['electric_predict'],
                'base64_graph':check1['base64_graph'],
                'type':'Exist_Query'
            })
        else:
            # down here for calling north's functions~~~
            elect_predict,encoded=AI(get['store_id'],get['years'],get['months'],get['date'])

            query_id=query.insert({
                "store_id":get['store_id'],
                "years":get['years'],
                "months":get['months'],
                "date":get['date'],
                "electric_predict":str(elect_predict),
                "base64_graph":encoded.decode()
            })
            result=jsonify({
                'electric_predict':str(elect_predict),
                'base64_graph':encoded.decode(),
                'type':'Call_Fuction'
            })
        return result
    except:
        result=jsonify({
            'message':"An error or exception occurred"
        })
        return  result
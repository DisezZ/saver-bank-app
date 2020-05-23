def index():
    return '''<h1 style="text-align:center">Hello World<h1><br>
<h2>This API have 4 pages now<h2><br>
<h3>1.This index Pages, path = /<h3><br>
<h3>2.register API, path = /register<h3><br>
<p>
JSON key parameter = 'username','password','email','first_name','last_name'<br>return parameter = 'message','status'
<p><br><hr><br>
<h3>3.login API, path = /login<h3><br>
<p>
JSON key parameter = 'username','password'<br>return parameter = 'message','status'
<p><br><hr><br>
<h3>4. 1st Feature API, path = /feature_1<h3>
<p>
JSON key parameter = 'store_id','years','months'<br>return parameter = 'electric_prediction'
<p><br><hr><br>'''
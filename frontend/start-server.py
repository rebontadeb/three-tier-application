from flask import Flask , request, render_template,redirect
import urllib.request , json
import requests
from waitress import serve

app = Flask(__name__)
flaskThread=2


@app.route("/add-donors",methods=['GET'])
def donors_method_page():
    return render_template('add-donors.html')


@app.route("/add-donors",methods=['POST'])
def donors_method_add():
  name = request.form['name']
  pin = request.form['pincode']
  phone = request.form['phone']
  print(name,pin,phone)
  apiep = "http://localhost:14200/add-donor/v1"
  add_data={"name": name,"pin": pin,"phone": phone}
  headers = {'Content-Type': 'application/json'} 
  jsondata = json.dumps(add_data).encode("utf-8") 
  requests.post(apiep, data=jsondata, headers=headers)
  return redirect("/add-donors")

if __name__ == "__main__":
  serve(app,host='0.0.0.0',port=4200,threads=flaskThread)
  #app.run(debug=False,port=4200)
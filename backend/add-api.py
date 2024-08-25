from flask import Flask , request, render_template,jsonify
from flask_mysqldb import MySQL
from waitress import serve

app = Flask(__name__)
flaskThread=2

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'donors'

mysql = MySQL(app)


@app.route('/add-donor/v1', methods = ['POST']) 
def add_donor(): 
    cur = mysql.connection.cursor()
    name = request.json['name']
    pin = request.json['pin']
    phone = request.json['phone']
    if(request.method == 'POST'): 
        try:
            cur.execute('''INSERT INTO donorDemographic (donorName, pincode , phonenumber) VALUES (%s, %s,%s)''', (name,pin,phone))
            mysql.connection.commit()
            return jsonify({'message': 'Data added successfully'})
        except:
            return jsonify({'message': 'User already exists'})                
        cur.close()
        
  


if __name__ == "__main__":
  serve(app,host='0.0.0.0',port=14200,threads=flaskThread)
  #app.run(debug=False,port=4200)
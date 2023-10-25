from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name)


app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'mysql-host'  
app.config['MYSQL_DB'] = 'mydb'
mysql = MySQL(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM data')
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def add_data():
    text = request.json['text']
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO data (text) VALUES (%s)', (text,))
    mysql.connection.commit()
    cursor.close()
    return 'Data added'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

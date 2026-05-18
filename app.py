from flask import Flask, request, jsonify 
render_template
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
import mysql.connector

conn = mysql.connector.connect(
    host="viaduct.proxy.rlwy.net",
    user="root",
    password="dSAzQaOnMhInyIedWZTkpNFbGOktIVnK",
    database="railway",
    port=31842
)

cursor = conn.cursor()

print("Database Connected")

cursor = conn.cursor()

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():

    data = request.json

    print(data)

    query = """
    INSERT INTO patients(first_name, email)
    VALUES(%s, %s)
    """

    values = (
        data['firstName'],
        data['email']
    )

    cursor.execute(query, values)

    conn.commit()

    return jsonify({
        "message": "Patient Registered Successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)

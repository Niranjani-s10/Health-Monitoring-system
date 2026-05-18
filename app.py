from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Niranjani@10",
    database="hospital_management_system"
)

cursor = conn.cursor()

@app.route('/')
def home():
    return "Backend Running"

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

from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Lấy URL cơ sở dữ liệu từ biến môi trường
database_url = os.getenv('DATABASE_URL')

def get_db_connection():
    return mysql.connector.connect(database_url)

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(jobs)
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

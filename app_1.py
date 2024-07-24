from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Cấu hình để kết nối đến cơ sở dữ liệu từ biến môi trường
db_config = {
    'user': os.getenv('DB_USER', 'admin1'),
    'password': os.getenv('DB_PASSWORD', 'levanduy98'),
    'host': os.getenv('DB_HOST', 'database1.cx8wai4u8ztf.eu-west-3.rds.amazonaws.com'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'database': os.getenv('DB_NAME', 'test1')
}

# Kết nối đến cơ sở dữ liệu
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Kiểm tra kết nối
@app.route('/api/test_db_connection', methods=['GET'])
def test_db_connection():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return jsonify({"status": "success", "message": "Database connection successful", "result": result})
    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)})

# Endpoint để lấy tất cả công việc
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs_indeed_finance")  # Đảm bảo bảng `jobs_indeed_finance` tồn tại trong cơ sở dữ liệu của bạn
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    jobs = []
    for row in rows:
        jobs.append({
            'ID': row['ID'],
            'Title': row['Title'],
            'Location': row['Location'],
            'Salaire': row['Salaire'],
            'Description': row['Description'],
            'URL': row['URL']
        })
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)

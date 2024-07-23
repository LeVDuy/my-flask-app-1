from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Cấu hình để kết nối đến cơ sở dữ liệu
db_config = {
    'user': 'admin1',
    'password': 'levanduy98',
    'host': 'database1.cx8wai4u8ztf.eu-west-3.rds.amazonaws.com',
    'port': 3306,
    'database': 'test1'
}

# Kết nối đến cơ sở dữ liệu
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Endpoint để lấy tất cả công việc
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs_indeed_finance")  # Đảm bảo bảng `jobs_indeed_finance` tồn tại trong cơ sở dữ liệu của bạn
    jobs = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(jobs)

# Endpoint cho root URL
@app.route('/')
def home():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

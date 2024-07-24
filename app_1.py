from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Cấu hình để kết nối đến cơ sở dữ liệu
db_config = {
    'user': '',
    'password': '',
    'host': '',
    'port': ,
    'database': ''
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
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    jobs = []
    for row in rows:
        jobs.append({
            'ID': row['ID'],
            'Iitle': row['Title'],
            'Location' : row['Location'],
            'Salaire' : row['Salaire'],
            'Description': row['Description'],
            'URL': row['URL']
        })
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)

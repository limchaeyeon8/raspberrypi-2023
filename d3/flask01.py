# Flask 웹 서버
from flask import Flask

app = Flask(__name__)

@app.route('/')     # http://localhost:5000/ <--- 이 위치
def index():
    return 'Hello, Flask!!!'

if __name__ == '__main__':
    # app.run(host='localhost')                 # 기본 포트번호 5000번
    app.run(host='localhost', port='8000', debug=True)      # 포트번호 지정 / 디버그 모드
# Flask 웹 서버
from flask import Flask, render_template        # 함수

app = Flask(__name__)

@app.route('/hello')     # http://localhost:5000/hello <--- 이 경로
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # app.run(host='localhost')                 # 기본 포트번호 5000번
    app.run(host='localhost', port='8000', debug=True)      # 포트번호 지정 / 디버그 모드
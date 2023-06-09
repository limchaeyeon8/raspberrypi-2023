# raspberrypi-2023
라즈베리파이 학습 리포지토리

## 1일차 - 2일차
- 라즈베리파이 학습
    - 라즈베리파이 소개
    - 라즈비안 설치
        - Bullseye
    - 라즈비안 설정
        - 기본 업데이트 / 업그레이드
        - 한글 폰트 및 입력기
        - Screensaver 화면 꺼짐 방지
        - Wifi 연결 끊김 해제
    - Pi-apps
        - Visual Studio Code 설치
        - Github Desktop 설치 및 설정
    - Visual Studio Code
        - Python 플러그인
    - 리눅스 기본
        - 리눅스 명령어 ( 대표 20여가지 )
    - Pygames로 단순 Drawing App

## 3일차
- 라즈베리파이 학습
    - 통신 설정
        - AnyDesk 실패,,
    - 리눅스 일반
        - 서비스 실행 / 확인 / 종료
            - systemctl [start|stop|status] 서비스명
        - MySQL DB
            - 암호설정 => set password for 'root'@'localhost' = password('12345'); ----> flush privileges;
            - nano /etc/mysql/mariadb.conf.d/50-server.cnf ==> bind-address            = 127.0.0.1 주석처리
            - sudo mysql -u root ==> grant all privileges on *.* to 'root'@'%' identified by '12345'; ==> use mysql;
    - Flask 기본

        - Web Server 프로그래밍
"""
fastAPI 사용법:
    1. import
    2. instance 생성
    3. 사용할 함수 만들기
    4. 함수 인스턴스 메서드 데코레이터로 감싸주기
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')       # path 설정, '/'는 local host 8000을 의미
def index_():
    return {'data': {'name': 'LSR'}}           # api에서는 json을 주로 쓰므로 dict를 써보자


@app.get('/about')
def about_page():
    return {'data': 'This is about page'}  
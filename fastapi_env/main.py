"""
fastAPI 사용법:
    1. import
    2. instance 생성
    3. 사용할 함수 만들기
    4. 함수 인스턴스 메서드 데코레이터로 감싸주기(경로 지정)
"""
  """_summary_

  터미널에서 실행하는 방법
  uvicorn (파일 이름):(FastAPI 인스턴스) --reload(리로드 기능을 원할 시) 
  
  reload 기능이란? 
    - ctrl + S로 저장만 하면 서버가 재시작되고 코드의 수정사항이 반영됨
    
    @app.get('/about')         -> get, post, delete 등 operation 
    def about_page():
    return {'data': 'This is about page'}  
  """



from fastapi import FastAPI

app = FastAPI()


@app.get('/')       # path 설정, '/'는 local host 8000을 의미
def index_():
    return {'data': {'name': 'LSR'}}           # api에서는 json을 주로 쓰므로 dict를 써보자


@app.get('/about')
def about_page():
    return {'data': 'This is about page'}  
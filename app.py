import response
from flask import Flask
from flask import render_template
from flask import request, make_response
app = Flask(__name__)
#쿠키와 세션
# 회원가입하면 쿠키를 서버에서 줌
# 회원가입정보 디비에 연동해서 넣기

from pymongo import MongoClient
client = MongoClient('mongodb+srv://taesikyoon97:louis17467@cluster0.ncjxm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta
ID = 'test'
PW = 'taesik'
@app.route("/")
def index():
    return  render_template('index.html')


@app.route("/login", methods=['GET'])
def login():
    user_id = request.args.get('userID')
    print(user_id)
    return render_template('login.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
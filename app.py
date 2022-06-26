from flask import Flask, render_template, request, jsonify, make_response
from pymongo import MongoClient
import datetime
import bcrypt, jwt
from functools import wraps


app = Flask(__name__)

# app.config['SECRET_KEY'] = 'hello'
SECRET_KEY = 'hello'
app.config['JSON_AS_ASCII'] = False
client = MongoClient('mongodb+srv://taesikyoon97:louis17467@cluster0.ncjxm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


# 토큰 유효성 검사
def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({"message": 'Token is missing'}),403
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return jsonify({"message": 'Token is invaild'}),403

        return f()(*args,**kwargs)
    return decorated

# 메인화면
@app.route('/')
@token_required
def index():
    return render_template('index.html')


@app.route("/login", methods=['POST'])
def login():
    if request.method == "POST":
        data_user = request.get_json() # 데이터 전달 받기 - json 타입으로 받음
        db_user = db.test.find_one({'id': "data_user['id']"})
        if db_user == None: return jsonify({"message":"아이디를 제대로 입력해주세요."})
        check_pw = bcrypt.checkpw(data_user['pw'].encode("utf-8"), db_user['pw'])
        if check_pw == False: return jsonify({"message":"비밀번호를 제대로 입력해주세요."})

        # 토큰 생성
        else:
            payload = {
                'id': db_user['id'],
                'exp': datetime.utcnow() + datetime.timedelta(minutes=3)  # 로그인 3분 유지
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            return jsonify({'result': 'success', 'access_token': token})

@app.route("/sign_up", methods=['POST'])
def sign_up():
    if request.method == "POST":
        data_user = request.get_json()
        pw_member = bcrypt.hashpw(data_user['pw'].encode("utf-8"), bcrypt.gensalt())
        doc = {
            'id': data_user['id'],
            'pw': pw_member
        }
        db.members.insert_one(doc)
        return jsonify({'result': 'success'})

@app.route('/check_up',methods=['POST'])
def check_same_id():
    if request.method == 'POST':
        data_user = request.get_json()
        db_user = db.test.find_one({'id': data_user['id']})
        if data_user == None: return jsonify({"message":"사용 가능한 아이디 입니다."})
        else: return jsonify({"message": "중복된 아이디 입니다."})



if __name__ == '__main__':
    app.run(debug=True)


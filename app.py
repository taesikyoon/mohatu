from flask import Flask,render_template,request,jsonify
import jwt,bcrypt

from pymongo import MongoClient
client = MongoClient('mongodb+srv://taesikyoon97:louis17467@cluster0.ncjxm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template('login.html')

@app.route("/join_member", methods=["POST","GET"])
def join_member():
    join_member_mail = request.form['member_mail_give']
    join_member_id = request.form['member_id_give']
    join_member_pw = request.form['member_pw_give']
    # 중복 확인 디비 확인해봐야해서 잘모르겠다
    user = db.users.find_one({'id': ""},{"mail":""})
    #비밀번호 암호화
    encrypted_password = bcrypt.hashpw(join_member_mail.encode("utf-8"), bcrypt.gensalt())
    doc = {
        "mail":join_member_mail,
        "id": join_member_id,
        "pw": join_member_pw,
    }
    db.users.insert_one(doc)
    return jsonify({"result":"join"})





if __name__ == '__main__':
  app.run('0.0.0.0',port=5000,debug=True)

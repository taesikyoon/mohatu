from flask import Flask, render_template, request, session, url_for,redirect
from pymongo import MongoClient
# 데이타임? 시간을 만들어준다고해야하나 아무튼 시간함수가있따
# 시간함수는 세션의 유통기한을 정할때 쓸것이다
client = MongoClient('mongodb+srv://taesikyoon97:louis17467@cluster0.ncjxm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

# 세션 암호화
app.secret_key = "ptmq6dhs2#$%!l"

#메인화면

@app.route("/",methods=['GET'])
def index():
    if "user" in session : return render_template('index.html',login=True)
    else : return redirect(url_for("login"))

#로그인 화면
@app.route("/login", methods=['POST','GET']) # POST와 GET 을 내주니 오류 없이 됐다...이유는 알수없음..
def login():
    if request.method == "POST":
      # test= request.form.get('id_give', False)
        user = request.form['id_give']
        session['user'] = user
        return redirect(url_for('index'))
    else :
        if "user" in session:
            return redirect(url_for('index'))
# 회원가입
app.route("/join_member", methods=["POST"])
def join_member():
    #회원가입 필요[ 이름,나이,성별,이메일,주소,전화번호,아이디,비밀번호,비밀번호 재확인,아이디 중복확인버튼]
    # 간단하게는 이름 아이디 비밀번호 필요함
    pass

#test shop,newspage,webtoon >> 등으로 세션 유지 확인
app.route('/user')
def user():
    return "well come " + user

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
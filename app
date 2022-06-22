# app.py
from flask import Flask ,render_template, request,session,redirect,url_for,jsonify
app = Flask(__name__)

# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://taesikyoon97:louis17467@cluster0.ncjxm.mongodb.net/Cluster0?retryWrites=true&w=majority')
# db = client.dbsparta

app.secret_key='hello'

ID = "test"
PW = "taesik"
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('id_give',False)
        user_pw = request.form.get('pw_give',False)
        print(type(user_id),user_pw)
        if ID == user_id and PW == user_pw:
            print(user_id)
            return jsonify({'restul':'success'})
        else:return jsonify({'restul':'fail'})
    else: return render_template('login.html')
app.route('/user')
def user():
    return "user 페이지"

if __name__ == '__main__':
  app.run('0.0.0.0',port=5000,debug=True)

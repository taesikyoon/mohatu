from pymongo import MongoClient
client = MongoClient('mongodb+srv://taesikyoon97:louis17467@cluster0.ncjxm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name' : 'bob',
    'age' : 27
}
# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})



db.users.insert_one({'name': 'body', 'age': 29})
db.users.insert_one({'name': 'louis', 'age': 21})
db.users.insert_one({'name': 'can', 'age': 19})
db.users.insert_one({'name': 'mac', 'age': 24})

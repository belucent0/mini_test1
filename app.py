from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.j20ekdf.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/guestbook", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    print(name_receive, comment_receive)

    doc = {
        'name': name_receive,
        'comment': comment_receive}
    db.dev9.insert_one(doc)


    return jsonify({'msg': '응원작성 완료!'})


@app.route("/guestbook", methods=["GET"])
def homework_get():
    comment_list = list(db.dev9.find({}, {'_id': False}))
    return jsonify({'comment' : comment_list})




@app.route("/joins", methods=["POST"])
def web_mars_post():
    nickname_receive = request.form['nickname_give']
    job_receive = request.form['job_give']
    self_receive = request.form['self_give']
    doc = {
        'nickname': nickname_receive,
        'job': job_receive,
        'self': self_receive,
    }
    db.dev9_join.insert_one(doc)

    return jsonify({'msg': '가입 신청 완료'})

@app.route("/joins", methods=["GET"])
def web_mars_get():
    order_list = list(db.dev9_join.find({}, {'_id': False}))
    return jsonify({'orders': order_list})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
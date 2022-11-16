from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()

client = MongoClient('')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    print(name_receive, comment_receive)

    doc = {
        'name': name_receive,
        'comment': comment_receive}
    db.homeworks.insert_one(doc)


    return jsonify({'msg': '응원작성 완료!'})



@app.route("/homework", methods=["GET"])
def homework_get():
    comment_list = list(db.homeworks.find({}, {'_id': False}))
    return jsonify({'comment' : comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import psutil

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

    def __init__(self):
        self.count = 0

@app.route('/hello/:<name>', methods=['GET'])
def hello_name(name):
    v = Visit.query.first()
    v.count +=1
    db.session.commit()
    return 'Hello, ' + name + '!'

@app.route("/health", methods=['GET'])
def health():
    p = psutil.Process()
    json_body = {
        "cpu_percent": p.cpu_percent(interval=None),
        "cpu_times": p.cpu_times(),
        "mem_info": p.memory_info(),
        "mem_percent": p.memory_percent()
    }
    return jsonify(json_body), 200

@app.route('/counts', methods=['GET'])
def counts():
    v = Visit.query.first()
    return jsonify(counter=v.count)

@app.route('/counts', methods=['DELETE'])
def reset():
    v = Visit.query.first()
    v.count = 0
    db.session.commit()
    return 'Count reset.'

if __name__ == "__main__":
    app.run(debug=True)


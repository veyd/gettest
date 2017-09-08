from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/hello/:<name>')
def hello_name(name):
    return 'Hello, ' + name + '!'

@app.route('/health')
def health():
    p = psutil.Process()
    json_body = {
        "cpu_percent": p.cpu_percent(interval=None),
        "cpu_times": p.cpu_times(),
        "mem_info": p.memory_info(),
        "mem_percent": p.memory_percent()
    }
    return jsonify(json_body), 200

@app.route('/counts')
def counts():
    return 'Count!'

from flask import Flask

app = Flask(__name__)

@app.route('/hello/:<name>')
def hello_name(name):
    return 'Hello, ' + name + '!'

@app.route('/health')
def health():
    return 'Metrics:'

@app.route('/counts')
def counts():
    return 'Count!'

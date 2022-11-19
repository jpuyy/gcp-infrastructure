from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'My service a, v1-1-2'

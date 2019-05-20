from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World.. first program on AWS"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

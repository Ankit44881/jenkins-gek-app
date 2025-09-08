from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Ankit's app deployed via Jenkins on GKE!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

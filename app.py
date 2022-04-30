from flask import Flask

app = Flask(__name__)

@app.route('/',methods = ['GET','PUSH'])
def index():
    return "Hello World"


if __name__ =='__main__':
    app.run(port = 8080,debug = True)
from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "Hello world!"

@app.route("/new/")
@app.route("/новаястраница/")
def new():
    return "new page"


if __name__ == "__main__":
    app.run()



from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def hello():
    return "Hello from the really smallest Flask webapp there is!"


@app.get("/bye")
def byebye():
    return "Goodbye from the really smallest Flask webapp there is!"


@app.get("/whoops")
def omg():
    first = 10
    second = 50

    return str(first / second)


if __name__ == "__main__":
    app.run(debug=True)

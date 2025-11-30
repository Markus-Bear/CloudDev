from flask import Flask, render_template

app = Flask(__name__)


@app.get("/hello")
def hello():
    return render_template(
        "hello.html",
        the_title="This is HELLO",
    )


@app.get("/bye")
def byebye():
    return "Goodbye from the really smallest Flask webapp there is!"


@app.get("/whoops")
def omg():
    first = 10
    second = 50

    return render_template(
        "whoops.html",
        result=first / second,
        the_title="The Results are in!",
    )


if __name__ == "__main__":
    app.run(debug=True)

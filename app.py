from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def fun():
    return "<h1>hi</h1>"


if __name__==("__main__"):
    app.run(debug=True)

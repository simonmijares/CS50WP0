from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/programming")
def programming():
    return render_template("programming.html")

@app.route("/tech")
def tech():
    return render_template("tech.html")

@app.route("/more")
def more():
    return render_template("more.html")


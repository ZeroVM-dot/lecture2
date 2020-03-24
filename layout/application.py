from flask import Flask, render_template
import jinja2


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page2")
def more():
    return render_template("more.html")

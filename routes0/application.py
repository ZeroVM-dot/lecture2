from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/zero")
def zero():
    return "Hello again!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
#Linha 15 é pra definir que a letra do nome seja maiúscula
    return f"<h1>Hello, {name}!</h1>"

from flask import Flask, render_template, request
from database.db import *

app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html")

@app.route("/register_page")
def regiter_page_func():
    return render_template("register.html")

@app.route("/consult_page")
def consult_page_func():
    return "Vista de consulta"

@app.route("/register_user", methods=["post"])
def register_render_func():
    data = request.form
    id = data["id"]
    nombre = data["nombre"]
    apellido = data["apellido"]
    nacimiento = data["nacimiento"]
    add_user(id,nombre,apellido,nacimiento) 
    return "Usuario agregado"

if __name__ == "__main__":
    host = "172.31.5.89"
    port = "80"
    app.run(host,port, debug=True)
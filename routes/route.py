from server import app
from controllers.control import *

@app.route("/")
def home_func():
    return func_home_func()

@app.route("/register_page")
def regiter_page_func():
    return func_regiter_page_func()

@app.route("/consult_page")
def consult_page_func():
    return  func_consult_page_func()

@app.route("/consult_user", methods=["post"])
def consult_user_func():
    return func_consult_user_func()

@app.route("/register_user", methods=["post"])
def register_render_func():
    return func_register_render_func()
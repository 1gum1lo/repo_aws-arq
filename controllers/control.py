from database.db import *
from flask import Flask, render_template, request, jsonify

def func_home_func():
    return render_template("home.html")


def func_regiter_page_func():
    return render_template("register.html")

def func_consult_page_func():
    return  render_template("consult.html")

def func_consult_user_func():
    id = request.get_json()
    result = consult_user(id)
    obj_response = {
        'nombre': result[0][1],
        'apellido': result[0][2],
        'nacimiento': result[0][3]
    }
    return jsonify (obj_response)

def func_register_render_func():
    data = request.form
    id = data["id"]
    nombre = data["nombre"]
    apellido = data["apellido"]
    nacimiento = data["nacimiento"]
    add_user(id,nombre,apellido,nacimiento) 
    return "Usuario agregado"
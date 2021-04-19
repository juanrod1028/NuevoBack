#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from AdminDao import AdminDao
from models import Persona
import json
import cgi
import os

print('Content-Type: text/json')
print('')

if os.environ['REQUEST_METHOD']=="POST":
    datos= cgi.FieldStorage()
    username =datos.getvalue('nombre')
    password =datos.getvalue('contraseña')
    direccion =datos.getvalue('direc')
    email =datos.getvalue('email')
    permisos ='a'
    identificacion =datos.getvalue('id')

    administrador=Persona(username,password,direccion,email,permisos,identificacion)
    dao=AdminDao()
    if(dao.consultar(username,password) is None):
        if(dao.registrar(administrador)):
            print(json.dumps('{"tipo":"OK","mensaje":"administrador creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear administrador"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un administrador con esa identificación o con ese correo"}'))
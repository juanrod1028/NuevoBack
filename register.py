#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from UsuariosDao import UsuariosDao
from models import Usuario
import json
import cgi
import os

print('Content-Type: text/json')
print('')

if os.environ['REQUEST_METHOD']=="POST":
    datos= cgi.FieldStorage()
    username =datos.getvalue('nombre')
    password =datos.getvalue('contraseña')
    usuario = Usuario(username,password)
    dao=UsuariosDao()
    if(dao.consultar(username,password) is None):
        if(dao.registrar(usuario)):
            print(json.dumps('{"tipo":"OK","mensaje":"Usuario creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear usuario"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un usuario con esa identificación o con ese correo"}'))
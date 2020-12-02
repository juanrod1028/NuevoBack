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
datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="POST":
    username = datos.getvalue('nombre')
    password = datos.getvalue('contraseña')
    dao=UsuariosDao()
    usuario = dao.consultar(username,password)
    if(usuario is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+usuario.username+'"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Usuario o contrasena inválidos"}'))
#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from UsuariosDao import UsuariosDao
from AdminDao import AdminDao
from models import Persona
import json
import cgi
import os
#si
print('Content-Type: text/json')
print('')
datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="POST":
    correo = datos.getvalue('correo')
    password = datos.getvalue('contraseña')
    dao=UsuariosDao()
    admindao = AdminDao()
    usuario = dao.consultar(correo,password)
    admin = admindao.consultar(correo,password)

    if(usuario is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+usuario.username+'"}'))
    elif (admin is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+admin.username+'","administrador":'+json.dumps(admin.__dict__)+'}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Usuario o contrasena inválidos"}'))

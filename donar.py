#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from donarDao import donarDao
from models import Producto
import json
import cgi
import os

print('Content-Type: text/json')
print('')

dao=donarDao()

datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="POST":
    producto = Producto(datos.getvalue('precio'),datos.getvalue('id'),datos.getvalue('nombre'),datos.getvalue('imagen'),datos.getvalue('categoria'))
    if dao.donar(producto):
        print(json.dumps('{"tipo":"OK",mensaje:Producto  creado"}'))
    else:
        print(json.dumps('{"tipo":"error", "mensaje":"error al crear el producto"}'))
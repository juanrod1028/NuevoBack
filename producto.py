#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from ProductosDao import ProductosDao
from models import Producto
import json
import cgi
import os

print('Content-Type: text/json')
print('')

dao=ProductosDao()

datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="POST":
    producto = Producto(datos.getvalue('precio'),datos.getvalue('id'),datos.getvalue('nombre'),datos.getvalue('imagen'),datos.getvalue('categoria'))
    if dao.registrar(producto):
        print(json.dumps('{"tipo":"OK",mensaje:Producto  creado"}'))
    else:
        print(json.dumps('{"tipo":"error", "mensaje":"error al crear el producto"}'))

elif os.environ['REQUEST_METHOD']=="PUT":
    producto = dao.consultar(datos.getvalue('id'))
    if producto is None:
        print(json.dumps('{"tipo":"error", "mensaje":"Ese producto no existe"}'))
    else:
        if datos.getvalue('precio') is not None:
            producto.precioProducto = datos.getvalue('precio')
        if datos.getvalue('id') is not None:
            producto.idProducto = datos.getvalue('id')
        if datos.getvalue('nombre') is not None:
            producto.titleProducto = datos.getvalue('nombre')
        if datos.getvalue('imagen') is not None:
            producto.imagenProducto = datos.getvalue('imagen')
        if datos.getvalue('categoria') is not None:
            producto.categoriaProducto = datos.getvalue('categoria')
        if dao.actualizar(producto):
            print(json.dumps('{"tipo":"OK", "mensaje":"Producto actualizado"}'))
        else:
            print(json.dumps('{"tipo":"error", "mensaje":"error al actualizar el producto"}'))

elif os.environ['REQUEST_METHOD']=="DELETE":
    producto = dao.consultar(datos.getvalue('id'))
    if producto is None:
        print(json.dumps('{"tipo":"error", "mensaje":"Ese producto no existe"}'))
    else:
        if dao.eliminar(producto):
            print(json.dumps('{"tipo":"OK", "mensaje":"Producto eliminado"}'))
        else:
            print(json.dumps('{"tipo":"error", "mensaje":"error al eliminar la categoria"}'))


"""
elif os.environ['REQUEST_METHOD']=="GET":
    idCategoria = datos.getvalue('idCategoria')
    productos=[]
    if idCategoria is None:
        productos = dao.listarTodos()
    else:
        productos = dao.consultarPorCategoria(idCategoria)
    print("[")
    longitud=len(productos)
    i=1
    for producto in productos:
        print(json.dumps(producto.__dict__))
        if i<longitud:
            print(",")
            i=i+1
    print("]") """
    
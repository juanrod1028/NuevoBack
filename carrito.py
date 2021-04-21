import mysql.connector
from mysql.connector import errorcode
from carritoDao import carritoDao
import json


dao=carritoDao()
carrito=dao.carrito()
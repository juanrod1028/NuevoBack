import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Persona
class AdminDao(dao):
  
    def registrar(self,administrador):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql="insert into persona (username, password, direccion, correo, permisos, identificacion) values ('"+administrador.username+"','"+administrador.password+"','"+administrador.direccion+"','"+administrador.correo+"','"+administrador.permisos+"','"+administrador.identificacion+"');"
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def consultar(self,correo,password):
       
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from persona where username ='"+correo+"' and password = '"+password+"' and permisos = 'a';"
            cursor.execute(sql)
            administrador=None
            for row in cursor:
                username=row[0]
                password=row[1]
                direccion=row[2]
                correo=row[3]
                permisos=row[4]
                identificacion=row[5] 
                administrador=Persona(username, password, direccion, correo, permisos, identificacion)
            cursor.close()
            cnx.close()
            return administrador
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

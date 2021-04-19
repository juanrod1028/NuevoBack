import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Persona
class UsuariosDao(dao):
    """
    Clase de objeto de acceso a datos de los usuarios
    """
    def registrar(self,usuario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql="insert into persona (username, password, direccion, correo, permisos, identificacion) values ('"+usuario.username+"','"+usuario.password+"','"+usuario.direccion+"','"+usuario.correo+"','"+usuario.permisos+"','"+usuario.identificacion+"');"
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
            else:
                print(err)
            return False

    def consultar(self,correo,password):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from usuario where correo ='"+correo+"' and password = '"+password+"';"
            cursor.execute(sql)
            usuario=None
            for row in cursor:
                username=row[0]
                password=row[1]
                direccion=row[2]
                correo=row[3]
                permisos=row[4]
                identificacion=row[5] 
                usuario=Persona(username, password, direccion, correo, permisos, identificacion)
            cursor.close()
            cnx.close()
            return usuario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

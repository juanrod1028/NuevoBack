import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Usuario
class UsuariosDao(dao):
    """
    Clase de objeto de acceso a datos de los usuarios
    """
    def registrar(self,usuario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql="insert into usuario (username, password, direccion, correo, identificacion) values ('"+usuario.username+"','"+usuario.password+"','"+usuario.direccion+"','"+usuario.correo+"','"+usuario.identificacion+"');"
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

    def consultar(self,username,password):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from usuario where username ='"+username+"' and password = '"+password+"';"
            cursor.execute(sql)
            usuario=None
            for row in cursor:
                username=row[0]
                password=row[1]
                direccion=row[2]
                correo=row[3]
                identificacion=row[4] 
                usuario=Usuario(username, password, direccion, correo, identificacion)
            cursor.close()
            cnx.close()
            return usuario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

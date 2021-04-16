import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Administrador
class AdminDao(dao):
  
    def registrar(self,administrador):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[administrador.username,administrador.password,administrador.direccion,administrador.correo,administrador.identificacion,administrador.permisos]
            cursor.callproc("crearAdministrador",args)
            for permiso in administrador.permisos:
                sql = "insert into ADMINISTRADOR_has_PERMISO (ADMINISTRADOR_PERSONA_idPERSONA,PERMISO_idPERMISO)  values (%s,%s);"
                cursor.execute(sql,(administrador.identificacion,permiso))
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

    def consultar(self,username,password):
       
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from administrador where username ='"+username+"' and password = '"+password+"';"
            cursor.execute(sql)
            administrador=None
            for row in cursor:
                username=row[0]
                password=row[1]
                direccion=row[2]
                correo=row[3]
                identificacion=row[4]
                administrador=Administrador(username,password,direccion,correo,identificacion,None)
            sql2= "select p.nombrePermiso from permiso as p inner join ADMINISTRADOR_has_PERMISO as ap on p.idPERMISO=ap.PERMISO_idPERMISO inner join administrador as a on ap.ADMINISTRADOR_PERSONA_idPERSONA=a.PERSONA_idPERSONA where a.PERSONA_idPERSONA='"+administrador.identificacion+"'"
            cursor.execute(sql2)
            permisos = []
            for row in cursor:
                permisos.append(row[0])
            administrador.permisos=permisos
            cursor.close()
            cnx.close()
            return administrador
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

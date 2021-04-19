import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Producto


class ProductosDao(dao):
    
    def registrar(self,producto):
        
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "insert into producto (precio,id,title,thumbnailUrl,categoria)  values (%s,%s,%s,%s,%s);"
            cursor.execute(sql,(producto.precioProducto,producto.idProducto,producto.titleProducto,producto.imagenProducto,producto.categoriaProducto))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with agregar")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False
    
    def consultar(self,idProducto):
        
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from producto where id="+str(idProducto)+";"
            cursor.execute(sql)
            producto=None
            for row in cursor:
                producto = Producto(row[0],row[2],row[3],row[4],row[5])
                producto.idProducto=row[1]
            cursor.close()
            cnx.close()
            return producto
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with consultar")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None


    def eliminar(self,producto):
        
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "delete from producto where id="+str(producto.idProducto)+"; "
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with eliminar")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return False

    def actualizar(self,producto):
        
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "update producto set precio=%s, id=%s, title =%s, thumbnailUrl=%s, categoria=%s where id=%s;"
            cursor.execute(sql,(producto.precioProducto,producto.idProducto,producto.titleProducto,producto.imagenProducto,producto.categoriaProducto))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with actualizar")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return False
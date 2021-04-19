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
            cursor.execute(sql,(producto.precioProducto,producto.idProducto,producto.nombreProducto,producto.imagenProducto,producto.categoriaProducto))
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
            sql = "select * from producto where idProducto="+str(idProducto)+";"
            cursor.execute(sql)
            producto=None
            for row in cursor:
                producto = Producto(row[0],row[1],row[2],row[3],row[4])
                producto.idProducto=row[0]
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
            sql = "delete from producto where idProducto="+str(producto.idProducto)+"; "
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
            sql = "update producto set idProducto=%s,nombreProducto=%s, imagenProducto =%s, precioProducto=%s where idProducto = %s;"
            cursor.execute(sql,(producto.idCategoria,producto.nombre,producto.imagen,producto.precio,producto.idProducto))
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
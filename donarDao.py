import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Producto


class donarDao(dao):
    
    def donar(self,producto):
        
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
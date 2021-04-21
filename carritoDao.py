import mysql.connector
import json
from dao import dao

class carritoDao(dao):

    def carrito(self):
        
        cnx = super().connectDB()
        cursor = cnx.cursor()
        universidad = []
        universidad2 = []
        cursor.execute("select *  from Productos group by categoria;")
        resultF = cursor.fetchall()
        cursor.execute("SELECT  categoria,count(*) as cantidad FROM Productos group by categoria order by categoria;")
        resultF2 = cursor.fetchall()
        for rowF in resultF:    
            universidad.append({'precio' : rowF[0], 'id' : rowF[1], 'title' : rowF[2], 'thumbnailUrl' : rowF[3],'categoria':rowF[4]})

        for rowF2 in resultF2:    
            universidad2.append({ 'categoria' : rowF2[0], 'cantidad' : rowF2[1]})

        json.dumps(universidad)


        with open('Front - copiadatos.json', 'w+') as outfile:
            json.dump(universidad, outfile)
        with open('datoscantidad.json', 'w+') as outfile:
            json.dump(universidad2, outfile)
        cnx.close()

        return True




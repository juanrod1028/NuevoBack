import mysql.connector
from mysql.connector import errorcode
class dao:
    
    def __init__(self):
        self.user='trolmico'
        self.password='nicolas26'
        self.database='ortopedicos'
        self.host='127.0.0.1'
    def connectDB(self):
        cnx = mysql.connector.connect(user=self.user, password = self.password, database=self.database, host=self.host)
        return cnx
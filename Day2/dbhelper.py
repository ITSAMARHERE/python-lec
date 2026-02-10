import mysql.connector 

class DBhelper:

    def __init__self(self):
       self.conn =  mysql.connector.connect(host = "localhost", user="root", password = "", database = "hit-db-demp")
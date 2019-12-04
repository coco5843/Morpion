import mysql.connector
from mysql.connector import Error


class Mysql:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (self.connection.is_connected()):
                cursor.close()
                self.close(self.connection)


        def close(self):
            if self.connection.is_connected():
                self.connection.close()
                print("MySQL connection is closed")

        def setup(self):
            pass
            
from DataLayer.DataBase.DBManager import DBManager
from DataLayer.Models.User import User

class Transactions:

    def findUserByEmail(self, email):
        exist = False
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'SELECT email FROM User WHERE email = %s'
        cursor.execute(query, (email,))
        userByEmail = cursor.fetchone()
        if userByEmail:
            exist = True
        return exist
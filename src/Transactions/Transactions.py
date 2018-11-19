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
    
    def saveWrongWordOfUser(self, userId, wWordId):
        rel = False
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'INSERT INTO User_has_WrongWord VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE quantity = quantity + 1'
        response = cursor.execute(query, (userId, wWordId, 1))
        print(response)
        if response:
            conn.connection.commit()
            rel = True
        return rel

    def findUserErrors(self, user):
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'SELECT WrongWord.id, label FROM User INNER JOIN User_has_WrongWord ON User.id = User_id INNER JOIN WrongWord ON WrongWord_id = WrongWord.id WHERE User.id = %s'
        cursor.execute(query, (user['id']))
        errors = cursor.fetchall()
        user['wrongWords'] = errors
        return user


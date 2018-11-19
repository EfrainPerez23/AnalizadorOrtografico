from DataLayer.DataAccessObject.Dependencies.DAO import DAO
from DataLayer.Models.User import User
from DataLayer.DataBase.DBManager import DBManager

class MYSQL_UserDAO(DAO):

    def create(self, user):
        
        if user.isValid():
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'INSERT INTO User VALUES (%s, %s, %s, %s, %s)'
            response = cursor.execute(query, (None, user.firstName, user.lastName, user.age, user.email))
            if response:
                conn.connection.commit()
                return user

        return None

    def delete(self, _id):
        deleted = False
        if _id:
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'DELETE FROM User WHERE id = %s'
            response = cursor.execute(query, (_id,))
            if response:
                conn.connection.commit()
                deleted =  True
        return deleted


    def read(self, _id):
        user = None
        if _id:
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'SELECT id, name, lastName, email, age FROM User WHERE id = %s'
            cursor.execute(query, (_id,))
            firstUser = cursor.fetchone()
            if firstUser:
                user = User(firstUser['id'], firstUser['name'], firstUser['lastName'], firstUser['email'], firstUser['age'], None)
            
        return user

    def readAll(self):
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'SELECT id, name, lastName, email, age FROM User'
        cursor.execute(query)
        users = cursor.fetchall()
        if users:
            return [
                User(user['id'], user['name'], user['lastName'], user['email'], user['age'], None).json()
                for user in users
            ]
            
        return []

    def update(self, user):
        if user and user.isValid():
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'UPDATE User SET name = %s, lastName = %s, age= %s, email = %s WHERE id = %s'
            response = cursor.execute(query,
                                      (user.firstName, user.lastName, user.age, user.email, user.id,))
            if response:
                conn.connection.commit()
                return user
        return None

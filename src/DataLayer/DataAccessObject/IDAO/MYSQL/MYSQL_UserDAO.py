from DataLayer.DataAccessObject.Dependencies.DAO import DAO

class MYSQL_UserDAO(DAO):

    def create(self, user):
        from DataLayer.DataBase.DBManager import DBManager
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
        pass

    def read(self, _id):
        pass

    def readALL(self):
        pass

    def update(self, user):
        pass

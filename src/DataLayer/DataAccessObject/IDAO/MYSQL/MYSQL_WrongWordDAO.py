from DataLayer.DataAccessObject.Dependencies.DAO import DAO
from DataLayer.Models.WrongWord import WrongWord
from DataLayer.DataBase.DBManager import DBManager


class MYSQL_WrongWordDAO(DAO):
    def create(self, wrongWord):
        if wrongWord.isValid():
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'INSERT INTO WrongWord VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE quantity = quantity + 1'
            response = cursor.execute(
                query, (None, wrongWord.label, wrongWord.quantity))
            if response:
                wrongWord.id = conn.connection.insert_id()
                conn.connection.commit()
                return wrongWord

        return None

    def delete(self, _id):
        deleted = False
        if _id:
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'DELETE FROM WrongWord WHERE id = %s'
            response = cursor.execute(query, (_id,))
            if response:
                conn.connection.commit()
                deleted = True
        return deleted

    def read(self, _id):
        wWord = None
        if _id:
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'SELECT id, label, quantity FROM WrongWord WHERE id = %s'
            cursor.execute(query, (_id,))
            firstWrongWord = cursor.fetchone()
            if firstWrongWord:
                wWord = WrongWord(
                    firstWrongWord['id'], firstWrongWord['label'], firstWrongWord['quantity'], None)

        return wWord

    def readAll(self):
        conn = DBManager()
        cursor = conn.connection.cursor()
        query = 'SELECT id, label, quantity FROM WrongWord'
        cursor.execute(query)
        WrongWords = cursor.fetchall()
        if WrongWords:
            return [
                WrongWord(wrongWord['id'],wrongWord['label'],
                          wrongWord['quantity'], None).json()
                for wrongWord in WrongWords
            ]

        return []

    def update(self, wrongWord):
        if wrongWord and wrongWord.isValid():
            conn = DBManager()
            cursor = conn.connection.cursor()
            query = 'UPDATE WrongWord SET label = %s, quantity = %s WHERE id = %s'
            response = cursor.execute(
                query, (wrongWord.label, wrongWord.quantity, wrongWord.id,))
            print(response)
            if response:
                conn.connection.commit()
                return wrongWord
        return None

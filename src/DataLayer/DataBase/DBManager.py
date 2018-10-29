import app as app
import pymysql

database_name = app.app.config.get('DATABASE_NAME')
database_host = app.app.config.get('DATABASE_HOST')
database_port = app.app.config.get('DATABASE_PORT')
database_username = app.app.config.get('DATABASE_USERNAME')
database_password = app.app.config.get('DATABASE_PASSWORD')


class DBManager(object):

    def __init__(self):
        self.connection = pymysql.connect(host=database_host,
                                          user=database_username,
                                          password=database_password,
                                          db=database_name,
                                          port=database_port,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
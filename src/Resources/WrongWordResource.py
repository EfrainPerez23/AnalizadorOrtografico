from Util.BodyParser import BodyParser
from flask_restful import Resource, reqparse
from DataLayer.DataAccessObject.IDAO.MYSQL.MYSQL_WrongWordDAO import MYSQL_WrongWordDAO
from DataLayer.Models.WrongWord import WrongWord

class WrongWordResource(Resource):

    def get(self, id=None):
        wrongWordDAO = MYSQL_WrongWordDAO()
        message = 'WrongWord does not exist'
        status = 400
        data = None
        if id:
            if id.isdigit():
                wrongWord = wrongWordDAO.read(id)

                if wrongWord:
                    message = 'WrongWord exists'
                    status = 200
                    data = wrongWord.json()
            else:
                message = 'Not allowed'
                status = 405

        else:
            wrongWords = wrongWordDAO.readAll()
            message = 'WrongWords do not exist'
            data = wrongWords
            if len(wrongWords) > 0:
                message = 'WrongWords exist'
                status = 200
        return {
                   'message': message,
                   'data': data
               }, status

    def post(id = None):
        
        _help = 'This field cannot be blank!'
        data = BodyParser.bodyParser([
            {
                'key': 'label',
                '_type': str,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'quantity',
                '_type': str,
                '_required': True,
                '_help': _help
            }
        ])

        wWord = WrongWord(None, data['label'], data['quantity'], None  )
        status = 400
        message = 'WrongWord not created'


        wrongWordDAO = MYSQL_WrongWordDAO()
        if wrongWordDAO.create(wWord):
            message = 'WrongWord created'
            status = 201

        return {'message': message, 'data': data}, status


    def put(self, id=None):
        _help = 'This field cannot be blank!'
        data = BodyParser.bodyParser([
            {
                'key': 'id',
                '_type': int,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'label',
                '_type': str,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'quantity',
                '_type': int,
                '_required': True,
                '_help': _help
            }

        ])
        wWordToUpdate = WrongWord(data['id'], data['label'], data['quantity'], None)
        wrongWordDAO = MYSQL_WrongWordDAO()
        status = 400
        if wrongWordDAO.update(wWordToUpdate):
            message = 'WrongWord updated'
            status = 201
        else:
            message = 'Not allowed'
            status = 405
        return {'message': message, 'data': data}, status

    def delete(self, id):
        message = 'Wrong word does not exist to delete it'
        status = 400
        if id.isdigit():
            wrongWordDAO = MYSQL_WrongWordDAO()
            if wrongWordDAO.delete(id):
                message = 'Wrong word deleted successfully'
                status = 202
        else:
            message = 'Not allowed'
            status = 405
        return {'message': message, 'data': {
            'id': id
        }}, status


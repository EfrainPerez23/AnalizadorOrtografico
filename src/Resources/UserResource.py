from Util.BodyParser import BodyParser
from flask_restful import Resource, reqparse
from DataLayer.DataAccessObject.IDAO.MYSQL.MYSQL_UserDAO import MYSQL_UserDAO
from DataLayer.Models.User import User
from Transactions.Transactions import Transactions


class UserResource(Resource):

    def get(self, id=None):
        userDAO = MYSQL_UserDAO()
        message = 'User does not exist'
        status = 400
        data = None
        if id:
            if id.isdigit():
                user = userDAO.read(id)

                if user:
                    message = 'User exists'
                    status = 200
                    transaction = Transactions()
                    data = user.json()
                    data = transaction.findUserErrors(data)
            else:
                message = 'Not allowed'
                status = 405

        else:
            users = userDAO.readAll()
            message = 'Users do not exist'
            data = users
            if len(users) > 0:
                message = 'Users exist'
                status = 200
                transaction =  Transactions()
                for _data in data:
                    _data = transaction.findUserErrors(_data)
        return {
                   'message': message,
                   'data': data
               }, status


    def post(id = None):
        
        _help = 'This field cannot be blank!'
        data = BodyParser.bodyParser([
            {
                'key': 'firstName',
                '_type': str,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'lastName',
                '_type': str,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'age',
                '_type': int,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'email',
                '_type': str,
                '_required': True,
                '_help': _help
            }

        ])

        newUser = User(None, data['firstName'], data['lastName'], data['email'], data['age'], None  )

        transaction = Transactions()
        userVerification = transaction.findUserByEmail(newUser.email)
        status = 400
        message = 'User not created'

        if userVerification:
            message = 'User already exists with that email'
            return {'message': message, 'data': newUser.json() }, status

        userDAO = MYSQL_UserDAO()
        userCreated = userDAO.create(newUser)
        if userCreated:
            message = 'User created'
            status = 201

        return {'message': message, 'data': userCreated.json()}, status

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
                'key': 'firstName',
                '_type': str,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'lastName',
                '_type': str,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'age',
                '_type': int,
                '_required': True,
                '_help': _help
            },
            {
                'key': 'email',
                '_type': str,
                '_required': True,
                '_help': _help
            }

        ])
        userToUpdate = User(data['id'], data['firstName'], data['lastName'], data['email'], data['age'], None)
        userDAO = MYSQL_UserDAO()
        status = 400
        if userDAO.update(userToUpdate):
            message = 'User updated'
            status = 201
        else:
            message = 'Not allowed'
            status = 405
        return {'message': message, 'data': data}, status
    
    def delete(self, id):
        message = 'User does not exist to delete it'
        status = 400
        if id.isdigit():
            userDAO = MYSQL_UserDAO()
            if userDAO.delete(id):
                message = 'User deleted successfully'
                status = 202
        else:
            message = 'Not allowed'
            status = 405
        return {'message': message, 'data': {
            'id': id
        }}, status

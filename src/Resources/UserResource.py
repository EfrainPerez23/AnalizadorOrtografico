from Util.BodyParser import BodyParser
from flask_restful import Resource, reqparse
from DataLayer.DataAccessObject.IDAO.MYSQL.MYSQL_UserDAO import MYSQL_UserDAO



class UserResource(Resource):

    def post(id = None):
        from DataLayer.Models.User import User
        from Transactions.Transactions import Transactions
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

        newUser = User(None, data['firstName'], data['lastName'], data['age'], data['email'], None  )

        transaction = Transactions()
        userVerification = transaction.findUserByEmail(newUser.email)
        status = 400
        message = 'User not created'

        if userVerification:
            message = 'User already exists with that email'
            return {'message': message, 'data': newUser.json() }, status

        userDAO = MYSQL_UserDAO()
        if userDAO.create(newUser):
            message = 'User created'
            status = 201

        return {'message': message, 'data': data}, status

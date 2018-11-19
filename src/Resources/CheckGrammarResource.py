from Util.BodyParser import BodyParser
from flask_restful import Resource, reqparse
from DataLayer.Models.Grammar import Grammar
from Grammar.CheckGrammar import CheckGrammar
from DataLayer.DataAccessObject.IDAO.MYSQL.MYSQL_WrongWordDAO import MYSQL_WrongWordDAO
from DataLayer.Models.WrongWord import WrongWord


class CheckGrammarResource(Resource):

    def post(self):
        data = BodyParser.bodyParser([
            {
                'key': 'paragraph',
                '_type': str,
                '_required': True,
                '_help': 'Paragraph cannot be blank!'
            },
        ])

        matches = CheckGrammar().checkGrammar(data['paragraph'])
        if (matches):
            wrongWordDAO = MYSQL_WrongWordDAO()
            for match in matches:
                wrongWordDAO.create(WrongWord(None, match['wrongWord'], 1, None))
            return {'data': matches}

        return {'data': matches}




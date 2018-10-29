from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, timedelta



# Resources
from Resources.CheckGrammarResource import CheckGrammarResource

app = Flask(__name__)

# Load config File
app.config.from_pyfile('config.cfg')
app.secret_key = app.config.get('SECRET_KEY')

# Init Rest API endpoints
api = Api(app)
api.add_resource(CheckGrammarResource, '/check-grammar')

if __name__ == '__main__':
    app.run()
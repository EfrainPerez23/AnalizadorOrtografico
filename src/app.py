from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, timedelta
from flask_cors import CORS



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load config File
app.config.from_pyfile('config.cfg')
app.secret_key = app.config.get('SECRET_KEY')

# Init Rest API endpoints
api = Api(app)


if __name__ == '__main__':

    # Resources
    from Resources.CheckGrammarResource import CheckGrammarResource
    from Resources.UserResource import UserResource
    api.add_resource(CheckGrammarResource, '/check-grammar')
    api.add_resource(UserResource, '/user', '/user/<id>', endpoint='user')
    api.add_resource(UserResource, '/wrong-word', '/wrong-word/<id>', endpoint='wrong-word')
    app.run()
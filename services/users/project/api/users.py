from flask import Blueprint
from flask_restful import Resource, Api

from project import db

from project.api.models import User

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)


class UsersList(Resource):
    def post(self):
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': f'{email} was added!'
        }
        return response_object, 201 


class UsersPing(Resource):
    def get(self):
        return {
            'status':  200,
            'message': "PONG"
        }


api.add_resource(UsersPing, '/users/ping')
api.add_resource(UsersList, '/users')
from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal_with

from apps.models.user_model import Users

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

types_fields = {
    'id': fields.Integer,
    'username': fields.String
}


class Home(Resource):
    @marshal_with(types_fields)
    def get(self):
        users = Users.query.all()
        return users


api.add_resource(Home, '/home')
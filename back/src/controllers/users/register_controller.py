from flask import make_response, jsonify
from flask.views import MethodView
from src.models.user_model import Users
from src.utils.db_util import db

class RegisterUserController(MethodView):
    
    def __init__(self):
        pass

    def get(self):
        return "ok" 
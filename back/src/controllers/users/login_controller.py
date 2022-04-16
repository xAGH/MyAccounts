from flask import make_response, jsonify
from flask.views import MethodView
from src.models.user_model import Users

class LoginUserController(MethodView):
    
    def __init__(self):
        pass

    def get(self):
        return "ok" 
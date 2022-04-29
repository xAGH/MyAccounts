from src.validators.user_validator import CreateUserRegisterSchema
from src.validators.user_validator import CreateUserLoginSchema
from src.services.user_service import UserService
from flask import make_response, jsonify, request
from src.hooks.input_validator import json_input
from src.utils.functions import validate_input
from flask.views import MethodView

class RegisterUserController(MethodView):
    
    def __init__(self):
        self.validator = CreateUserRegisterSchema()
        self.service = UserService()

    @json_input
    def post(self):

        content, valid = validate_input(self, request.get_json())
        
        if valid:
            response, status = self.service.register(content)
            return make_response(jsonify(response), status)

        return make_response(jsonify(content[0]), content[1])

class LoginUserController(MethodView):

    def __init__(self):
        self.validator = CreateUserLoginSchema()
        self.service = UserService()

    @json_input
    def post(self):

        content, valid = validate_input(self, request.get_json())
        
        if valid:
            response, status = self.service.login(content)
            return make_response(jsonify(response), status)

        return make_response(jsonify(content[0]), content[1])

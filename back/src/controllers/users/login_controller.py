from flask import make_response, jsonify, request
from flask.views import MethodView
from src.models.user_model import Users
from src.validators.login_user_validator import CreateUserLoginSchema
from bcrypt import checkpw
import jwt
from src.config import KEYS

class LoginUserController(MethodView):

    def __init__(self):
        self.validator = CreateUserLoginSchema()

    def post(self):

        if not request.is_json:
            return make_response(jsonify({
                "status": 400,
                "response": "Send a json format."
            }), 400)

        content = request.get_json()
        errors = self.validator.validate(content)

        if errors:
            return make_response(jsonify({
                "status": 400,
                "response": errors
            }), 400)

        user = Users.query.filter_by(correo=content.get("correo")).first()

        if user is None:
            return make_response(jsonify({
                "status": 422,
                "response": "The user doesn't exists."
            }), 422)

        db_pass = bytes(user.password, 'utf8')
        pass_bytes = bytes(content.get("password"), 'utf8')

        if not checkpw(pass_bytes, db_pass):
            return make_response(jsonify({
                "status": 406,
                "response": "Password is incorrect."
            }), 406)

        token = jwt.encode(
                {
                    "email": user.email,
                    "document": user.document
                }, KEYS.JWT, "HS256")
        
        token = bytes.decode(token, 'utf8')

        return make_response(jsonify({
            "status": 200,
            "response": "Login successfully.",
            "token": f"{token}"
        }), 200)

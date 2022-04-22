from flask import make_response, jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from src.models.user_model import Users
from src.utils.db_util import db
from src.validators.register_user_validator import CreateUserRegisterSchema
from bcrypt import gensalt, hashpw

class RegisterUserController(MethodView):
    
    def __init__(self):
        self.validator = CreateUserRegisterSchema()

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

        try:
            print(content.get("savings"))
            db.session.add(
                Users(
                    document = content.get("document"),
                    name = content.get("name"),
                    email = content.get("email"),
                    password = bytes.decode(hashpw(bytes(content.get("password"), 'utf-8'), gensalt()), 'utf-8'),
                    cash_balance = content.get("cash_balance"),
                    card_balance = content.get("card_balance"),
                    savings = content.get("savings")
                )
            )
            db.session.commit()

            return make_response(jsonify({
                "status": 201,
                "response": "User created successfully."
            }), 201)

        except IntegrityError:
            db.session.rollback()
            return make_response(jsonify({
                "status": 409,
                "response": "The user alredy exists."
            }), 409)
        
        except:
            db.session.rollback()
            raise

        finally:
            db.session.close()


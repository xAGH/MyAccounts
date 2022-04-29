from src.models.user_model import Users
from src.utils.functions import time
from src.utils.instances import db
from src.config import KEYS
from bcrypt import checkpw, hashpw, gensalt
import jwt
from sqlalchemy.exc import IntegrityError

class UserService():

    def login(self, data):
        user: Users = Users.query.filter_by(email=data.get("email")).first()

        if user is None:
            return (
                {
                    "response": "The user doesn't exists.",
                }, 
                422
            )

        try:
            user.last_login = time()
            db.session.commit()

        except Exception as e:
            return (
                {
                    "response": "Error in server.",
                    "error": str(e)
                },
                500
            )

        db_pass = bytes(user.password, 'utf8')
        pass_bytes = bytes(data.get("password"), 'utf8')

        if not checkpw(pass_bytes, db_pass):
            return (
                {
                    "response": "Password is incorrect."
                },
                406
            )

        token = jwt.encode(
                {
                    "email": user.email,
                    "document": user.document
                }, KEYS.JWT, "HS256")
        
        token = bytes.decode(token, 'utf8')

        return (
            {
                "response": "Login successfully.",
                "token": f"{token}"
            },
            200
        )

    def register(self, data):
        try:
            db.session.add(
                Users(
                    document = data.get("document"),
                    name = data.get("name"),
                    email = data.get("email"),
                    password = bytes.decode(hashpw(bytes(data.get("password"), 'utf-8'), gensalt()), 'utf-8'),
                    cash_balance = data.get("cash_balance"),
                    card_balance = data.get("card_balance"),
                    savings = data.get("savings")
                )
            )
            db.session.commit()

            return (
                {
                    "response": "User created successfully."
                },
                201
            )

        except IntegrityError:
            db.session.rollback()
            return (
                {
                    "response": "The user alredy exists."
                },
                409
            )
        
        except Exception as e:
            db.session.rollback()
            return (
                {
                    "response": f"Error in server: {e}."
                },
                500
            )


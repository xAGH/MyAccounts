from flask import Flask
from flask import make_response, jsonify
from flask_cors import CORS
from src.routes import users
from src.config import DB, APP

class Aplication:
    @classmethod
    def create_app(cls):
        cls.app = Flask(__name__)
        cls.__configure()
        return cls.app

    @classmethod
    def __configure(cls):
        try:
            # Database configuration
            cls.app.config["SQLALCHEMY_DATABASE_URI"] = f'{DB.ENGINE}+{DB.DRIVER}://{DB.USER}:{DB.PASS}@{DB.HOST}:{DB.PORT}/{DB.NAME}'
            cls.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

            # CORS configuration
            CORS(cls.app, resources={
               r"/*": {
                   "origins": [APP.CORS, "*"]
               }
            }, supports_credentials=True)

            # Register routes
            cls.__register_routes()

        except Exception as e:
            return make_response(jsonify({
                "response": "Error starting server",
                "error": str(e)
            }), 500)

    @classmethod
    def __register_routes(cls):
        cls.app.add_url_rule(users["index"], view_func=users["index_controller"])
    

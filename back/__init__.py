from flask import Flask
from flask_cors import CORS
from src.routes import users
from src.config import DB, APP

class Application():

    @classmethod
    def create_app(cls):
        # Instance of Flask
        cls.app = Flask(__name__)
        cls.__configure()
        return cls.app

    @classmethod
    def __configure(cls):
        # Database configuration
        cls.app.config["SQLALCHEMY_DATABASE_URI"] = f'{DB.ENGINE}+{DB.DRIVER}://{DB.USER}:{DB.PASS}@{DB.HOST}:{DB.PORT}/{DB.NAME}'
        cls.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        # Run config
        cls.app.config["RUN_CONFIG"] = dict(host=APP.HOST, port=APP.PORT, debug=APP.DEBUG)

        # CORS configuration
        CORS(cls.app, resources={
            r"/*": {
                "origins": [APP.CORS, "*"]
            }
        }, supports_credentials=True)
        
        # Register routes
        cls.__register_routes()
    
    @classmethod
    def __register_routes(cls):
        # Users
        cls.app.add_url_rule(users["login"], view_func=users["login_controller"])
        cls.app.add_url_rule(users["register"], view_func=users["register_controller"])

from os import getenv
from dotenv import load_dotenv
load_dotenv()
class DB():
    ENGINE = getenv("DB_ENGINE", "mysql")
    DRIVER = getenv("DB_DRIVER", "pymsql")
    HOST = getenv("DB_HOST", "localhost")
    USER = getenv("DB_USER",'root')
    PASS = getenv("DB_PASS", '')
    NAME = getenv("DB_NAME", 'database')
    PORT = int(getenv("DB_PORT", 3306))

class APP():
    HOST = getenv("APP_HOST", "localhost")
    PORT = int(getenv("APP_PORT", 3000))
    DEBUG = bool(getenv("APP_DEBUG", True))
    CORS = getenv("CORS_ORIGIN", "localhost:4200")
    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

class KEYS():
    JWT = getenv("JWT_KEY")

from dataclasses import dataclass


@dataclass(frozen=True)
class RevolverConfig:
    DEF_NAME: str = "Colt .44"
    DEF_DESCR: str = "Стандартный револьвер системы Colt. Классика дикого запада."
    DEF_DRUM_CAPACITY: int = 6
    DEF_DRUM_TURN_PERIOD: float = 0.5  # seconds
    DEF_BULLETS_COUNT: int = 1
    MIN_DRUM_CAPACITY: int = 4
    MAX_DRUM_CAPACITY: int = 8


@dataclass(frozen=True)
class WebAppConfig:

    IP = "0.0.0.0"
    PORT = 80
    SECRET_KEY = 'secret_key'
    SECURITY_PASSWORD_SALT = 'very_salt_pw'
    TEMPLATE_FOLDER = 'web/templates'
    STATIC_FOLDER = 'web/static'

    MONGODB_SETTINGS = {
        'db': 'database',
        'host': 'mongo',
        'port': 27017
    }

    # Mongo
    MONGO_CONNECT_URL = "mongodb://mongo:27017/database"

    # Logs
    LOGGING_LEVEL = "DEBUG"
    STATUS_HOURS = 1
    STATUS_ADMIN_DAYS = 7
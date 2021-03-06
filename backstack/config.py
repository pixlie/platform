import sys
from decouple import config

from .singleton import Singleton
from . import constants


class Settings(metaclass=Singleton):
    _instance = None

    def __init__(self):
        config.search_path = sys.path[0]

        # Statement for enabling development environment.
        # Keep PRODUCTION = True for production environment
        self.RUNNING_AS = config("RUNNING_AS", cast=str, default=constants.RUNNING_DEVELOPMENT)

        # Python path to the User model class (SQLAlchemy model)
        # This is not read from settings.ini, instead set this in your main.py like
        #  `settings.USER_MODEL = "apps.account.models.User"`
        self.USER_MODEL = config("USER_MODEL", cast=str, default=None)

        # Datebase configurations
        self.DB_DEFAULT = config("DB_DEFAULT", cast=str, default=None)
        self.DB_TEST = config("DB_TEST", cast=str, default=None)

        # Database migrations using SQLAlchemy-migrate
        self.DB_MIGRATIONS_FOLDER = config("DB_MIGRATIONS_FOLDER", cast=str, default="db-migrations")

        # Settings for running the server on localhost with port number
        self.DAEMON = {
            "host": config("DAEMON_HOST", cast=str, default="127.0.0.1"),
            "port": config("DAEMON_PORT", cast=int, default=4000),
        }

        self.SERVER_PROTOCOL = config("SERVER_PROTOCOL", cast=str, default="http")
        self.SERVER_DOMAIN = config("SERVER_DOMAIN", cast=str, default="localhost:4000")

        self.WEBSITE_PROTOCOL = config("WEBSITE_PROTOCOL", cast=str, default="http")
        self.WEBSITE_DOMAIN = config("WEBSITE_DOMAIN", cast=str, default="localhost:3000")

        self.SECRET_KEY = config("SECRET_KEY", cast=str)

        self.RABBITMQ_HOST = config("RABBITMQ_HOST", cast=str, default="localhost")
        self.RABBITMQ_PORT = config("RABBITMQ_PORT", cast=int, default=5672)
        self.RABBITMQ_EXCHANGE = config("RABBITMQ_EXCHANGE", cast=str, default="mq-exchange")

        self.MEMCACHED_HOST = config("MEMCACHED_HOST", cast=str, default="localhost")

        self.APPS = ()

        self.FILE_UPLOAD_PATH = config("FILE_UPLOAD_PATH", cast=str, default="/tmp/")
        self.S3_BUCKET = config("S3_BUCKET", cast=str, default=None)
        self.S3_ENDPOINT_URL = config("S3_ENDPOINT_URL", cast=str, default=None)

        self.SESSION_COOKIE_NAME = config("SESSION_COOKIE_NAME", cast=str, default=None)

        self.ALLOWED_ORIGINS = config(
            "ALLOWED_ORIGINS",
            cast=lambda v: [s.strip() for s in v.split(',')],
            default="http://localhost:3000,"
        )

    def get_mq_exchange_name(self):
        return "{}.{}".format(self.RABBITMQ_EXCHANGE, "topic")


settings = Settings()

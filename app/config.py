import os
from dotenv import load_dotenv, find_dotenv
import redis 

load_dotenv(find_dotenv())

class Config:
    FLASK_APP = 'trivia_time.py'
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Session
    REDIS_URI = os.environ.get('SESSION_REDIS')
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url(REDIS_URI)
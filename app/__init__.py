from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.users.routes import users
    from app.quiz.routes import quiz
    from app.home.routes import home
    app.register_blueprint(users)
    app.register_blueprint(quiz)
    app.register_blueprint(home)

    return app

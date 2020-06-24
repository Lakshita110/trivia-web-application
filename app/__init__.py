from flask import Flask, session, render_template, flash, redirect, url_for, request
from flask_session import Session
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login = LoginManager()
sess = Session()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        from . import auth
        db.create_all()  # Create sql tables for our data models

        return app
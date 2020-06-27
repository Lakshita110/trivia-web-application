from flask import render_template, request, Blueprint
from flask_login import current_user, login_user, logout_user, login_required

home = Blueprint('home', __name__)

@home.route("/")
@home.route("/home")
@login_required
def home():
    render_template('')
from flask import render_template, request, Blueprint
from flask_login import current_user, login_user, logout_user, login_required

quiz = Blueprint('quiz', __name__)
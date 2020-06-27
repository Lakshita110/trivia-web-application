from flask import render_template, flash, redirect, url_for, request, jsonify, json, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse 
from sqlalchemy.sql import func
from statistics import mean 
from .forms import LoginForm, RegisterForm
from .models import User
from app import db

main = Blueprint('main', __name__)

# Homepage route from where user can search.
@main.route("/home")
@main.route("/", methods=['GET','POST'])
# @login_required
def index():
    return render_template('home.html', title='Home')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You're already logged in.")
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        flash('Congratulations, you are logged in!')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form = form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("You're already logged in.")
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are registered!')
        return redirect(url_for('main.login'))
    return render_template('register.html',title='Register', form=form)
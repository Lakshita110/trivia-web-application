from flask import render_template, flash, redirect, url_for, request, jsonify, json
import json
from . import db, forms, models
from .forms import *
from .models import *
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse 
# from sqlalchemy.sql import func
# from statistics import mean 
#------------------------------------------------------------------------

# Homepage route from where user can search.
@app.route("/index")
@app.route("/", methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html', title='Home', form=form)

# Login route which verifies a user's existance with the database. 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You're already logged in.")
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Congratulations, you are logged in!')
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Log In', form = form)

# Registration route which adds a user to the database after all fields have been verified.
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("You're already logged in.")
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are registered!')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register', form=form) 

# Logout route to logout the user and display a logged out message.
@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Sucessfully logged out!")
        return redirect(url_for('index'))
    else:
        flash("You're not logged in")
        return redirect(url_for('login'))
    

# 404 error handler. 
@app.errorhandler(404)   
def not_found(e):
    return render_template('error.html', message="Page was not found. Sorry!")    


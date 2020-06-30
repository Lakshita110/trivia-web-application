import html
import random
from statistics import mean
import requests
from flask import (Blueprint, flash, json, jsonify, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy.sql import func
from werkzeug.urls import url_parse
from app import db
from .forms import GenerateQuizForm, LoginForm, RegisterForm
from .models import User
from flask import session

main = Blueprint('main', __name__)

# Homepage route from where user can search.
@main.route("/home")
@main.route("/", methods=['GET','POST'])
@login_required
def index():
    form = GenerateQuizForm()
    if form.validate_on_submit():            
        amount = form.amount.data
        category = form.category.data
        difficulty = form.difficulty.data
        if category== 0 and difficulty=='any':
            res_api = requests.get("https://opentdb.com/api.php?type=multiple",params={"amount": amount}) 
        elif category==0:
            res_api = requests.get("https://opentdb.com/api.php?type=multiple",params={"amount": amount, "difficulty": difficulty})
        elif difficulty=='any':
            res_api = requests.get("https://opentdb.com/api.php?type=multiple",params={"amount": amount, "category":category})
        else:
            res_api = requests.get("https://opentdb.com/api.php?type=multiple",params={"amount": amount, "difficulty": difficulty, "category":category})
        content = res_api.json()
        questions = html.unescape(content['results'])
        session['questions'] = questions
        for question in questions:
            question["answers"] = [i for i in question["incorrect_answers"]]
            question["answers"].append((question["correct_answer"]))
            random.shuffle(question["answers"])
        return render_template('quiz.html', title='Quiz', questions = questions)
    return render_template('home.html', title='Start', form = form)
    

@main.route("/score", methods=['GET','POST'])
@login_required
def score():
    if request.method == 'POST':
        questions = session.get('questions')
        score = 0
        for i in range(len(questions)):
            answer = request.form[str(i)]
            question = questions[i]
            if question["correct_answer"] == answer:
                score += 1 
                question["correct"] = "correct!"
            else:
                question["correct"] = "incorrect!"
        user = User.query.filter_by(id=session["current_user"]).first()
        user.score += score
        db.session.commit()
        session["questions"] = {} 
    return render_template('score.html', score=score, questions=questions, total_score=user.score)

@main.route("/profile", methods=['GET','POST'])
@login_required
def profile():
    user = User.query.filter_by(id=session["current_user"]).first()
    return render_template('profile.html', user=user)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You're already logged in.")
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        session["current_user"] = user.id 
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

@main.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Sucessfully logged out!")
        return redirect(url_for('main.login'))
    else:
        flash("You're not logged in")
        return redirect(url_for('main.login'))

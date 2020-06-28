from flask_wtf import FlaskForm
from wtforms import (BooleanField, IntegerField, PasswordField, SelectField, StringField, SubmitField, TextAreaField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length, NumberRange, Optional, ValidationError)
from app.models import User


# Form for registration displayed on register.html.
class RegisterForm(FlaskForm):    
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

# Form for logging in displayed on login.html.
class LoginForm(FlaskForm):    
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

class GenerateQuizForm(FlaskForm):
    style={'class': 'form-group'}
    amount = IntegerField('Number of Questions', validators=[DataRequired(), NumberRange(min=0, max=20)])
    category = SelectField('Category', coerce=int, choices=[(0,'Any'),(9, 'General Knowledge'), (10, 'Entertainment: Books'), (11, 'Entertainment: Film'), (12, 'Entertainment: Music'), (13, 'Entertainment: Musicals & Theatres'), (14, 'Entertainment: Television'), (15, 'Entertainment: Video Games'), (16, 'Entertainment: Board Games'), (17, 'Science & Nature'), (18, 'Science: Computers'), (19, 'Science: Mathematics'), (20, 'Mythology'), (21, 'Sports'), (22, 'Geography'), (23, 'History'), (24, 'Politics'), (25, 'Art'), (26,'Celebrities'), (27, 'Animals'), (28, 'Vehicles'), (29, 'Entertainment: Comics'), (30, 'Science: Gadgets'), (31, 'Entertainment: Japanese Anime & Manga'), (32, 'Entertainment: Cartoon & Animations')])
    difficulty = SelectField('Difficulty', validators=[DataRequired()], choices=
        [('any','Any'),
        ('easy','Easy'),
        ('medium','Medium'),
        ('hard','Hard')])
    submit = SubmitField('Start')


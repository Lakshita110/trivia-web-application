from . import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Model for a User which is related to the Note.
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship("Note")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

# User loader for flask-login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
login.login_view = 'login'

# Model for a BookReview which references a book's isbn and a user's username.

class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    # !date = db.Column(db.Integer)
    # content = db.Column(db.String)
    # book_isbn = db.Column(db.String, db.ForeignKey("books.isbn"))
    # username = db.Column(db.Integer, db.ForeignKey("users.username"))
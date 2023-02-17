from project import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Columb(db.String(140))
    posts = db.relationship('Article', backref='author', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    topic = db.Column(db.Text)
    header = db.Column(db.Integer)
    content = db.Column(db.Integer)

    def __repr__(self):
        return '<Post {}>'.format(self.topic, '\n', self.header, '\n', self.content)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

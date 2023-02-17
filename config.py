import os

key = 'qweqwe'
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

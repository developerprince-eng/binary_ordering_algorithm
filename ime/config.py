import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True

#SQLALCHEMY DATABASE CONFIGURATIONS
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'ime.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
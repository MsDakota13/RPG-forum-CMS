import os
import configparser

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join(basedir, '../config/config.ini'))

        self.SECRET_KEY = self.config.get('General','secret_key') or 'you-will-never-guess'
        self.SQLALCHEMY_DATABASE_URI = self.config.get('Database','url') or 'sqlite:///' + os.path.join(basedir, 'app.db')
        self.SQLALCHEMY_TRACK_MODIFICATIONS = self.config.get('Database','debug') or False

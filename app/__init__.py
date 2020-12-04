from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()
db = SQLAlchemy()


# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views
from app import routes
from flask import Flask
import os
from app.config import Config

app = Flask(__name__)
# app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
app.register_blueprint(routes.bp)
app.config.from_object(Config)
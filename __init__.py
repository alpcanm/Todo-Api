from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
app.config["JWT_SECRET_KEY"] = '23123123123123'
jwt = JWTManager(app)
CORS(app)


def create_app():
    return app

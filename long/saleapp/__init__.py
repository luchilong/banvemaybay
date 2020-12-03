from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
import os

app = Flask(__name__)
app.secret_key = "^%@&^@*&!@67532623^@%^%@!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/bvmb?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['ROOT_PROJECT_PATH'] = app.root_path

db = SQLAlchemy(app=app)
admin = Admin(app=app, name="Đại Lý Vé Máy Bay", template_mode="bootstrap4")
login = LoginManager(app=app)
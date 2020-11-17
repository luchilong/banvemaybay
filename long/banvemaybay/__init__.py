from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

banvemaybay = Flask(__name__)
banvemaybay.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/BVMB?charset=utf8mb4'
banvemaybay.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=banvemaybay)
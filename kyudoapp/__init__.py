# app.config.from_object('kyudoapp.config')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)  # SQLAlchemyをappに紐付け

from kyudoapp.models.result import Result  # Resultモデルをインポート


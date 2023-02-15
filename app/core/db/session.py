# Flask
from flask_sqlalchemy import SQLAlchemy


from main import app
from core.db.base import Base

db = SQLAlchemy(app, model_class=Base)
db_session = db.session
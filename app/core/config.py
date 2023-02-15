# Import app code
from main import app

from core.data import SQLALCHEMY_MYSQL_URI

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_MYSQL_URI
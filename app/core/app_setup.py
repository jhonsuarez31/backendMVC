# Import app code
from main import app

# Set up global variables
from core import data

# Set up Config Environments
from core import config

# Set up flask db session
from core.db.session import db_session

#Set cors
from core import cors

# Set up Flask Endpoints

from api.v1 import api as api_v1




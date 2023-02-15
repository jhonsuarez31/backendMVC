# Import installed packages
from flask import Flask

# Import app code
app = Flask (__name__)

import core.app_setup

if __name__ == "__main__":
    app.run( debug = True, )
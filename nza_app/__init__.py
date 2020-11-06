from flask import Flask

# Import the Config Object
from config import Config

# Import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# Import the Migrate Object
from flask_migrate import Migrate

# Import for the Flask Login Module
from flask_login import LoginManager

app = Flask(__name__)
# Complete the Config cycle for our Flask App
# And Give access to our Database(When we have one)
# Along with our Secret Key
app.config.from_object(Config)

# Init our database (db)
db = SQLAlchemy(app)

# Init the migrator 
migrate = Migrate(app,db)


# Login Config - Init for the LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Specify what page to load for NON-authenticated users

from nza_app import routes,models
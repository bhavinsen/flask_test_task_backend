from flask import Flask
from config import Config
from flask_migrate import Migrate
from .db import db

    
app = Flask(__name__)
app.config.from_object(Config)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config ['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

migrate = Migrate(app, db)

db.init_app(app)
migrate.init_app(app, db)

from .models.models import About

# register api blueprint
from .api import bp as api_bp

app.register_blueprint(api_bp, url_prefix='/api')

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Shared extension instances; the real Flask app & config are in app.py
db = SQLAlchemy()
ma = Marshmallow()

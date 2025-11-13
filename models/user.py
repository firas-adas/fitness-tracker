from sqlalchemy import func
from models.schemas import Actor
from core import ma, db

from sqlalchemy import DateTime, Enum
from core import db
from sqlalchemy.sql import func


class User(db.Model):
    __tablename__ = 'User'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    gender = db.Column(Enum('Male', 'Female'))
    age = db.Column(db.Integer, nullable=True)
    activity_level = db.Column(db.String(50), nullable=True)
    experience = db.Column(db.String(50), nullable=True)
    subscription_status = db.Column(Enum('Active', 'Inactive'), default='Active')
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())

    goals = db.relationship('Goal', back_populates='user', cascade='all, delete-orphan')
    workouts = db.relationship('Workout', back_populates='user', cascade='all, delete-orphan')
    body_metrics = db.relationship('BodyMetric', back_populates='user', cascade='all, delete-orphan')
    nutrition_entries = db.relationship('Nutrition', back_populates='user', cascade='all, delete-orphan')

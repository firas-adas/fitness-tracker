from core.__init__ import db  # your SQLAlchemy instance
from sqlalchemy import func    # for func.now() in last_update
from sqlalchemy.types import DateTime  # for DateTime columns

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=True)
    activity_level = db.Column(db.String(50), nullable=True)
    experience = db.Column(db.String(50), nullable=True)
    last_update = db.Column(DateTime(timezone=True), onupdate=func.now())
    
    workouts = db.relationship("Workout", back_populates="user", cascade="all, delete-orphan")
    body_metrics = db.relationship('BodyMetric', back_populates='user', cascade='all, delete-orphan')
    nutrition_entries = db.relationship('Nutrition', back_populates='user', cascade='all, delete-orphan')

class Workout(db.Model):
    __tablename__ = 'workout'

    workout_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    workout_type = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    calories_burned = db.Column(db.Integer, nullable=True)
    workout_date = db.Column(db.Date, nullable=True)
    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())

    user = db.relationship("User", back_populates="workouts")

class BodyMetric(db.Model):
    __tablename__ = "body_metric"

    body_metric_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    weight = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True)
    bmi = db.Column(db.Float, nullable=True)
    recorded_date = db.Column(db.Date, nullable=True)

    last_update = db.Column(DateTime(timezone=True), nullable=True, onupdate=func.now())

    user = db.relationship("User", back_populates="body_metrics")

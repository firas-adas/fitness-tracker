from core import db, ma
from datetime import datetime
from sqlalchemy import func

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
    last_update = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())

# Functions used by app.py
def get_users():
    return User.query.all()

def add_user(first_name, last_name, email, date_of_birth, gender, activity_level, experience):
    dob = None
    if date_of_birth:
        try:
            dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except:
            pass
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        date_of_birth=dob,
        gender=gender,
        activity_level=activity_level,
        experience=experience
    )
    db.session.add(new_user)
    db.session.commit()

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()

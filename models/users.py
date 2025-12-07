from core import db
from datetime import datetime
from sqlalchemy import func

class User(db.Model):
    __tablename__ = 'User'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    gender = db.Column(db.String(20), nullable=True)  
    subscription_status = db.Column(db.String(20), nullable=True)
    last_update = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())

def get_users():
    return User.query.all()

def add_user(first_name, last_name, email, gender, birthdate):
    dob = datetime.strptime(birthdate, "%Y-%m-%d").date() if birthdate else None
    
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender=gender,
        date_of_birth=dob
    )
    db.session.add(new_user)
    db.session.commit()

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()

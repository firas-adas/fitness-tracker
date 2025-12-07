from core import db
from datetime import datetime

class Workout(db.Model):
    __tablename__ = "Workout"

    workout_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    workout_type = db.Column(db.String(50))
    duration = db.Column(db.Integer)
    calories_burned = db.Column(db.Integer)
    workout_date = db.Column(db.Date)

def get_workouts_by_user(user_id):
    return Workout.query.filter_by(user_id=user_id).all()

def add_workout(user_id, workout_type, duration, calories_burned, workout_date):
    wd = datetime.strptime(workout_date, "%Y-%m-%d").date() if workout_date else None
    new_workout = Workout(
        user_id=user_id,
        workout_type=workout_type,
        duration=duration,
        calories_burned=calories_burned,
        workout_date=wd
    )
    db.session.add(new_workout)
    db.session.commit()

def delete_workout(workout_id):
    w = Workout.query.get(workout_id)
    if w:
        db.session.delete(w)
        db.session.commit()

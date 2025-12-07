from core import db, ma
from datetime import datetime

class Workout(db.Model):
    __tablename__ = "Workout"

    workout_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    workout_name = db.Column(db.String(100))
    scheduled_datetime = db.Column(db.DateTime)

def get_workouts_by_user(user_id):
    return Workout.query.filter_by(user_id=user_id).all()

def add_workout(user_id, workout_name, scheduled_datetime):
    sd = datetime.strptime(scheduled_datetime, "%Y-%m-%d") if scheduled_datetime else None
    new_workout = Workout(user_id=user_id, workout_name=workout_name, scheduled_datetime=sd)
    db.session.add(new_workout)
    db.session.commit()

def delete_workout(workout_id):
    w = Workout.query.get(workout_id)
    if w:
        db.session.delete(w)
        db.session.commit()

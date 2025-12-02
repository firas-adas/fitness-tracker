from core import db
from datetime import datetime

class WorkoutSet(db.Model):
    __tablename__ = 'workout_set'

    set_id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, nullable=False)
    exercise_id = db.Column(db.Integer, nullable=False)
    set_number = db.Column(db.Integer)
    weight = db.Column(db.Numeric(6, 2))
    reps = db.Column(db.Integer)
    rpe = db.Column(db.Numeric(3, 1))
    note = db.Column(db.String(255))

def get_workout_sets():
    return WorkoutSet.query.all()

def add_workout_set(workout_id, exercise_id, set_number, weight, reps, rpe, note):
    new_set = WorkoutSet(
        workout_id=workout_id,
        exercise_id=exercise_id,
        set_number=set_number,
        weight=weight,
        reps=reps,
        rpe=rpe,
        note=note
    )
    db.session.add(new_set)
    db.session.commit()

def delete_workout_set(set_id):
    ws = WorkoutSet.query.get(set_id)
    if ws:
        db.session.delete(ws)
        db.session.commit()
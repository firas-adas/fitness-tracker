from sqlalchemy import func
from datetime import datetime
from core import ma, db
from models.schemas import Workout


# ------------------- GET WORKOUTS BY USER -------------------

def get_workouts_by_user(user_id):
    workouts = Workout.query.filter_by(user_id=user_id).all()
    return workouts_schema.dump(workouts)


# ------------------- ADD WORKOUT -------------------

def add_workout(user_id, workout_type, duration, calories_burned, workout_date):
    
    date_obj = None
    if workout_date and workout_date != "":
        try:
            date_obj = datetime.strptime(workout_date, "%Y-%m-%d").date()
        except ValueError:
            date_obj = None

    new_workout = Workout(
        user_id=user_id,
        workout_type=workout_type,
        duration=duration,
        calories_burned=calories_burned,
        workout_date=date_obj,
        last_update=func.now()
    )

    db.session.add(new_workout)
    db.session.commit()


# ------------------- DELETE WORKOUT -------------------

def delete_workout(workout_id):
    workout = Workout.query.get(workout_id)
    if workout:
        db.session.delete(workout)
        db.session.commit()


# ------------------- MARSHMALLOW SCHEMA -------------------

class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True


workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

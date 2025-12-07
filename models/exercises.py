from core import db

class Exercise(db.Model):
  __tablename__ = "exercise"

exercise_id = db.Column(db.Integer, primary_key=True)
exercise_name = db.Column(db.String(100), nullable=False)
description = db.Column(db.String(255))

#Foreign Keys
muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_group.muscle_group_id'), nullable=True)
equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.equipment_id'), nullable=True)

#setup relationships for MuscleGroup and Equipment
muscle_group = db.relationship('MuscleGroup', backref='exercises')
equipment = db.relationship('Equipment', backref='exercises')

def get_all_exercises():
  return Exercise.query.all()

def get_exercise_by_id(exercise_id):
  return Exercise.query.get(exercise_id)

def add_exercise(exercise_name, muscle_group_id, equipment_id, description=None):
  new_exercise = Exercise(
    exercise_name=exercise_name,
    muscle_group_id=muscle_group_id,
    equipment_id=equipment_id,
    description=description
  )
  db.session.add(new_exercise)
  db.session.commit()
  return new_exercise

def delete_exercise(exercise_id):
  ex = Exercise.query.get(exercise_id)
  if ex:
    db.session.delete(ex)
    db.session.commit()

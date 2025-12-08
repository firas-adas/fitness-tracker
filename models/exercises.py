from core import db

class MuscleGroup(db.Model):
    __tablename__ = "MuscleGroup"

    muscle_group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Equipment(db.Model):
    __tablename__ = "Equipment"

    equipment_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Exercise(db.Model):
    __tablename__ = "Exercise"

    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    # Foreign Keys
    muscle_group_id = db.Column(
        db.Integer,
        db.ForeignKey('MuscleGroup.muscle_group_id'),
        nullable=True
    )
    equipment_id = db.Column(
        db.Integer,
        db.ForeignKey('Equipment.equipment_id'),
        nullable=True
    )

    # Relationships
    muscle_group = db.relationship('MuscleGroup', backref='exercises')
    equipment = db.relationship('Equipment', backref='exercises')


def get_all_exercises():
    return Exercise.query.all()

def get_exercise_by_id(exercise_id):
    return Exercise.query.get(exercise_id)

def add_exercise(exercise_name, muscle_group_id=None, equipment_id=None, description=None):
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

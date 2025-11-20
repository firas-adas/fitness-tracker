from sqlalchemy import func
from datetime import datetime
from models.schemas import User
from core import ma, db


# ------------------- GET ALL USERS -------------------

def get_users():
    all_users = User.query.all()
    return users_schema.dump(all_users)


# ------------------- ADD NEW USER -------------------

def add_user(first_name, last_name, email, date_of_birth, gender,
             activity_level, experience):

    # Convert date string -> date object
    dob = None
    if date_of_birth and date_of_birth != "":
        try:
            dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except ValueError:
            dob = None

    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        date_of_birth=dob,
        gender=gender if gender != "" else None,
        activity_level=activity_level,
        experience=experience,
        last_update=func.now()
    )

    db.session.add(new_user)
    db.session.commit()


# ------------------- DELETE USER -------------------

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()


# ------------------- MARSHMALLOW SCHEMA -------------------

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)

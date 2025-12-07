from core import db
from datetime import datetime

class Nutrition(db.Model):
    __tablename__ = "Nutrition"

    nutrition_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    calories = db.Column(db.Float)
    protein = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fat = db.Column(db.Float)
    log_date = db.Column(db.Date)

def get_nutrition_by_user(user_id):
    return Nutrition.query.filter_by(user_id=user_id).all()

def add_nutrition(user_id, calories, protein, carbs, fat, log_date):
    ld = datetime.strptime(log_date, "%Y-%m-%d").date() if log_date else None

    new_entry = Nutrition(
        user_id=user_id,
        calories=calories,
        protein=protein,
        carbs=carbs,
        fat=fat,
        log_date=ld
    )
    db.session.add(new_entry)
    db.session.commit()

def delete_nutrition(nutrition_id):
    entry = Nutrition.query.get(nutrition_id)
    if entry:
        db.session.delete(entry)
        db.session.commit()

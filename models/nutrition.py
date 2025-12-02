from core import db, ma
from datetime import datetime

class Nutrition(db.Model):
    __tablename__ = 'nutrition'

    nutrition_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Float)
    protein = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fat = db.Column(db.Float)
    water = db.Column(db.Float)
    consistency = db.Column(db.String(50))
    log_date = db.Column(db.Date)

# Schema for app.py nutrition dumping
class NutritionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Nutrition
        load_instance = True

nutritions_schema = NutritionSchema(many=True)

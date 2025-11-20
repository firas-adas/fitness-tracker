from core import db, ma
from sqlalchemy import Date, Integer
from sqlalchemy.sql import func
from datetime import date


class Nutrition(db.Model):
    __tablename__ = "nutrition"

    nutrition_id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

    calories = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Integer, nullable=False)
    water = db.Column(db.Integer, nullable=True)
    consistency = db.Column(db.String(50), nullable=True)

    log_date = db.Column(Date, nullable=False, default=date.today)

    last_update = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    user = db.relationship("User", backref="nutrition_logs")


# ------------------- SCHEMA -------------------

class NutritionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Nutrition
        load_instance = True


nutrition_schema = NutritionSchema()
nutritions_schema = NutritionSchema(many=True)

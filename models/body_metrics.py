from sqlalchemy import func
from datetime import datetime
from models.schemas import BodyMetric
from core import ma, db


# ------------------- GET ALL BODY METRICS -------------------

def get_body_metrics():
    metrics = BodyMetric.query.all()
    return body_metrics_schema.dump(metrics)


# ------------------- ADD BODY METRIC -------------------

def add_body_metric(user_id, weight, height, bmi, recorded_date):

    record_date = None
    if recorded_date and recorded_date != "":
        try:
            record_date = datetime.strptime(recorded_date, "%Y-%m-%d").date()
        except ValueError:
            record_date = None

    metric = BodyMetric(
        user_id=user_id,
        weight=weight,
        height=height,
        bmi=bmi,
        recorded_date=record_date,
        last_update=func.now()
    )

    db.session.add(metric)
    db.session.commit()


# ------------------- DELETE BODY METRIC -------------------

def delete_body_metric(metric_id):
    metric = BodyMetric.query.get(metric_id)
    if metric:
        db.session.delete(metric)
        db.session.commit()


# ------------------- MARSHMALLOW SCHEMA -------------------

class BodyMetricSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BodyMetric
        load_instance = True


body_metric_schema = BodyMetricSchema()
body_metrics_schema = BodyMetricSchema(many=True)

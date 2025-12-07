from core import db
from datetime import datetime

class BodyMetric(db.Model):
    __tablename__ = "BodyMetric"

    metric_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    measurement_date = db.Column(db.Date)


def get_metrics_by_user(user_id):
    return BodyMetric.query.filter_by(user_id=user_id).all()


def add_metric(user_id, weight, height, measurement_date):
    md = datetime.strptime(measurement_date, "%Y-%m-%d").date() if measurement_date else None
    new_metric = BodyMetric(user_id=user_id, weight=weight, height=height, measurement_date=md)
    db.session.add(new_metric)
    db.session.commit()


def delete_metric(metric_id):
    m = BodyMetric.query.get(metric_id)
    if m:
        db.session.delete(m)
        db.session.commit()

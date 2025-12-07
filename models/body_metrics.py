from core import db, ma
from datetime import datetime

class BodyMetric(db.Model):
    __tablename__ = "BodyMetric"

    metric_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'))
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    measurement_date = db.Column(db.Date)


def get_body_metrics():
    return BodyMetric.query.all()

def add_body_metric(user_id, weight, height, bmi, recorded_date):
    rd = datetime.strptime(recorded_date, "%Y-%m-%d").date() if recorded_date else None
    bm = BodyMetric(user_id=user_id, weight=weight, height=height, bmi=bmi, recorded_date=rd)
    db.session.add(bm)
    db.session.commit()

def delete_body_metric(body_metric_id):
    bm = BodyMetric.query.get(body_metric_id)
    if bm:
        db.session.delete(bm)
        db.session.commit()

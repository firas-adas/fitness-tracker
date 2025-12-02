from core import db, ma
from datetime import datetime

class Goal(db.Model):
    __tablename__ = 'goal'

    goal_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    goal_type = db.Column(db.String(50))
    target_value = db.Column(db.Float)
    start_date = db.Column(db.Date)
    target_date = db.Column(db.Date)

def get_goals():
    return Goal.query.all()

def add_goal(user_id, goal_type, target_value, start_date, target_date):
    sd = datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
    td = datetime.strptime(target_date, "%Y-%m-%d").date() if target_date else None
    new_goal = Goal(user_id=user_id, goal_type=goal_type, target_value=target_value,
                    start_date=sd, target_date=td)
    db.session.add(new_goal)
    db.session.commit()

def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if goal:
        db.session.delete(goal)
        db.session.commit()

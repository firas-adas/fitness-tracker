from core import db, ma

# SQLAlchemy Goal model
class Goal(db.Model):
    __tablename__ = "Goal"

    goal_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.user_id"), nullable=False)

    goal_type = db.Column(db.String(50))
    target_value = db.Column(db.Float)
    start_date = db.Column(db.Date)
    target_date = db.Column(db.Date)

    # Relationship: each goal belongs to a user
    user = db.relationship("User", back_populates="goals")

class GoalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Goal

goal_schema = GoalSchema()
goals_schema = GoalSchema(many=True)



def get_goals():
    all_goals = Goal.query.all()
    return goals_schema.dump(all_goals)


def get_goal(goal_id):
    return Goal.query.get(goal_id)


def add_goal(user_id, goal_type=None, target_value=None, start_date=None, target_date=None):
    new_goal = Goal(
        user_id=user_id,
        goal_type=goal_type,
        target_value=target_value,
        start_date=start_date,
        target_date=target_date
    )
    db.session.add(new_goal)
    db.session.commit()
    return new_goal


def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if goal:
        db.session.delete(goal)
        db.session.commit()
        return True
    return False
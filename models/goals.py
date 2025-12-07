from core import db

class Goal(db.Model):
    __tablename__ = "Goal"

    id = db.Column(db.Integer, primary_key=True)
    
    # FIXED foreign key reference (matches User table and column exactly)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)

    weight_goal = db.Column(db.Float, nullable=True)
    calorie_goal = db.Column(db.Integer, nullable=True)

def get_goal_for_user(user_id):
    return Goal.query.filter_by(user_id=user_id).first()

def save_goal(user_id, weight_goal, calorie_goal):
    goal = get_goal_for_user(user_id)

    if goal:
        goal.weight_goal = weight_goal
        goal.calorie_goal = calorie_goal
    else:
        goal = Goal(
            user_id=user_id,
            weight_goal=weight_goal,
            calorie_goal=calorie_goal
        )
        db.session.add(goal)

    db.session.commit()

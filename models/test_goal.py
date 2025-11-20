from datetime import date
from app import db
from models.goal import add_goal, get_goals, get_goal, delete_goal

# Make sure your Flask app context is available if using Flask
from core import create_app

app = create_app()
app.app_context().push()

# --- Add a new goal ---
goal = add_goal(
    user_id=1, 
    goal_type="Weight Loss", 
    target_value=180, 
    start_date=date.today(),
    target_date=date(2025, 12, 31)
)
print("Added Goal:", goal.goal_id, goal.goal_type, goal.target_value)

# --- Get all goals ---
all_goals = get_goals()
print("All Goals:", all_goals)

# --- Get a single goal ---
single_goal = get_goal(goal.goal_id)
print("Single Goal:", single_goal.goal_id, single_goal.goal_type)

# --- Delete the goal ---
deleted = delete_goal(goal.goal_id)
print("Deleted:", deleted)

# --- Confirm deletion ---
all_goals_after = get_goals()
print("All Goals After Deletion:", all_goals_after)

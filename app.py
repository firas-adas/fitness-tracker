from core import app
from flask import redirect, request, url_for, render_template

from models.user import UserModel

from models.goal import Goal
import models.goal as GoalModel

from models.workouts import Workout
import models.workouts as WorkoutModel

from models.body_metrics import BodyMetric
import models.body_metrics as BodyModel

from models.nutrition import Nutrition
import models.nutrition as NutritionModel

from datetime import datetime

# ---------------- HOME ----------------

@app.route('/')
def index():
    return render_template('index.html')


# ---------------- USERS ----------------

# View all users
@app.route('/users')
def users_list():
    users = UserModel.get_users()
    return render_template('users.html', users=users)


# Render add user form
@app.route('/add_user', methods=["GET"])
def add_user_form():
    return render_template('add_user.html')


# Add user to database
@app.route('/add_user', methods=["POST"])
def add_user():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    date_of_birth = request.form.get("date_of_birth")
    gender = request.form.get("gender")
    activity_level = request.form.get("activity_level")
    experience = request.form.get("experience")

    UserModel.add_user(
        first_name,
        last_name,
        email,
        date_of_birth,
        gender,
        activity_level,
        experience
    )

    return redirect('/users')


# Delete user
@app.route('/delete_user/<int:id>')
def delete_user(id):
    UserModel.delete_user(id)
    return redirect('/users')


# ---------------- GOALS ----------------

# View all goals
@app.route('/goals')
def goals_list():
    goals = GoalModel.get_goals()
    return render_template('goals.html', goals=goals)


# Render add goal form
@app.route('/add_goal', methods=["GET"])
def add_goal_form():
    return render_template('add_goal.html')


# Add goal to database
@app.route('/add_goal', methods=["POST"])
def add_goal():
    user_id = request.form.get("user_id")
    goal_type = request.form.get("goal_type")
    target_value = request.form.get("target_value")
    start_date = request.form.get("start_date")
    target_date = request.form.get("target_date")

    # type conversions / sanitization
    try:
        user_id = int(user_id) if user_id else None
    except (ValueError, TypeError):
        user_id = None

    try:
        target_value = float(target_value) if target_value else None
    except (ValueError, TypeError):
        target_value = None

    # dates
    def _parse_date(s):
        if not s:
            return None
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            return None

    start_date = _parse_date(start_date)
    target_date = _parse_date(target_date)

    GoalModel.add_goal(
        user_id,
        goal_type,
        target_value,
        start_date,
        target_date
    )

    return redirect('/goals')


# Delete goal
@app.route('/delete_goal/<int:id>')
def delete_goal(id):
    GoalModel.delete_goal(id)
    return redirect('/goals')


# ---------------- WORKOUTS ----------------

# View all workouts
@app.route('/workouts')
def workouts_list():
    workouts = WorkoutModel.get_workouts()
    return render_template('workouts.html', workouts=workouts)


# Render add workout form
@app.route('/add_workout', methods=["GET"])
def add_workout_form():
    return render_template('add_workout.html')


# Add workout to database
@app.route('/add_workout', methods=["POST"])
def add_workout():
    user_id = request.form.get("user_id")
    workout_type = request.form.get("workout_type")
    duration = request.form.get("duration")
    calories_burned = request.form.get("calories_burned")
    workout_date = request.form.get("workout_date")

    try:
        user_id = int(user_id) if user_id else None
    except (ValueError, TypeError):
        user_id = None

    try:
        duration = int(duration) if duration else None
    except (ValueError, TypeError):
        duration = None

    try:
        calories_burned = int(calories_burned) if calories_burned else None
    except (ValueError, TypeError):
        calories_burned = None

    try:
        workout_date = datetime.strptime(workout_date, "%Y-%m-%d").date() if workout_date else None
    except ValueError:
        workout_date = None

    WorkoutModel.add_workout(
        user_id,
        workout_type,
        duration,
        calories_burned,
        workout_date
    )

    return redirect('/workouts')


# Delete workout
@app.route('/delete_workout/<int:id>')
def delete_workout(id):
    WorkoutModel.delete_workout(id)
    return redirect('/workouts')


# ---------------- BODY METRICS ----------------

# View all body metrics
@app.route('/metrics')
def metrics_list():
    metrics = BodyModel.get_metrics()
    return render_template('metrics.html', metrics=metrics)


# Render add metric form
@app.route('/add_metric', methods=["GET"])
def add_metric_form():
    return render_template('add_metric.html')


# Add a body metric entry
@app.route('/add_metric', methods=["POST"])
def add_metric():
    user_id = request.form.get("user_id")
    weight = request.form.get("weight")
    height = request.form.get("height")
    bmi = request.form.get("bmi")
    recorded_date = request.form.get("recorded_date")

    try:
        user_id = int(user_id) if user_id else None
    except (ValueError, TypeError):
        user_id = None

    def _to_float(v):
        try:
            return float(v) if v else None
        except (ValueError, TypeError):
            return None

    weight = _to_float(weight)
    height = _to_float(height)
    bmi = _to_float(bmi)

    try:
        recorded_date = datetime.strptime(recorded_date, "%Y-%m-%d").date() if recorded_date else None
    except ValueError:
        recorded_date = None

    BodyModel.add_metric(
        user_id,
        weight,
        height,
        bmi,
        recorded_date
    )

    return redirect('/metrics')


# Delete a metric
@app.route('/delete_metric/<int:id>')
def delete_metric(id):
    BodyModel.delete_metric(id)
    return redirect('/metrics')


# ---------------- NUTRITION ----------------

# View all nutrition entries
@app.route('/nutrition')
def nutrition_list():
    entries = NutritionModel.get_nutrition()
    return render_template('nutrition.html', entries=entries)


# Render add nutrition form
@app.route('/add_nutrition', methods=["GET"])
def add_nutrition_form():
    return render_template('add_nutrition.html')


# Add nutrition entry
@app.route('/add_nutrition', methods=["POST"])
def add_nutrition():
    user_id = request.form.get("user_id")
    calories = request.form.get("calories")
    protein = request.form.get("protein")
    carbs = request.form.get("carbs")
    fat = request.form.get("fat")
    log_datetime = request.form.get("log_datetime")

    try:
        user_id = int(user_id) if user_id else None
    except (ValueError, TypeError):
        user_id = None

    def _to_decimal(v):
        try:
            return float(v) if v else None
        except (ValueError, TypeError):
            return None

    calories = int(calories) if calories else 0
    protein = _to_decimal(protein)
    carbs = _to_decimal(carbs)
    fat = _to_decimal(fat)

    # If log_datetime provided, try to parse (YYYY-MM-DD HH:MM) or date-only
    parsed_dt = None
    if log_datetime:
        for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M", "%Y-%m-%d"):
            try:
                parsed = datetime.strptime(log_datetime, fmt)
                parsed_dt = parsed if fmt != "%Y-%m-%d" else parsed.date()
                break
            except ValueError:
                continue

    NutritionModel.add_nutrition(
        user_id,
        calories,
        protein,
        carbs,
        fat,
        parsed_dt
    )

    return redirect('/nutrition')


# Delete nutrition
@app.route('/delete_nutrition/<int:id>')
def delete_nutrition(id):
    NutritionModel.delete_nutrition(id)
    return redirect('/nutrition')


# ---------------- MAIN ----------------

if __name__ == '__main__':
    app.run(port=8001, debug=True)
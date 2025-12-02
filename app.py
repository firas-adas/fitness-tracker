from core import app
from flask import redirect, request, url_for, render_template
from models import user as UserModel
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

from models import goal as GoalModel

# View goals for a specific user
@app.route('/goals/<int:user_id>')
def goals_list(user_id):
    goals = GoalModel.get_goals()
    return render_template('goals.html', goals=goals, user_id=user_id)

# Render add-goal form
@app.route('/add_goal/<int:user_id>', methods=["GET"])
def add_goal_form(user_id):
    return render_template('add_goal.html', user_id=user_id)

# Add goal
@app.route('/add_goal/<int:user_id>', methods=["POST"])
def add_goal(user_id):
    goal_type = request.form.get("goal_type")
    target_value = request.form.get("target_value")
    start_date = request.form.get("start_date")
    target_date = request.form.get("target_date")

    GoalModel.add_goal(user_id, goal_type, target_value, start_date, target_date)
    return redirect(f'/goals/{user_id}')

# Delete goal
@app.route('/delete_goal/<int:id>')
def delete_goal(id):
    GoalModel.delete_goal(id)
    return redirect('/users')

from models import workouts as WorkoutModel

# View workouts for a user
@app.route('/workouts/<int:user_id>')
def workouts_list(user_id):
    workouts = WorkoutModel.get_workouts_by_user(user_id)
    return render_template('workouts.html', workouts=workouts, user_id=user_id)

# Render add workout form
@app.route('/add_workout/<int:user_id>', methods=["GET"])
def add_workout_form(user_id):
    return render_template('add_workout.html', user_id=user_id)

# Add workout
@app.route('/add_workout/<int:user_id>', methods=["POST"])
def add_workout(user_id):
    workout_type = request.form.get("workout_type")
    duration = request.form.get("duration")
    calories = request.form.get("calories_burned")
    workout_date = request.form.get("workout_date")

    WorkoutModel.add_workout(user_id, workout_type, duration, calories, workout_date)
    return redirect(f'/workouts/{user_id}')

# Delete workout
@app.route('/delete_workout/<int:id>')
def delete_workout(id):
    WorkoutModel.delete_workout(id)
    return redirect('/users')


from models import body_metrics as BodyModel

@app.route('/metrics/<int:user_id>')
def metrics_list(user_id):
    metrics = BodyModel.get_body_metrics()
    return render_template('body_metrics.html', metrics=metrics, user_id=user_id)

@app.route('/add_metric/<int:user_id>', methods=["GET"])
def add_metric_form(user_id):
    return render_template('add_body_metric.html', user_id=user_id)

@app.route('/add_metric/<int:user_id>', methods=["POST"])
def add_metric(user_id):
    weight = request.form.get("weight")
    height = request.form.get("height")
    bmi = request.form.get("bmi")
    recorded_date = request.form.get("recorded_date")

    BodyModel.add_body_metric(user_id, weight, height, bmi, recorded_date)
    return redirect(f'/metrics/{user_id}')

@app.route('/delete_metric/<int:id>')
def delete_metric(id):
    BodyModel.delete_body_metric(id)
    return redirect('/users')

from models import nutrition as NutritionModel

@app.route('/nutrition/<int:user_id>')
def nutrition_list(user_id):
    nutrition = NutritionModel.nutritions_schema.dump(
        NutritionModel.Nutrition.query.filter_by(user_id=user_id).all()
    )
    return render_template('nutrition.html', nutrition=nutrition, user_id=user_id)

@app.route('/add_nutrition/<int:user_id>', methods=["GET"])
def add_nutrition_form(user_id):
    return render_template('add_nutrition.html', user_id=user_id)

@app.route('/add_nutrition/<int:user_id>', methods=["POST"])
def add_nutrition(user_id):
    calories = request.form.get("calories")
    protein = request.form.get("protein")
    carbs = request.form.get("carbs")
    fat = request.form.get("fat")
    water = request.form.get("water")
    consistency = request.form.get("consistency")
    log_date = request.form.get("log_date")

    # Add entry
    entry = NutritionModel.Nutrition(
        user_id=user_id,
        calories=calories,
        protein=protein,
        carbs=carbs,
        fat=fat,
        water=water,
        consistency=consistency,
        log_date=log_date
    )

    from core import db
    db.session.add(entry)
    db.session.commit()

    return redirect(f'/nutrition/{user_id}')

@app.route('/delete_nutrition/<int:id>')
def delete_nutrition(id):
    entry = NutritionModel.Nutrition.query.get(id)
    if entry:
        from core import db
        db.session.delete(entry)
        db.session.commit()
    return redirect('/users')



# ---------------- MAIN ----------------

if __name__ == '__main__':
    app.run(port=8001, debug=True)

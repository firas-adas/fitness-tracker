from flask import Flask, render_template, request, redirect, url_for
from core import db
from dotenv import load_dotenv
import os

# --- Load .env variables ---
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# --- Models ---
from models.users import User, add_user, delete_user
from models.workouts import Workout, get_workouts_by_user, add_workout, delete_workout
from models.body_metrics import BodyMetric, get_metrics_by_user, add_metric, delete_metric
from models.nutrition import Nutrition, get_nutrition_by_user, add_nutrition, delete_nutrition
from models.goals import Goal, get_goal_for_user, save_goal   # << NEW

app = Flask(__name__, template_folder="templates")

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ---------- HOME ----------
@app.route('/')
def home():
    return render_template('index.html')

# ---------- USERS ----------
@app.route('/users')
def users_list():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user_route():
    if request.method == 'POST':
        add_user(
            request.form['first_name'],
            request.form['last_name'],
            request.form['email'],
            request.form.get('birthdate'),
            request.form.get('gender'),
            request.form.get('activity_level'),
            request.form.get('experience')
        )
        return redirect(url_for('users_list'))
    return render_template('add_user.html')

@app.route('/delete_user/<int:id>')
def delete_user_route(id):
    delete_user(id)
    return redirect(url_for('users_list'))


# ---------- WORKOUTS ----------
@app.route('/workouts/<int:user_id>')
def workouts_list(user_id):
    workouts = get_workouts_by_user(user_id)
    return render_template('workouts.html', workouts=workouts, user_id=user_id)

@app.route('/workouts/add/<int:user_id>', methods=['GET', 'POST'])
def add_workout_form(user_id):
    if request.method == 'POST':
        add_workout(
            user_id,
            request.form['workout_name'],
            request.form['scheduled_datetime']
        )
        return redirect(url_for('workouts_list', user_id=user_id))
    return render_template('add_workout.html', user_id=user_id)

@app.route('/workouts/delete/<int:id>')
def delete_workout_route(id):
    workout = Workout.query.get(id)
    user_id = workout.user_id
    delete_workout(id)
    return redirect(url_for('workouts_list', user_id=user_id))


# ---------- METRICS ----------
@app.route('/metrics/<int:user_id>')
def metrics_list(user_id):
    metrics = get_metrics_by_user(user_id)
    return render_template('metrics.html', metrics=metrics, user_id=user_id)

@app.route('/metrics/add/<int:user_id>', methods=['GET', 'POST'])
def add_metric_form(user_id):
    if request.method == 'POST':
        add_metric(
            user_id,
            request.form['weight'],
            request.form['height'],
            request.form['measurement_date']
        )
        return redirect(url_for('metrics_list', user_id=user_id))
    return render_template('add_metric.html', user_id=user_id)

@app.route('/metrics/delete/<int:id>')
def delete_metric_route(id):
    metric = BodyMetric.query.get(id)
    user_id = metric.user_id
    delete_metric(id)
    return redirect(url_for('metrics_list', user_id=user_id))


# ---------- NUTRITION ----------
@app.route('/nutrition/<int:user_id>')
def nutrition_list(user_id):
    logs = get_nutrition_by_user(user_id)
    return render_template('nutrition.html', logs=logs, user_id=user_id)

@app.route('/nutrition/add/<int:user_id>', methods=['GET', 'POST'])
def add_nutrition_form(user_id):
    if request.method == 'POST':
        add_nutrition(
            user_id,
            request.form['calories'],
            request.form['protein'],
            request.form['carbs'],
            request.form['fat'],
            request.form['log_date']
        )
        return redirect(url_for('nutrition_list', user_id=user_id))
    return render_template('add_nutrition.html', user_id=user_id)

@app.route('/nutrition/delete/<int:id>')
def delete_nutrition_route(id):
    entry = Nutrition.query.get(id)
    user_id = entry.user_id
    delete_nutrition(id)
    return redirect(url_for('nutrition_list', user_id=user_id))



from models.goals import Goal, get_goal_for_user, save_goal

@app.route('/goals/<int:user_id>', methods=['GET', 'POST'])
def goals_page(user_id):
    goal = get_goal_for_user(user_id)

    if request.method == 'POST':
        save_goal(
            user_id,
            request.form['weight_goal'],
            request.form['calorie_goal']
        )
        return redirect(url_for('goals_page', user_id=user_id))

    return render_template('goals.html', goal=goal, user_id=user_id)


# ---------- RUN ----------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

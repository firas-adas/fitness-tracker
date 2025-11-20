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


# ------------- PLACEHOLDERS FOR FUTURE MODELS -------------

# Goals (coming soon)
# @app.route('/goals') ...
# @app.route('/add_goal') ...

# Workouts (coming soon)
# @app.route('/workouts') ...
# @app.route('/add_workout') ...

# Body Metrics (coming soon)
# @app.route('/metrics') ...
# @app.route('/add_metric') ...

# Nutrition (coming soon)
# @app.route('/nutrition') ...
# @app.route('/add_nutrition') ...


# ---------------- MAIN ----------------

if __name__ == '__main__':
    app.run(port=8001, debug=True)

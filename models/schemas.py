class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=True)
    activity_level = db.Column(db.String(50), nullable=True)
    experience = db.Column(db.String(50), nullable=True)
    last_update = db.Column(DateTime(timezone=True), onupdate=func.now())

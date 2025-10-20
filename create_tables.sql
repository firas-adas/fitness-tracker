-- Use or create database
CREATE DATABASE IF NOT EXISTS FitnessTracker;
USE FitnessTracker;

-- User Table
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    email VARCHAR(100) UNIQUE,
    subscription_status ENUM('Active', 'Inactive') DEFAULT 'Active'
);

-- Goal Table
CREATE TABLE Goal (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    goal_type VARCHAR(50),
    target_value DECIMAL(6,2),
    start_date DATE,
    target_date DATE,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Muscle Group Lookup Table
CREATE TABLE MuscleGroup (
    muscle_group_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Equipment Lookup Table
CREATE TABLE Equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Exercise Table
CREATE TABLE Exercise (
    exercise_id INT AUTO_INCREMENT PRIMARY KEY,
    exercise_name VARCHAR(100) NOT NULL,
    muscle_group_id INT,
    equipment_id INT,
    description VARCHAR(255),
    FOREIGN KEY (muscle_group_id) REFERENCES MuscleGroup(muscle_group_id),
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id)
);

-- Workout Table
CREATE TABLE Workout (
    workout_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    workout_name VARCHAR(100),
    scheduled_datetime DATETIME,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

-- Set Log Table
CREATE TABLE WorkoutSet (
    set_id INT AUTO_INCREMENT PRIMARY KEY,
    workout_id INT,
    exercise_id INT,
    set_number INT,
    weight DECIMAL(6,2),
    reps INT,
    rpe DECIMAL(3,1),
    note VARCHAR(255),
    FOREIGN KEY (workout_id) REFERENCES Workout(workout_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Body Metric Table
CREATE TABLE BodyMetric (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    weight DECIMAL(6,2),
    height DECIMAL(5,2),
    measurement_date DATE,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Nutrition Log Table
CREATE TABLE Nutrition (
    nutrition_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    calories INT,
    protein DECIMAL(6,2),
    carbs DECIMAL(6,2),
    fat DECIMAL(6,2),
    log_datetime DATETIME,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

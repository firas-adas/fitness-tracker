-- Drop and recreate database
DROP DATABASE IF EXISTS FitnessTracker;
CREATE DATABASE FitnessTracker;
USE FitnessTracker;

-- Drop tables in reverse dependency order (safety net)
DROP TABLE IF EXISTS WorkoutSet;
DROP TABLE IF EXISTS Workout;
DROP TABLE IF EXISTS Exercise;
DROP TABLE IF EXISTS Equipment;
DROP TABLE IF EXISTS MuscleGroup;
DROP TABLE IF EXISTS Goal;
DROP TABLE IF EXISTS BodyMetric;
DROP TABLE IF EXISTS Nutrition;
DROP TABLE IF EXISTS User;

-- User Table
CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female'),
    email VARCHAR(100) NOT NULL UNIQUE,
    subscription_status ENUM('Active', 'Inactive') DEFAULT 'Active'
);

-- Goal Table
CREATE TABLE Goal (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,

    goal_name VARCHAR(100) NOT NULL,
    goal_type VARCHAR(50) NOT NULL,

    target_value DECIMAL(10,2) NOT NULL,
    starting_value DECIMAL(10,2),
    current_value DECIMAL(10,2),

    unit_of_measure VARCHAR(20) NOT NULL,

    start_date DATE NOT NULL,
    target_date DATE,

    status ENUM('in progress', 'achieved', 'abandoned') DEFAULT 'in progress',
    frequency ENUM('daily', 'weekly', 'monthly'),

    notes TEXT,
    priority_level INT,

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
    muscle_group_id INT NOT NULL,
    equipment_id INT NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (muscle_group_id) REFERENCES MuscleGroup(muscle_group_id),
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id)
);

-- Workout Table
CREATE TABLE Workout (
    workout_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    workout_name VARCHAR(100),
    scheduled_datetime DATETIME,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- Workout Set Table
CREATE TABLE WorkoutSet (
    set_id INT AUTO_INCREMENT PRIMARY KEY,
    workout_id INT NOT NULL,
    exercise_id INT NOT NULL,
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
    user_id INT NOT NULL,
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
    user_id INT NOT NULL,
    calories INT DEFAULT 0,
    protein DECIMAL(6,2) DEFAULT 0,
    carbs DECIMAL(6,2) DEFAULT 0,
    fat DECIMAL(6,2) DEFAULT 0,
    log_datetime DATETIME,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

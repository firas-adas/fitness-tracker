USE FitnessTracker;

-- Clear existing data
DELETE FROM WorkoutSet WHERE set_id > 0;
DELETE FROM Workout WHERE workout_id > 0;
DELETE FROM Exercise WHERE exercise_id > 0;
DELETE FROM Equipment WHERE equipment_id > 0;
DELETE FROM MuscleGroup WHERE muscle_group_id > 0;
DELETE FROM Goal WHERE goal_id > 0;
DELETE FROM BodyMetric WHERE metric_id > 0;
DELETE FROM Nutrition WHERE nutrition_id > 0;
DELETE FROM User WHERE user_id > 0;

-- Users
INSERT INTO User (first_name, last_name, date_of_birth, gender, email, subscription_status)
VALUES
('Alice', 'Johnson', '1990-05-12', 'Female', 'alice@email.com', 'Active'),
('Bob', 'Smith', '1985-11-03', 'Male', 'bob@email.com', 'Active'),
('Charlie', 'Lee', '2000-01-20', 'Male', 'charlie@email.com', 'Inactive');

-- Goals
INSERT INTO Goal (user_id, goal_type, target_value, start_date, target_date)
VALUES
(1, 'Weight Loss', 10.0, '2025-01-01', '2025-03-01'),
(2, 'Endurance', 5.0, '2025-02-01', '2025-04-01'),
(3, 'Strength', 15.0, '2025-01-15', '2025-05-01');

-- Muscle Groups
INSERT INTO MuscleGroup (name)
VALUES
('Full Body'), ('Chest'), ('Back'), ('Legs'), ('Shoulders'), ('Arms'), ('Triceps');

-- Equipment
INSERT INTO Equipment (name)
VALUES
('None'), ('Bodyweight'), ('Barbell'), ('Dumbbell'), ('Cable');

-- Exercises
INSERT INTO Exercise (exercise_name, muscle_group_id, equipment_id, description)
VALUES
('Running', 1, 1, NULL),
('Burpees', 1, 2, NULL),
('Barbell Bench Press', 2, 3, NULL),
('Tricep Cable Pushdowns', 7, 5, 'Cable on 6th notch, straight bar.'),
('Incline Dumbbell Press', 2, 4, NULL),
('Lat Pulldown', 3, 5, 'Use neutral grip bar.'),
('Barbell Squat', 4, 3, 'Rack set chest height.'),
('Seated Row', 3, 5, NULL),
('Dumbbell Lateral Raise', 5, 4, NULL),
('Bicep Curl', 6, 4, NULL);

-- Workouts
INSERT INTO Workout (user_id, workout_name, scheduled_datetime)
VALUES
(1, 'Push Day', '2025-10-07 07:00:00'),
(2, 'Full Body Circuit', '2025-10-07 18:00:00'),
(3, 'Leg Focus', '2025-10-08 08:30:00');

-- Workout Sets
INSERT INTO WorkoutSet (workout_id, exercise_id, set_number, weight, reps, rpe, note)
VALUES
(1, 3, 1, 135, 10, 7.5, NULL),
(1, 3, 2, 155, 8, 8.0, NULL),
(1, 4, 1, 50, 12, 7.0, 'Use rope attachment next time'),
(1, 5, 1, 40, 10, 8.0, NULL),
(2, 1, 1, 0, 20, 6.5, NULL),
(3, 7, 1, 185, 8, 7.5, 'Depth was good');

-- Body Metrics
INSERT INTO BodyMetric (user_id, weight, height, measurement_date)
VALUES
(1, 150.5, 65.0, '2025-10-01'),
(2, 180.0, 70.0, '2025-10-02'),
(3, 140.0, 62.0, '2025-10-03');

-- Nutrition Logs
INSERT INTO Nutrition (user_id, calories, protein, carbs, fat, log_datetime)
VALUES
(1, 2000, 100, 250, 70, '2025-10-05 12:30:00'),
(2, 2500, 120, 300, 80, '2025-10-05 12:15:00');

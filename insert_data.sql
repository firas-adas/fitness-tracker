USE fitnesstracker;

-- Clear existing data in FK-safe order
DELETE FROM WorkoutSet;
DELETE FROM Workout;
DELETE FROM Exercise;
DELETE FROM Equipment;
DELETE FROM MuscleGroup;
DELETE FROM Goal;
DELETE FROM BodyMetric;
DELETE FROM Nutrition;
DELETE FROM User;

-- Users (matches models/users.py + create_tables.sql)
INSERT INTO User (first_name, last_name, date_of_birth, gender, activity_level, experience, email, subscription_status)
VALUES
('Alice',   'Johnson', '1990-05-12', 'Female', 'Moderate', 'Intermediate', 'alice@email.com',   'Active'),
('Bob',     'Smith',   '1985-11-03', 'Male',   'High',     'Advanced',    'bob@email.com',     'Active'),
('Charlie', 'Lee',     '2000-01-20', 'Male',   'Low',      'Beginner',    'charlie@email.com', 'Inactive');

-- Goals (matches new Goal schema: id, user_id, weight_goal, calorie_goal)
INSERT INTO Goal (user_id, weight_goal, calorie_goal)
VALUES
(1, 140.0, 2000),
(2, 175.0, 2500),
(3, 150.0, 2200);

-- Muscle Groups
INSERT INTO MuscleGroup (name)
VALUES
('Full Body'),
('Chest'),
('Back'),
('Legs'),
('Shoulders'),
('Arms'),
('Triceps');

-- Equipment
INSERT INTO Equipment (name)
VALUES
('None'),
('Bodyweight'),
('Barbell'),
('Dumbbell'),
('Cable');

-- Exercises (matches Exercise table: exercise_name, description, muscle_group_id, equipment_id)
INSERT INTO Exercise (exercise_name, description, muscle_group_id, equipment_id)
VALUES
('Running',                   NULL, 1, 1),
('Burpees',                   NULL, 1, 2),
('Barbell Bench Press',       NULL, 2, 3),
('Tricep Cable Pushdowns',    'Cable on 6th notch, straight bar.', 7, 5),
('Incline Dumbbell Press',    NULL, 2, 4),
('Lat Pulldown',              'Use neutral grip bar.', 3, 5),
('Barbell Squat',             'Rack set chest height.', 4, 3),
('Seated Row',                NULL, 3, 5),
('Dumbbell Lateral Raise',    NULL, 5, 4),
('Bicep Curl',                NULL, 6, 4);

-- Workouts (matches models/workouts.py: workout_type, duration, calories_burned, workout_date)
INSERT INTO Workout (user_id, workout_type, duration, calories_burned, workout_date)
VALUES
(1, 'Push Day',          60,  450, '2025-10-07'),
(2, 'Full Body Circuit', 45,  400, '2025-10-07'),
(3, 'Leg Focus',         70,  500, '2025-10-08');

-- Workout Sets (matches WorkoutSet schema)
INSERT INTO WorkoutSet (workout_id, exercise_id, set_number, weight, reps, rpe, note)
VALUES
(1, 3, 1, 135, 10, 7.5, NULL),
(1, 3, 2, 155,  8, 8.0, NULL),
(1, 4, 1,  50, 12, 7.0, 'Use rope attachment next time'),
(1, 5, 1,  40, 10, 8.0, NULL),
(2, 1, 1,   0, 20, 6.5, NULL),
(3, 7, 1, 185,  8, 7.5, 'Depth was good');

-- Body Metrics
INSERT INTO BodyMetric (user_id, weight, height, measurement_date)
VALUES
(1, 150.5, 65.0, '2025-10-01'),
(2, 180.0, 70.0, '2025-10-02'),
(3, 140.0, 62.0, '2025-10-03');

-- Nutrition Logs (matches Nutrition.log_date as DATE)
INSERT INTO Nutrition (user_id, calories, protein, carbs, fat, log_date)
VALUES
(1, 2000, 100, 250, 70, '2025-10-05'),
(2, 2500, 120, 300, 80, '2025-10-05');

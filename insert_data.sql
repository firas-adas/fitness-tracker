-- Insert Users
INSERT INTO User (first_name, last_name, date_of_birth, gender, email, subscription_status)
VALUES 
('Alice', 'Johnson', '1990-05-12', 'Female', 'alice@email.com', 'Active'),
('Bob', 'Smith', '1985-11-03', 'Male', 'bob@email.com', 'Active'),
('Charlie', 'Lee', '2000-01-20', 'Male', 'charlie@email.com', 'Inactive');

-- Insert Goals
INSERT INTO Goal (user_id, goal_type, target_value, start_date, target_date)
VALUES 
(1, 'Weight Loss', 10.0, '2025-01-01', '2025-03-01'),
(2, 'Endurance', 5.0, '2025-02-01', '2025-04-01'),
(3, 'Strength', 15.0, '2025-01-15', '2025-05-01');

-- Insert Workouts
INSERT INTO Workout (user_id, workout_name, scheduled_datetime)
VALUES
(1, 'Morning Run', '2025-10-07 07:00:00'),
(2, 'HIIT Session', '2025-10-07 18:00:00'),
(3, 'Weight Training', '2025-10-08 08:30:00');

-- Insert Body Metrics
INSERT INTO BodyMetric (user_id, weight, height, measurement_date)
VALUES
(1, 150.5, 65.0, '2025-10-01'),
(2, 180.0, 70.0, '2025-10-02'),
(3, 140.0, 62.0, '2025-10-03');

-- Insert Nutrition Logs
INSERT INTO Nutrition (user_id, calories, protein, carbs, fat, log_date)
VALUES
(1, 2000, 100, 250, 70, '2025-10-05'),
(2, 2500, 120, 300, 80, '2025-10-05'),
(3, 1800, 80, 200, 60, '2025-10-05');

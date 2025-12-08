
USE FitnessTracker;

-- Show all users who currently have an active subscription.
SELECT 
    user_id,
    first_name,
    last_name,
    email,
    subscription_status
FROM User
WHERE subscription_status = 'Active';

-- Show each user's average calorie intake from their nutrition logs.
SELECT 
    n.user_id,
    CONCAT(u.first_name, ' ', u.last_name) AS full_name,
    ROUND(AVG(n.calories), 2) AS avg_daily_calories
FROM Nutrition n
JOIN User u ON n.user_id = u.user_id
GROUP BY n.user_id
ORDER BY avg_daily_calories DESC;

-- List all users along with their current goals and target dates.
SELECT 
    u.first_name,
    u.last_name,
    g.goal_type,
    g.target_value,
    g.start_date,
    g.target_date
FROM User u
INNER JOIN Goal g ON u.user_id = g.user_id
ORDER BY g.target_date ASC;

-- Find the total number of workouts each user has completed.
SELECT 
    u.user_id,
    CONCAT(u.first_name, ' ', u.last_name) AS full_name,
    COUNT(w.workout_id) AS total_workouts
FROM User u
LEFT JOIN Workout w ON u.user_id = w.user_id
GROUP BY u.user_id
ORDER BY total_workouts DESC;


-- Calculate each user's average weight based on body metric records.
SELECT 
    u.user_id,
    CONCAT(u.first_name, ' ', u.last_name) AS full_name,
    ROUND(AVG(b.weight), 2) AS avg_weight
FROM BodyMetric b
JOIN User u ON b.user_id = u.user_id
GROUP BY u.user_id
ORDER BY avg_weight ASC;


-- Show each user's workout details, including exercises and equipment used.
SELECT 
    CONCAT(u.first_name, ' ', u.last_name) AS full_name,
    w.workout_name,
    e.exercise_name,
    eq.name AS equipment_used,
    ws.weight,
    ws.reps,
    ws.rpe
FROM User u
JOIN Workout w ON u.user_id = w.user_id
JOIN WorkoutSet ws ON w.workout_id = ws.workout_id
JOIN Exercise e ON ws.exercise_id = e.exercise_id
LEFT JOIN Equipment eq ON e.equipment_id = eq.equipment_id
ORDER BY u.user_id, w.workout_name;


-- Find users who logged nutrition entries but have not recorded any workouts.
SELECT 
    u.user_id,
    CONCAT(u.first_name, ' ', u.last_name) AS full_name
FROM User u
WHERE EXISTS (SELECT 1 FROM Nutrition n WHERE n.user_id = u.user_id)
  AND NOT EXISTS (SELECT 1 FROM Workout w WHERE w.user_id = u.user_id);



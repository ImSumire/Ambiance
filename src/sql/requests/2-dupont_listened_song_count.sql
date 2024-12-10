SELECT COUNT(song)
FROM activity
JOIN user ON user.id = activity.user
WHERE last_name = "Dupont";

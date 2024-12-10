SELECT COUNT(song_id)
FROM activity
JOIN user ON user.id = activity.user_id
WHERE user.last_name = 'Dupont';

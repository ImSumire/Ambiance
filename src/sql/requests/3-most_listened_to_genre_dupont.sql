SELECT genre.name, COUNT(activity.id)
FROM user
JOIN activity ON user.id = activity.user
JOIN song ON activity.song = song.id
JOIN genre ON song.genre = genre.id
WHERE user.last_name = 'Dupont'
GROUP BY genre.name
ORDER BY COUNT(activity.id) DESC
LIMIT 1;

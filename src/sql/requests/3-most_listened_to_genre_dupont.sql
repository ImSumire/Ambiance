SELECT genre.name, COUNT(activity.id)
FROM user
JOIN activity ON user.id = activity.user_id
JOIN song ON activity.song_id = song.id
JOIN genre ON song.genre_id = genre.id
WHERE user.last_name = 'Dupont'
GROUP BY genre.name
ORDER BY COUNT(activity.id) DESC
LIMIT 1;

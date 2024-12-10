SELECT song.title
FROM song
JOIN genre ON song.genre_id = genre.id
JOIN activity ON song.id = activity.song_id
JOIN user ON activity.user_id = user.id
WHERE user.id <> (
    SELECT id
    FROM user
    WHERE last_name = 'Dupont'
)
AND genre.id NOT IN (
    SELECT DISTINCT song.genre_id
    FROM song
    JOIN activity ON song.id = activity.song_id
    JOIN user ON activity.user_id = user.id
    WHERE user.last_name = 'Dupont'
    AND activity.elapsed < 100
)
GROUP BY song.id
ORDER BY COUNT(activity.id) DESC;

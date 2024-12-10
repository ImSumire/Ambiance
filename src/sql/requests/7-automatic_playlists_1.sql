SELECT song.title
FROM song
JOIN genre ON song.genre_id = genre.id
WHERE genre.name = (
    SELECT genre.name
    FROM song
    JOIN genre ON song.genre_id = genre.id
    JOIN activity ON song.id = activity.song_id
    JOIN user ON activity.user_id = user.id
    WHERE user.last_name = 'Dupont'
    GROUP BY genre.name
    ORDER BY COUNT(activity.id) DESC
    LIMIT 1
)
AND song.id NOT IN (
    SELECT song.id
    FROM song
    JOIN activity ON song.id = activity.song_id
    JOIN user ON activity.user_id = user.id
    WHERE user.last_name = 'Dupont'
    AND activity.elapsed = 100
)
ORDER BY song.title;


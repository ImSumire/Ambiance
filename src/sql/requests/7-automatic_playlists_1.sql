SELECT song.title
FROM song
JOIN genre ON song.genre = genre.id
WHERE genre.name = (
    SELECT genre.name
    FROM song
    JOIN genre ON song.genre = genre.id
    JOIN activity ON song.id = activity.song
    JOIN user ON activity.user = user.id
    WHERE user.last_name = 'Dupond'
    GROUP BY genre.name
    ORDER BY COUNT(activity.id) DESC
    LIMIT 1
)
AND song.id NOT IN (
    SELECT song.id
    FROM song
    JOIN activity ON song.id = activity.song
    JOIN user ON activity.user = user.id
    WHERE user.last_name = 'Dupond'
    AND activity.elapsed = 100
)
ORDER BY song.title;


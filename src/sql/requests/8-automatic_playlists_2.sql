SELECT song.title
FROM song
JOIN genre ON song.genre = genre.id
JOIN activity ON song.id = activity.song
JOIN user ON activity.user = user.id
WHERE genre.name = (
    SELECT genre.name
    FROM song
    JOIN genre ON song.genre = genre.id
    JOIN activity ON song.id = activity.song
    JOIN user ON activity.user = user.id
    WHERE user.last_name = 'Dupont'
    GROUP BY genre.name
    ORDER BY COUNT(activity.id) DESC
    LIMIT 1
)
AND user.last_name <> 'Dupont'
GROUP BY song.id
ORDER BY COUNT(activity.id) DESC;

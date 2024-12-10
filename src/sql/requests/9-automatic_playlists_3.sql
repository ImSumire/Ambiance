SELECT song.title
FROM song
JOIN activity ON song.id = activity.song
JOIN user ON activity.user = user.id
WHERE user.id <> (
    SELECT id
    FROM user
    WHERE last_name = 'Dupont'
)
AND ABS((julianday(user.birth) - julianday((SELECT birth FROM user WHERE last_name = 'Dupont'))) / 365) <= 5
GROUP BY song.id
ORDER BY COUNT(activity.id) DESC;

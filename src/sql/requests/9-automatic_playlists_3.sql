SELECT song.title
FROM song
JOIN activity ON song.id = activity.song_id
JOIN user ON activity.user_id = user.id
WHERE user.id <> (
    SELECT id
    FROM user
    WHERE last_name = 'Dupont'
)
AND ABS((julianday(user.birth_date) - julianday((SELECT birth_date FROM user WHERE last_name = 'Dupont'))) / 365) <= 5
GROUP BY song.id
ORDER BY COUNT(activity.id) DESC;

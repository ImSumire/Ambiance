SELECT AVG(song.length * (activity.elapsed / 100))
FROM activity
JOIN song ON activity.song_id = song.id;

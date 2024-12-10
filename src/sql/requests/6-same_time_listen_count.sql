SELECT COUNT(*)
FROM (
    SELECT contract.id, activity.start, COUNT(DISTINCT user.id)
    FROM activity
    JOIN user ON activity.user = user.id
    JOIN contract ON user.contract = contract.id
    WHERE DATE(activity.start) = '2024-10-14'
    GROUP BY contract.id, activity.start
    HAVING COUNT(DISTINCT user.id) > 1
);

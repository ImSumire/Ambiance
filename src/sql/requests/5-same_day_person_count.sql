SELECT MAX(person_count)
FROM (
    SELECT contract.id, DATE(activity.start), COUNT(DISTINCT user.id) AS person_count
    FROM activity
    JOIN user ON activity.user = user.id
    JOIN contract ON user.contract = contract.id
    GROUP BY contract.id, DATE(activity.start)
);


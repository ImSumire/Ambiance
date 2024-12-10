SELECT COUNT(*)
FROM (
    SELECT contract.id, activity.start_date, COUNT(DISTINCT user.id)
    FROM activity
    JOIN user ON activity.user_id = user.id
    JOIN contract ON user.contract_id = contract.id
    WHERE DATE(activity.start_date) = '2024-10-14'
    GROUP BY contract.id, activity.start_date
    HAVING COUNT(DISTINCT user.id) > 1
);

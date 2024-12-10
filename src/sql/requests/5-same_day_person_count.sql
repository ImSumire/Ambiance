SELECT MAX(person_count)
FROM (
    SELECT contract.id, DATE(activity.start_date), COUNT(DISTINCT user.id) AS person_count
    FROM activity
    JOIN user ON activity.user_id = user.id
    JOIN contract ON user.contract_id = contract.id
    GROUP BY contract.id, DATE(activity.start_date)
);


# Write your MySQL query statement below
SELECT machine_id,
    ROUND(SUM(IF(activity_type = 'start', -1, 1) * timestamp) / COUNT(DISTINCT process_id), 3) AS processing_time
FROM Activity
GROUP BY machine_id;



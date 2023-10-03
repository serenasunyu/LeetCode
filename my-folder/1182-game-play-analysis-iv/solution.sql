# Write your MySQL query statement below

/*
SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
IN (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id);
*/

WITH firstLoginDate AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(DISTINCT fld.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM firstLoginDate fld
JOIN Activity a
ON fld.player_id = a.player_id AND datediff(a.event_date, fld.first_login_date) = 1;

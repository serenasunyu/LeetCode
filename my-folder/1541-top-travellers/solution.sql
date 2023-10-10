# Write your MySQL query statement below
SELECT name, 
 SUM(
   CASE WHEN u.id = r.user_id THEN distance 
   ELSE 0
   END) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, name ASC;

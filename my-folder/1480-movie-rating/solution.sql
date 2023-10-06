# Write your MySQL query statement below

(SELECT name AS results 
FROM Users u
JOIN MovieRating mr ON u.user_id = mr.user_id
GROUP BY name
ORDER BY COUNT(rating) DESC, name
LIMIT 1)

UNION ALL

(SELECT title AS results
FROM Movies m
JOIN MovieRating mr ON m.movie_id = mr.movie_id
WHERE DATE_FORMAT(created_at,'%Y-%m') = '2020-02'
GROUP BY title
ORDER BY AVG(rating) DESC, title
LIMIT 1)


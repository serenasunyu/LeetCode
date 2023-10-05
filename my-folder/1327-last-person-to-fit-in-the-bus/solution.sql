# Write your MySQL query statement below
/*
SELECT q1.person_name
FROM Queue q1
JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1;
*/

select person_name
from
  (SELECT *,
    SUM(weight) OVER (ORDER BY turn)
    AS tot
  FROM queue) t
where tot <= 1000
order by tot desc
limit 1;


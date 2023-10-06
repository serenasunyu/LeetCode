# Write your MySQL query statement below
/*
SELECT id,
    CASE
        WHEN id % 2 = 0 THEN (lag(student) OVER(ORDER BY id))
        ELSE IFNULL(LEAD(student) OVER(ORDER BY id), student)
    END AS 'student'
FROM Seat;
*/

SELECT CASE
           WHEN s.id % 2 <> 0 AND s.id = (SELECT COUNT(*) FROM Seat) THEN s.id
           WHEN s.id % 2 = 0 THEN s.id - 1
           ELSE
               s.id + 1
           END AS id,
       student
FROM Seat AS s
ORDER BY id;


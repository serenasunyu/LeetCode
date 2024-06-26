# Write your MySQL query statement below
WITH cte AS (
  SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary, DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS ranking
FROM Employee e
JOIN Department d
ON e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM cte
WHERE ranking BETWEEN 1 AND 3;


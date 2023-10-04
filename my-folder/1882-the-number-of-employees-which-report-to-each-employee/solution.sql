# Write your MySQL query statement below
/*
SELECT e.employee_id, e.name, COUNT(m.employee_id) AS reports_count, ROUND(AVG(m.age)) AS average_age
FROM Employees e, Employees m
WHERE e.employee_id = m.reports_to
GROUP BY e.employee_id, e.name
HAVING reports_count > 0
ORDER BY e.employee_id;
*/

SELECT e.employee_id, e.name, (SELECT COUNT(m.employee_id) FROM Employees m WHERE m.reports_to = e.employee_id) AS reports_count, (SELECT ROUND(AVG(m.age)) FROM Employees m WHERE m.reports_to = e.employee_id) AS average_age
FROM Employees e
HAVING reports_count > 0
ORDER BY e.employee_id;

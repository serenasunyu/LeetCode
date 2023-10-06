# Write your MySQL query statement below

SELECT employee_id
FROM Employees
WHERE salary < 30000 AND manager_id NOT IN (
    SELECT e2.employee_id
    FROM Employees e2
)
ORDER BY employee_id;

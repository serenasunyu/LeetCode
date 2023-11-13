# Write your MySQL query statement below
SELECT DISTINCT c.customer_id
FROM Customer c
GROUP BY customer_id
HAVING COUNT(DISTINCT c.product_key) = (SELECT COUNT(*) FROM Product);


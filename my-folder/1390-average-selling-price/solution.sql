# Write your MySQL query statement below
SELECT p.product_id, COALESCE(ROUND(SUM(p.price * us.units) / SUM(us.units), 2), 0) AS average_price 
FROM Prices p
LEFT JOIN UnitsSold us ON p.product_id = us.product_id
WHERE (us.purchase_date BETWEEN p.start_date AND p.end_date) OR us.product_id IS NULL
GROUP BY p.product_id;


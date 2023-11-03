# Write your MySQL query statement below
SELECT p.product_id, 
  CASE 
    WHEN SUM(us.units) <> 0
    THEN ROUND(COALESCE(SUM(p.price * us.units) / SUM(us.units), 0), 2) 
    ELSE 0 
  END AS average_price
FROM Prices p
LEFT JOIN UnitsSold us
ON p.product_id = us.product_id
WHERE us.purchase_date >= p.start_date AND us.purchase_date <= p.end_date OR us.product_id IS NULL
GROUP BY p.product_id;



# Write your MySQL query statement below
/*
WITH rk AS (
    SELECT DISTINCT product_id, new_price As price,
        RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS rk
    FROM Products p
    WHERE change_date <= '2019-08-16'
)

SELECT product_id, price
FROM rk
WHERE rk = 1

UNION

SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (
    SELECT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
);
*/

SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (
    SELECT DISTINCT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
    )
UNION

SELECT DISTINCT product_id, new_price AS price
FROM Products
WHERE (product_id, change_date) IN (
    SELECT product_id, MAX(change_date) AS date 
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
    )

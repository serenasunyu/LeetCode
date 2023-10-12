# Write your MySQL query statement below
/*
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
) AND (lat, lon) IN (
    SELECT lat, lon 
    FROM Insurance
    GROUP BY lat, lon 
    HAVING COUNT(*) = 1
);
*/

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT tiv_2016,
           COUNT(*) OVER (PARTITION BY tiv_2015) AS cnt_tiv_2015,
           COUNT(*) OVER (PARTITION BY lat, lon) AS cnt_lat_lon
    FROM insurance
) AS subquery
WHERE cnt_tiv_2015 > 1 AND cnt_lat_lon = 1;

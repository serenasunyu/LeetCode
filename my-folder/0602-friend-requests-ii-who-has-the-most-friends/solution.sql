# Write your MySQL query statement below
/*
SELECT accepter_id AS id, 
    (SELECT COUNT(*) 
    FROM RequestAccepted 
    WHERE (requester_id = id or accepter_id = id))AS num
FROM RequestAccepted
GROUP BY accepter_id

UNION

SELECT requester_id AS id, 
    (SELECT COUNT(*) 
    FROM RequestAccepted 
    WHERE (requester_id = id or accepter_id = id))AS num
FROM RequestAccepted
GROUP BY requester_id
ORDER BY num DESC
LIMIT 1;
*/

WITH base AS (
  SELECT requester_id AS id
  FROM RequestAccepted

  UNION ALL

  SELECT accepter_id AS id
  FROM RequestAccepted
)

SELECT id, COUNT(*) AS num
FROM base
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

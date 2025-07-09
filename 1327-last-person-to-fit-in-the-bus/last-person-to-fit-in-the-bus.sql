# Write your MySQL query statement below
WITH bus AS (SELECT person_name, turn, SUM(weight) OVER(ORDER BY turn) AS total_weight FROM queue)
SELECT person_name FROM bus WHERE total_weight <= 1000 ORDER BY total_weight DESC LIMIT 1;
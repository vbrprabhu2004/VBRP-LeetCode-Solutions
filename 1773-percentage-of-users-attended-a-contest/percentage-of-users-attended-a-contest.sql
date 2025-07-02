# Write your MySQL query statement below
select R.contest_id, 
round(COUNT(*)/(select count(*) from Users)*100,2) as percentage
from Register R
group by R.contest_id
order by round(COUNT(*)/(select count(*) from Users)*100,2) desc,
contest_id
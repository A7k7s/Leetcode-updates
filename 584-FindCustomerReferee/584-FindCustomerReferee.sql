-- Last updated: 7/14/2026, 2:02:10 PM
# Write your MySQL query statement below
select name
from Customer
where referee_id!=2 or referee_id is null;
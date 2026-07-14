-- Last updated: 7/14/2026, 2:02:04 PM
# Write your MySQL query statement below
select name,population,area
from World
where population>=25000000 || area>=3000000;
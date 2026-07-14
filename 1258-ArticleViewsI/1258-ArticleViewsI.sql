-- Last updated: 7/14/2026, 2:01:31 PM
# Write your MySQL query statement below
select distinct author_id as id
from Views
where author_id=viewer_id
order by id;
-- Last updated: 7/14/2026, 2:01:24 PM
# Write your MySQL query statement below
select eu.unique_id,e.name
from Employees e
left join EmployeeUNI eu on e.id=eu.id;
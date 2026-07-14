-- Last updated: 7/14/2026, 2:01:34 PM
# Write your MySQL query statement below
select pt.product_name,st.year,st.price
from Sales st
join product pt on st.product_id=pt.product_id;
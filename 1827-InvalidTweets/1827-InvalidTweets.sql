-- Last updated: 7/14/2026, 2:01:19 PM
# Write your MySQL query statement below
select tweet_id
from Tweets
where char_length(content)>15;
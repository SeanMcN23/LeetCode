# Write your MySQL query statement below
select email as Email 
from Person p1
group by email
having COUNT(email) > 1
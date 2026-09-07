# Write your MySQL query statement below


select e1.name from Employee as e1 inner join Employee as e2 on e2.managerId = e1.id group by e2.managerId having COUNT(e2.managerId) >= 5
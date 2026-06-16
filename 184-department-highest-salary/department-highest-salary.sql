# Write your MySQL query statement below
select d1.name as Department, e1.name as Employee, e1.salary as Salary from Employee e1 
join Department d1 on e1.departmentId=d1.id
# need to match the department id and salary pair from OG table

# this will basically aggregate together the departments, then choose from there the max salary that it finds. then we can display it

where (e1.departmentId,e1.salary) in
( select departmentId,
    max(salary) as Max_salary
    from Employee
    group by departmentId

);

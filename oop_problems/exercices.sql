SELECT * FROM employees

SELECT name, department FROM employees WHERE department="HR"

SELECT name, salary FROM employees ORDER by salary DESC

SELECT Count(*) as total_employees from employees

select department, sum(salary) as total_salary
from employees group by department

SELECT department, SUM(salary) AS total_salary
FROM Employees
GROUP BY department
HAVING SUM(salary) > 100000;
# Having goes wirh groups ( groupping )



SELECT Employees.name, Departments.department_name FROM employees JOIN Departments
on employees.department_id == Departments.department_id


SELECT A.name as employee1, B.name as employee2 FROM Employee A JOIN Employee B 
ON A.department_id = B.department_id WHERE A.id != B.id


SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)

SELECT name, 
       (SELECT COUNT(*) 
        FROM Employees E 
        WHERE E.department_id = Employees.department_id) AS total_department_employees
FROM Employees;


SELECT MAX(salary) as second_salary FROM Employees 
WHERE salary < (SELECT MAX(salary) FROM Employees)


SELECT product_id, customer_id, COUNT(*)
From ORDER
group by product_id, customer_id 
HAVING count(*) > 1


######################################################################
Exercices :

'1 - Find the name of the customer who has placed the highest number of orders in the system. If there is a tie, return all such customers.'

My answer
SELECT C.customer_name, Count(*) as nb_orders FROM Customers C JOIN Orders O 
ON C.customer_id = O.customer_id 
WHERE nb_orders >= ( SELECT MAX(Count(*)) FROM Customers C JOIN Orders O ON  C.customer_id = O.customer_id GROUP BY  C.customer_id)

''' You cant use aliases in WHERE clause because they are not resolved yet.
You cant use MAX on Count directly
'''

Correction 
SELECT C.customer_name, COUNT(*) as nb_orders FROM Customers C JOIN Orders O ON C.customer_id = O.customer_id
GROUP BY C.customer_id, C.customer_name
HAVING COUNT(*) = (
    SELECT MAX(order_count) FROM (
        SELECT Count(*) as order_count
        FROM OrdersGROUP BY customer_id
    )
)


'2 - Find the names of employees who work in a department located in the same city as their manager.'

SELECT E.name, E.manager_id FROM Employees E JOIN Departments D JOIN Locations L
ON E.department_id = D.department_id AND D.location_id = L.location_id
WHERE L.city = ( SELECT )
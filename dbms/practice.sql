CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    department TEXT
);

INSERT INTO employees VALUES
(1, 'Yash', 40000, 'IT'),
(2, 'Rahul', 50000, 'HR'),
(3, 'Priya', 60000, 'IT');

SELECT * FROM employees;

SELECT * FROM employees WHERE department = 'IT';


SELECT department, AVG(salary) FROM employees GROUP BY department;

SELECT department, MAX(salary) AS max_salary
FROM employees
GROUP BY department;

-- second highest salary
-- max salary
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);


CREATE TABLE dept (dept_id INT PRIMARY KEY, dept_name VARCHAR(50));
INSERT INTO dept VALUES (1,'IT'), (2,'HR'), (3,'Finance');

CREATE TABLE emp (emp_id INT PRIMARY KEY, name VARCHAR(50), dept_id INT);
INSERT INTO emp VALUES (1,'Yash',1), (2,'Rahul',2), (3,'Priya',1), (4,'Amit',NULL);


SELECT e.name, d.dept_name
FROM emp e
INNER JOIN dept d ON e.dept_id = d.dept_id;


SELECT e.name, d.dept_name
FROM emp e
LEFT JOIN dept d ON e.dept_id = d.dept_id;

SELECT e.name, d.dept_name
FROM emp e
RIGHT JOIN dept d ON e.dept_id = d.dept_id;

SELECT e.name, d.dept_name
FROM emp e LEFT JOIN dept d ON e.dept_id = d.dept_id
UNION
SELECT e.name, d.dept_name
FROM emp e RIGHT JOIN dept d ON e.dept_id = d.dept_id;
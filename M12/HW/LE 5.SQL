--1.CREATE THE TABLE
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);
--2.INSERT INITIAL DATA
INSERT INTO employees (employee_id, first_name, last_name, department, salary, hire_date) VALUES
(1, 'Alice', 'Smith', 'HR', 55000.00, '2022-03-15'),
(2, 'Bob', 'Johnson', 'IT', 75000.00, '2021-06-20'),
(3, 'Charlie', 'Brown', 'IT', 80000.00, '2020-01-10'),
(4, 'Diana', 'Prince', 'Marketing', 62000.00, '2023-11-01'),
(5, 'Evan', 'Wright', 'HR', 48000.00, '2024-02-15');

--3.MANIPULATE DATA (UPDATE)
-- Give Alice a raise
UPDATE employees
SET salary = 58000.00
WHERE employee_id = 1;

--4.FILTER AND SORT DATA (ANALYSE)
-- Find employees in IT or Marketing making over 60,000, sorted highest to lowest
SELECT first_name, last_name, department, salary
FROM employees
WHERE salary > 60000 
  AND department IN ('IT', 'Marketing')
ORDER BY salary DESC;
--Create the DEPARTMENT table if it does not exist
CREATE TABLE IF NOT EXISTS DEPARTMENT (
  EMPLOYESS_ID TEXT,
  NAME TEXT,
  DEPARTMENT_ID TEXT,
  MANAGER_ID TEXT,
  SALARY REAL
);

INSERT INTO DEPARTMENT(EMPLOYESS_ID,NAME,DEPARTMENT_ID,MANAGER_ID,SALARY)VALUES
('100', 'STEVEN KING', '90', '100', 2400000),
('101', 'NEENA KOCCHAR', '90', '100', 1700000),
('102', 'LEX DEHAAN', '90', '102', 900000),
('103', 'BRUCE LEE', '60', '103', 480000),
('104', 'DIANA WILLS', '60', '103', 250000),
('105', 'VALLI PATOR', '50', '100', 420000),
('1973', 'LUV HAMI', '60', '102', 5000000),
('106', 'DAVID AUSTIN', '90', '100', 600000);

SELECT * FROM DEPARTMENT;

--Query to count the number of employess in each department
SELECT department_id AS "Department Code",
COUNT(*)AS "No of Employees"
FROM DEPARTMENT
GROUP BY department_id;

--Query to sum the salary of each department
SELECT department_id,SUM(salary)
FROM DEPARTMENT
GROUP BY deparTment_id;

--Query to count the number of employees and sum the salary in each department
SELECT department_id AS "Department code",
COUNT(*) AS "No of Employees",
SUM(salary)AS"Total Salary"
FROM DEPARTMENT 
GROUP BY department_id;

--Query to sum the salary of employess with a spesific manager
SELECT department_id AS "Department Code",
SUM(SALARY)AS "total Salary"
FROM DEPARTMENT
WHERE MANAGER_ID = '103'
GROUP BY department_id;

--Query to find department with more then 2 employees
SELECT department_id,COUNT(*) AS "No . of Employees"
FROM DEPARTMENT
GROUP BY department_id
HAVING COUNT(*) > 2;
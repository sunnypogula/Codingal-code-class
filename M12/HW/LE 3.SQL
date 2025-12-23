-- 1. Create the Employee table
CREATE TABLE EMPLOYEE (
    EMP_ID TEXT PRIMARY KEY,
    EMP_NAME TEXT,
    ROLE TEXT,
    SALARY REAL
);

-- 2. Insert sample data to help Tarun identify employees
INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME, ROLE, SALARY) VALUES
('E01', 'John Doe', 'Manager', 50000),
('E02', 'Jane Smith', 'Developer', 45000),
('E03', 'Robert Brown', 'Analyst', 38000);

-- 3. Fetch all records to display on screen
SELECT * FROM EMPLOYEE;
-- Calculate sum, average, count, minimum, and maximum salary
SELECT 
    SUM(SALARY) AS Total_Payroll,
    AVG(SALARY) AS Average_Salary,
    COUNT(DISTINCT ROLE) AS Total_Departments,
    MIN(SALARY) AS Lowest_Salary,
    MAX(SALARY) AS Highest_Salary
FROM EMPLOYEE;
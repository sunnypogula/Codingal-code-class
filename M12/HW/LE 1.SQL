-- Create the table for Tarun's company (DXC Company)
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    EMP_ID TEXT PRIMARY KEY,
    EMP_NAME TEXT,
    ROLE TEXT,
    SALARY REAL
);

-- Insert sample records
INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME, ROLE, SALARY) VALUES
('E001', 'John Doe', 'Manager', 55000),
('E002', 'Jane Smith', 'Developer', 48000),
('E003', 'Robert Brown', 'Clerk', 25000);

-- Fetch all details to help Tarun identify employees
SELECT * FROM EMPLOYEE;
WHERE EMP_NAME = 'John doe';
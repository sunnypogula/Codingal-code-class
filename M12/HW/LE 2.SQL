-- Create the table
CREATE TABLE IF NOT EXISTS CUSTOMER (
    cust_id INTEGER PRIMARY KEY,
    cust_name TEXT,
    city TEXT,
    grade INTEGER
);

-- Insert sample data
INSERT INTO CUSTOMER (cust_id, cust_name, city, grade) VALUES
(1, 'Alice', 'New York', 150),
(2, 'Bob', 'London', 200),
(3, 'Charlie', 'New York', 80),
(4, 'David', 'Paris', 50);

-- Run your queries here!
SELECT * FROM CUSTOMER 
WHERE city = 'New York' OR grade > 100;

SELECT * FROM CUSTOMER 
WHERE city = 'New York' AND grade > 100;

-- 1. CREATE THE CUSTOMERS & EXPORTS TABLE
CREATE TABLE company_records (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    export_country VARCHAR(50),
    order_amount DECIMAL(10, 2)
);

-- 2. INSERT SAMPLE DATA FOR HARISH'S COMPANY
INSERT INTO company_records (customer_id, customer_name, product_name, export_country, order_amount) VALUES
(1, 'Aaron Miller', 'Solar Panels', 'Germany', 15000.00),
(2, 'Jordan Taylor', 'Wind Turbines', 'Canada', 22000.00),
(3, 'Amanda Ross', 'Electric Motors', 'Germany', 8500.00),
(4, 'George Brooks', 'Microchips', 'Japan', 31000.00),
(5, 'Alice Morgan', 'LED Systems', 'Canada', 12500.00),
(6, 'Robert Fox', 'Solar Panels', 'Brazil', 18000.00);


-- 3. QUERY 1: Find customers whose name starts with "a" (Case-Insensitive check)
-- The '%' wildcard matches any characters following the 'a'
SELECT customer_name, product_name, export_country 
FROM company_records
WHERE customer_name LIKE 'a%';


-- 4. QUERY 2: Find customers whose name contains "or" anywhere
-- The '%' wildcards on both sides mean 'or' can be at the beginning, middle, or end
SELECT customer_name, product_name, export_country
FROM company_records
WHERE customer_name LIKE '%or%';


-- 5. QUERY 3: Find all unique countries where products are exported
-- The DISTINCT keyword eliminates duplicate country entries from the list
SELECT DISTINCT export_country 
FROM company_records
ORDER BY export_country ASC;
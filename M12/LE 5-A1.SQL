--Create the salesman table if it doed not exist
CREATE TABLE IF NOT EXISTS Salesman(
   Salesman_id TEXT PRIMARY KEY,
   name TEXT,
   city TEXT,
   Comission REAL
);
--Insert sample data into the Salesman table
INSERT INTO Salesman(Salesman_id,name,city,Comission)VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5002', 'Nail Knite', 'Paris', 0.13),
('5005', 'Pit Alex', 'London', 0.11),
('5006', 'Mc Lyon', 'Paris', 0.14),
('5007', 'Paul Adam', 'Rome', 0.13),
('5003', 'Lauson Hen', 'San Jose', 0.12);

--Create the Customer table if it does not exist
CREATE TABLE IF NOT EXISTS Customer(
 customer_id TEXT,
 cust_name TEXT PRIMARY KEY,
 city TEXT,
 Salesman_id TEXT,
 FOREIGN KEY (Salesman_id)REFERNCES Salesman(Salesman_id)
);

--INSERT SAMPLE DATA INTO THE CUSTOMER TABLE
INSERT INTO Customer (customer_id,cust_name,city,grade,Salesman_id)VALUES
('3002', 'nick rimando', 'New York', 100, '5001'),
('3007', 'brad davis', 'New York', 200, '5001'),
('3005', 'graham zusi', 'California', 200, '5002'),
('3008', 'julian green', 'London', 300, '5004'),
('3004', 'fabian johnson', 'Paris', 300, '5006'),
('3009', 'geoff cameron', 'Berlin', 100, '5003'),
('3003', 'jozy altidor', 'Moscow', 200, '5007'),
('3001', 'brad guzan', 'London', NULL, '5005');

--CREATE THE ORDERA TABLE IF IT DOES NOT EXIST
CREATE TABLE IF NOT EXISTS Orders(
  ord_no TEXT PRIMARY KEY,
  purch_amt REAL,
  customer_id TEXT,
  Salesman_id TEXT,
  FOREIGN KEY (customer_id)REFERNCES Customer(customer_id),
  FOREIGN KEY(Salesman_id)REFERNCES Salesman(Salesman_id)
);

--INSERT SAMPLE DATA INTO THE ORDERS TABLE
INSERT INTO Orders(ord_no,purch_amt,ord_data,cusomer_id ,Salesman_id)VALUES
('70001', 150.5, '2012-10-05', '3005', '5002'),
('70009', 270.65, '2012-09-10', '3001', '5001'),
('70002', 65.26, '2012-10-05', '3002', '5003'),
('70004', 110.5, '2012-08-17', '3009', '5007'),
('70007', 948.5, '2012-09-10', '3005', '5005'),
('70005', 2400.6, '2012-07-27', '3007', '5006');

--Queries
SELECT * FROM Customer;
SELECT * FROM Salesman;
SELECT * FROM Orders

--matching customers and salesman by city
SELECT customer.cust_name,salesman.name,salesman.city
FROM Customer
JOIN Salesman ON Customer.city = Salesman.Salesman_id;

--linking customers to their salesman
SELECT Customer.cust_name,Salesman.name
FROM Customer
JOIN Salesman ON Customer.Salesman_id = Salesman.Salesman_id;

--fetching orders where customer's city does not match salesman's city
SELECT Orders.ord_no,Customer.cust_name,Orders.customer_id,Orders.Salesman_id
FROM Orders
JOIN Customer ON Orders.Customer_id = Customer.customer_id
JOIN Customer ON Orders.Salesman_id = Salesman.Salesman_id
WHERE Customer.city <> Salesman.city;

--
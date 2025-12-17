--Create the STUDENT table if it does not exist
--NOT NULL is used for NAME to ensure every student record has a name
CREATE TABLE IF NOT EXIST STUDENT(
   ROLL_NO TEXT PRIMARY KEY,
   NAME TEXT NOT NULL,
   ADDRESS TEXT,
   PHONE TEXT,
   AGE INTEDER
);

--Insert sample data into the STUDENT table
INSERT INTO STUDENT (ROLL_NO,NAME,ADDRESS,PHONE,AGE)VALUES
   ('1','RAM','DELHI','******',18),
   ('2', 'RAMESH', 'GURGAON', '*****', 18),
   ('3', 'SUJIT', 'ROHTAK', '*****', 20),
   ('4', 'SURESH', 'DELHI', '*****', 18),
   ('5', 'AMAN', 'ROHTAK', '*****', 20),
   ('6', 'HARSH', 'GURGAON', '*****', 18);
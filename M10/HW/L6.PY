import sqlite3

def list_tables(db_name):
    try:
        # 1. Establish a connection to the database
        connection = sqlite3.connect(db_name)
        
        # 2. Create a cursor object to execute SQL commands
        cursor = connection.cursor()
        
        # 3. Query the 'sqlite_master' table to find all user-defined tables
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(query)
        
        # 4. Fetch all results
        tables = cursor.fetchall()
        
        # 5. Print the results
        if tables:
            print(f"Tables found in '{db_name}':")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print("No tables found in the database.")
            
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        
    finally:
        # 6. Close the connection
        if connection:
            connection.close()

# Provide your database filename here
list_tables('my_database.db')
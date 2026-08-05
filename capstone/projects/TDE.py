import sqlite3
import pandas as pd

# 1. Connect to an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# 2. Create destination and attraction tables
conn.execute(
    """
CREATE TABLE destinations (
    dest_id INTEGER PRIMARY KEY,
    city TEXT,
    country TEXT
)
"""
)

conn.execute(
    """
CREATE TABLE attractions (
    attraction_id INTEGER PRIMARY KEY,
    dest_id INTEGER,
    attraction_name TEXT
)
"""
)

# 3. Insert sample data (including one destination without attractions and one orphan attraction)
conn.executemany(
    "INSERT INTO destinations VALUES (?, ?, ?)",
    [
        (1, "Paris", "France"),
        (2, "Tokyo", "Japan"),
        (3, "Rome", "Italy"),
    ],
)

conn.executemany(
    "INSERT INTO attractions VALUES (?, ?, ?)",
    [
        (101, 1, "Eiffel Tower"),
        (102, 1, "Louvre Museum"),
        (103, 2, "Tokyo Tower"),
        (104, 99, "Mystery Spot"),
    ],
)

# 4. INNER JOIN: Get destinations with matching attractions
query_inner = """
SELECT d.city, d.country, a.attraction_name
FROM destinations d
INNER JOIN attractions a ON d.dest_id = a.dest_id
"""

# 5. LEFT JOIN: Get all destinations, including those without attractions
query_left = """
SELECT d.city, d.country, a.attraction_name
FROM destinations d
LEFT JOIN attractions a ON d.dest_id = a.dest_id
"""

# 6. Display results using Pandas
print("--- INNER JOIN ---")
print(pd.read_sql_query(query_inner, conn))

print("\n--- LEFT JOIN ---")
print(pd.read_sql_query(query_left, conn))

conn.close()
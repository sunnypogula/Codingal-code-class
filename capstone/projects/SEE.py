import sqlite3
import pandas as pd

# 1. Connect to in-memory SQLite database
conn = sqlite3.connect(":memory:")

# 2. Create tables
conn.execute(
    """
CREATE TABLE experiments (
    id INTEGER PRIMARY KEY,
    name TEXT,
    duration_mins INTEGER
)
"""
)

conn.execute(
    """
CREATE TABLE materials (
    id INTEGER PRIMARY KEY,
    exp_id INTEGER,
    material_name TEXT
)
"""
)

# 3. Insert sample data
conn.executemany(
    "INSERT INTO experiments VALUES (?, ?, ?)",
    [
        (1, "Volcano Eruption", 30),
        (2, "Plant Growth", 120),
        (3, "Magnet Test", 15),
    ],
)

conn.executemany(
    "INSERT INTO materials VALUES (?, ?, ?)",
    [
        (101, 1, "Baking Soda"),
        (102, 1, "Vinegar"),
        (103, 2, "Soil"),
        (104, 3, "Magnet"),
    ],
)

# 4. Query using subquery and aliases to find the quickest experiment
query_quickest = """
SELECT 
    e.name AS experiment_name, 
    e.duration_mins AS duration
FROM experiments e
WHERE e.duration_mins = (SELECT MIN(duration_mins) FROM experiments)
"""

# 5. Query using subquery to find experiments matching a material
query_matching = """
SELECT 
    e.name AS experiment_name, 
    e.duration_mins AS duration
FROM experiments e
WHERE e.id IN (
    SELECT exp_id 
    FROM materials 
    WHERE material_name = 'Baking Soda'
)
"""

# 6. Display results using Pandas
print("--- Quickest Experiment ---")
print(pd.read_sql_query(query_quickest, conn))

print("\n--- Matching Experiments (Using Baking Soda) ---")
print(pd.read_sql_query(query_matching, conn))

conn.close()
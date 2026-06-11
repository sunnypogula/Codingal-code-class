#import necessary libraries
import numpy as np
import pandas as pd
import sqlite3

#setup connection with database
#and display all tables inside the database
database = 'database.sqlite'

conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type ='table'""",conn)

tables
#check how inner join works
joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_name,
                          
                          Ci.City_Name
                          FROM country c INNER JOIN city ci
                          ON c.Country_Id == ci.Country_id""",conn)
joined_city
#check how outer join works
joined_left = pd.read_sql("""SELECT *
                          FROM player
                          LEFT JOIN season
                          ON player.Player_ID ==
                          season.man_of_the_Series""",conn)
joined_left
#check how cross join works
joined_cross = pd.read_sql("""SELECT C.Country_Id,c.Country_name,
                           ci.city_Name
                           FROM country c
                           CROSS JOIN ci""",conn)
joined_cross
#check how union clause works
union = pd.read_sql("""SELECT Player_Name
                    FROM player
                    UNION
                    SELECT Team_Name
                    FROM team""",conn)
union
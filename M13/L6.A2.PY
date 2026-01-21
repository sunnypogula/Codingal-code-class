#Import necessary libraries
import pandas as pd
import sqlite3

database = 'database.sqlite'
conn =sqlite3.connect(database)

tables = pd.read_sql("""SELECT * 
FROM sqlite_master
WHERE type='table';""",conn)

print(tables)

#fetch details of all matches played by csk in year 2015
csk_matches_2015 = pd.read_sql("""SELECT Match_Id,Team_2 AS Away_Team, Toss_Winner,Match_Winner
                               FROM Match
                               WHERE Team_1 = 
                               (SELECT Team_1
                               FROM Match
                               WHERE Season_Id == 8)""",conn)

print("Matches Played By chennai super kings in year 2015")
print(csk_matches_2015)# Changed from 'csk_matches_2015' to 'print(csk_matches_2015)' for execution

# Fetch Details of all matches won by CSK in year 2015 (Query from first image)
# Note: This query assumes Team_Id 3 is CSK and Season_Id 8 is the 2015 season.
Csk_wins = pd.read_sql("""SELECT *
                       FROM Match
                       WHERE Match_winner == 3 AND Season_id == 8""",conn)

#fetch deatails of all the matches
#where batsman score more then 5 in year 2015(query from first image)
match_runs = pd.read_sql("""SELECT Match_Id,Runs_Scored AS Total_Runs,Innings_No
                         FROM Batsman_Scored
                         WHERE Total_Runs > 5 AND Match_id IN 
                         (SELECT Match_id 
                         FROM Match
                         WHERE Season_Id == 8)""",conn)

print("match with scored runs greater than 5 in year 2015")
print(match_runs)
# Fetch Details of Matches played in year 2015

# where Total Runs Scored were greater than average scored run (Query from first image)

# Note: This query calculates the average run score *across the whole Batsman_Scored table*,

# then compares it only to runs scored in Innings_No 1.
avg_runs = pd.read_sql("""SELECT Match_Id,Runs_Scored AS Total_Runs,Innings_No
                         FROM Batsman_Scored
                         WHERE Innings_No == 1 AND Runs_Scored >
                       (SELECT AVG(Runs_Scored)
                       FROM Batsman_Scored)""",conn)

print("matches with scored runs greater than average scored runs")
print(avg_runs)
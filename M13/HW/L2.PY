#Filter rows by a category/text field
SELECT player_name, position 
FROM table_name 
WHERE position = 'Guard';

Filter rows by a numerical threshold
SELECT player_name, points 
FROM table_name 
WHERE points >= 20;
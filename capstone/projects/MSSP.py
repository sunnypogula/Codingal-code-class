# 1. Store fixed student details in a tuple (Name, Grade, Roll Number)
student_info = ("Alex", 10, 101)

# Accessing tuple values
print("--- Student Information ---")
print("Name:", student_info[0])
print("Grade:", student_info[1])
print("Roll Number:", student_info[2])
print()

# 2. Create subject sets for different days
monday_subjects = {"Math", "English", "Science", "History"}
tuesday_subjects = {"Math", "Art", "Science", "Physical Education"}

print("Monday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
print()

# 3. Modify sets (add a new subject and remove an existing one)
monday_subjects.add("Computer Science")
monday_subjects.remove("History")

print("Updated Monday Subjects:", monday_subjects)
print()

# 4. Compare subjects using common set operations

# Subjects studied on BOTH days (Intersection)
common_subjects = monday_subjects.intersection(tuesday_subjects)
print("Subjects on both Monday & Tuesday:", common_subjects)

# ALL unique subjects studied across both days (Union)
all_subjects = monday_subjects.union(tuesday_subjects)
print("All unique subjects studied:", all_subjects)

# Subjects studied ONLY on Monday (Difference)
monday_only = monday_subjects.difference(tuesday_subjects)
print("Subjects studied ONLY on Monday:", monday_only)
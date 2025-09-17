# Program to calculate attendance percentage and exam eligibility

# Input: total working days and number of absent days
working_days = int(input("Enter total number of working days: "))
absent_days = int(input("Enter total number of days absent: "))

# Calculate attended days
attended_days = working_days - absent_days

# Calculate attendance percentage
percentage = (attended_days / working_days) * 100

# Display attendance
print(f"Attendance percentage: {percentage:.2f}%")

# Check eligibility
if percentage < 75:
    print("You are NOT allowed to sit for the exam.")
else:
    print("You are allowed to sit for the exam.")
from datetime import datetime

# 1. Display current date and time using datetime module
now = datetime.now()
print("=== My Daily Mood Advisor ===")
print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("-" * 30)

# 2. Get user input
name = input("Enter your name: ")
mood = input("How are you feeling today? (happy/sad/stressed): ").lower()
energy = input("What is your energy level? (high/low): ").lower()

# 3. Personalized advice using conditional statements
advice = ""

if mood == "happy":
    if energy == "high":
        advice = "Great day to start a new project or go work out!"
    else:
        advice = "Enjoy your good mood with a relaxing activity or book."
elif mood == "sad":
    if energy == "high":
        advice = "Go for a walk or talk to a friend to clear your mind."
    else:
        advice = "Get plenty of rest and treat yourself kindly today."
elif mood == "stressed":
    advice = "Take a deep breath and take things one step at a time."
else:
    advice = "Stay mindful and make time for things you enjoy!"

# 4. Display personalized advice message
print(f"\nHello {name}!")
print(f"Daily Advice: {advice}")
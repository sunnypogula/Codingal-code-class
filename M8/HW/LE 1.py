import random

# List of numbers provided to srujan

numbers = [3, 7, 12, 19, 25, 30]

# Randomly choose a number (the judge's number)
secret_number = random.choice(numbers)

print("Welcome, srujan!")
print("Here is your list of numbers:")
print(numbers)

# Ask srujan to guess
guess = int(input("Guess the number selected by the judge: "))

# Compare guess with secret number
if guess == secret_number:
    print("🎉 Correct! You guessed the number!")
elif guess > secret_number:
    print("Too high! Try a smaller number next time.")
else:
    print("Too low! Try a bigger number next time.")

print(f"The correct number was: {secret_number}")
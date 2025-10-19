import tkinter as tk
from tkinter import messagebox
import random

# --- 1. Global Variable for the Secret Number ---
SECRET_NUMBER = 0
MAX_GUESSES = 10 # Optional limit

# --- 2. Function to Start a New Game ---
def start_new_game():
    """Generates a new random number and resets the game state."""
    global SECRET_NUMBER
    # Use the random module to pick a number between 1 and 100
    SECRET_NUMBER = random.randint(1, 100)
    
    # Reset GUI elements
    result_label.config(text="Guess a number between 1 and 100.")
    guess_entry.delete(0, tk.END) # Clear the input field
    # 
# --- 3. Function to Check the User's Guess ---
def check_guess():
    """Handles the user's input, checks the guess, and updates the display."""
    try:
        # Get input and convert to an integer
        user_guess = int(guess_entry.get())
        
        # Input validation (Conditional Statement)
        if not 1 <= user_guess <= 100:
            result_label.config(text="Please enter a number between 1 and 100.")
            return

        # Conditional Statements to check the guess
        if user_guess < SECRET_NUMBER:
            result_label.config(text="Too Low! Try again.")
        elif user_guess > SECRET_NUMBER:
            result_label.config(text="Too High! Try again.")
        else:
            # Correct Guess - Show a Pop-up/Dialogue Window
            messagebox.showinfo("CONGRATULATIONS!", f"You guessed it! The number was {SECRET_NUMBER}.")
            start_new_game() # Automatically start a new game
            
    except ValueError:
        # Error handling for non-integer input
        result_label.config(text="Invalid input. Please enter a whole number.")
    
    # Clear the entry field after each guess for user convenience
    guess_entry.delete(0, tk.END)

# --- 4. Setting up the Tkinter GUI ---
# Initialize the main window
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("400x250") # Set window size

# Create Widgets

# Title Label
title_label = tk.Label(root, text="🔢 Number Guessing Game", font=('Arial', 16, 'bold'))
title_label.pack(pady=10)

# Instruction/Result Label
result_label = tk.Label(root, text="Click 'New Game' to start!", font=('Arial', 12))
result_label.pack(pady=5)

# Entry field for the user's guess
guess_entry = tk.Entry(root, width=15, font=('Arial', 14))
guess_entry.pack(pady=5)

# Button to submit the guess, linked to the 'check_guess' function
guess_button = tk.Button(root, text="Guess", command=check_guess, font=('Arial', 12), bg='#4CAF50', fg='white')
guess_button.pack(pady=5)

# Button to start a new game
new_game_button = tk.Button(root, text="New Game", command=start_new_game, font=('Arial', 12), bg='#2196F3', fg='white')
new_game_button.pack(pady=10)

# --- 5. Start the Game and Run the Main Loop ---
start_new_game() # Call the function to initialize the first game

# This is the main Tkinter event loop (implicitly using loops concept)
root.mainloop()
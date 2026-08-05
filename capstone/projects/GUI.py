import random
import tkinter as tk

# Choices available
choices = ["Rock", "Paper", "Scissors"]


# Function to process player move and check outcome
def play(user_choice):
    comp_choice = random.choice(choices)

    # Determine winner using conditional statements
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors")
        or (user_choice == "Paper" and comp_choice == "Rock")
        or (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Update GUI label with choices and result
    result_label.config(
        text=f"You: {user_choice}\nComputer: {comp_choice}\n\n{result}"
    )


# 1. Initialize main GUI window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("320x220")

# 2. Add header label
tk.Label(root, text="Make Your Choice:", font=("Arial", 12, "bold")).pack(
    pady=10
)

# 3. Create interactive buttons using a loop
btn_frame = tk.Frame(root)
btn_frame.pack()

for choice in choices:
    tk.Button(
        btn_frame,
        text=choice,
        width=8,
        command=lambda c=choice: play(c),
    ).pack(side=tk.LEFT, padx=5)

# 4. Display label for game outcome
result_label = tk.Label(root, text="", font=("Arial", 11), pady=15)
result_label.pack()

root.mainloop()
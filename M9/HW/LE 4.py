import random
import string

def generate_password(length=12):
    """
    Generates a strong random password of a specified length.

    Args:
        length (int): The desired length of the password. Defaults to 12.

    Returns:
        str: The generated random password.
    """
    # 1. Define the set of characters to choose from
    # This combines all required character types: lowercase, uppercase, digits, and punctuation.
    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    # 2. Ensure the password contains at least one of each type for strength
    if length < 4:
        # Handle case where desired length is too short
        print("Password length must be at least 4 to include all character types.")
        return None

    # Guarantee at least one of each required type
    password_list = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # 3. Fill the remaining length with random choices from the full character set
    remaining_length = length - len(password_list)
    
    # Use the random.choices() function to efficiently pick the remaining characters
    password_list += random.choices(characters, k=remaining_length)

    # 4. Shuffle the list to randomize the order of the characters
    random.shuffle(password_list)

    # 5. Join the list of characters into a final string and return it
    password = "".join(password_list)
    
    return password

# --- Main execution block ---

if __name__ == "__main__":
    # Ask the user for the desired length
    try:
        desired_length = int(input("Enter the desired password length (e.g., 14): "))
    except ValueError:
        print("Invalid input. Using default length of 12.")
        desired_length = 12

    print("\nGenerating password for Meghan...")
    
    # Call the function to generate the password
    new_password = generate_password(desired_length)

    # Display the result
    if new_password:
        print("-" * 30)
        print(f"✅ Generated Password ({len(new_password)} chars): **{new_password}**")
        print("-" * 30)
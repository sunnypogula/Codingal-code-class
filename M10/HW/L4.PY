def binary_to_decimal(binary_str):
    decimal_value = 0
    # Reverse the string to start from the right (2^0)
    reversed_binary = binary_str[::-1]
    
    for i in range(len(reversed_binary)):
        if reversed_binary[i] == '1':
            decimal_value += 2**i
            
    return decimal_value

# --- User Input ---
user_input = input("Enter a binary number (e.g., 1011): ")

# Method 1: Manual Calculation
manual_result = binary_to_decimal(user_input)

# Method 2: Python Shortcut
shortcut_result = int(user_input, 2)

print(f"Decimal Value (Manual): {manual_result}")
print(f"Decimal Value (Shortcut): {shortcut_result}")
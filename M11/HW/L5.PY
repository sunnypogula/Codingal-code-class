def longest_consecutive_ones_string(n):
    # Convert to binary string (removing the '0b' prefix)
    binary = bin(n)[2:]
    
    max_count = 0
    current_count = 0
    
    for bit in binary:
        if bit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
            
    return max_count

# Testing with 156 (10011100)
num = 156
print(f"Binary of {num}: {bin(num)[2:]}")
print(f"Longest streak of 1s: {longest_consecutive_ones_string(num)}")
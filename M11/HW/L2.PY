def find_first_set_bit(n):
    if n == 0:
        return 0 # No set bits in zero
    
    position = 1
    # Check if the last bit is 1; if not, shift right and increment position
    while (n & 1) == 0:
        n = n >> 1
        position += 1
        
    return position

# Testing
num = 12 # Binary 1100
print(f"The first set bit of {num} is at position: {find_first_set_bit(num)}")
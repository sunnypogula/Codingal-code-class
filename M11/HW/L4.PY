def is_power_of_eight(n):
    # 1. Powers must be greater than 0
    if n <= 0:
        return False
    
    # 2. Check if it is a power of 2 (only one bit set)
    # The formula (n & (n - 1)) == 0 is the classic power-of-2 check
    if (n & (n - 1)) != 0:
        return False
    
    # 3. Check if the set bit is in a position that is a multiple of 3
    # We find the position of the set bit (0-indexed)
    import math
    position = int(math.log2(n))
    
    return position % 3 == 0

# --- Testing ---
test_numbers = [1, 8, 64, 512, 10, 16]

for num in test_numbers:
    if is_power_of_eight(num):
        print(f"{num} is a power of 8!")
    else:
        print(f"{num} is NOT a power of 8.")
def reverse_bits(n, bit_size=8):
    reversed_num = 0
    
    for i in range(bit_size):
        # 1. Shift the current reversed number to the left to make room
        reversed_num = reversed_num << 1
        
        # 2. Extract the last bit of n using AND (&) 
        # and add it to reversed_num using OR (|)
        reversed_num = reversed_num | (n & 1)
        
        # 3. Shift the original number to the right to process the next bit
        n = n >> 1
        
    return reversed_num

# --- Testing the Logic ---
num = 10  # Binary: 1010
bits = 4   # We'll treat it as a 4-bit number for this example
result = reverse_bits(num, bits)

print(f"Original: {num} (binary: {bin(num)[2:].zfill(bits)})")
print(f"Reversed: {result} (binary: {bin(result)[2:].zfill(bits)})")
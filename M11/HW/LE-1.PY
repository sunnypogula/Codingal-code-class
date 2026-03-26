def solve_circuit(a, b):
    # AND Gate: Returns 1 if both bits are 1
    and_gate = a & b
    
    # OR Gate: Returns 1 if at least one bit is 1
    or_gate = a | b
    
    # XOR Gate: Returns 1 if the bits are different
    xor_gate = a ^ b
    
    # NOT Gate: Flips the bits (Inverting a)
    # Note: ~a in Python is -(a+1), so we often mask it for 8-bit circuits
    not_gate = ~a & 0xFF 
    
    return and_gate, or_gate, xor_gate, not_gate

# --- Testing with Input Values ---
# Binary: 5 is 0101, 3 is 0011
val_a = 5 
val_b = 3

res_and, res_or, res_xor, res_not = solve_circuit(val_a, val_b)

print(f"Inputs: A = {val_a} (bin: {bin(val_a)}), B = {val_b} (bin: {bin(val_b)})")
print(f"AND Gate Result: {res_and} (bin: {bin(res_and)})")
print(f"OR Gate Result:  {res_or} (bin: {bin(res_or)})")
print(f"XOR Gate Result: {res_xor} (bin: {bin(res_xor)})")
print(f"NOT Gate (A):    {res_not} (bin: {bin(res_not)})")
# 1. Input list of items
items = ["A", "B", "C"]
n = len(items)

# Total number of subsets = 2^n
total_subsets = 1 << n  # Same as 2**n

print("--- Power Set (All Subsets) ---")
# 2. Enumerate all subsets using two loops
for i in range(total_subsets):
    subset = []
    for j in range(n):
        # 3. Bit probe (check if j-th bit is set)
        bit_probe = 1 << j
        if (i & bit_probe) != 0:
            subset.append(items[j])

    # Print binary mask and corresponding subset
    print(f"Mask {i:03b} ({i}): {subset}")

# 4. Compare bit difference between two numbers (Hamming Distance)
num1, num2 = 5, 3  # 101 and 011 in binary
xor_result = num1 ^ num2
bit_diff = bin(xor_result).count("1")

print(
    f"\nBit difference between {num1} ({num1:03b}) and {num2} ({num2:03b}): {bit_diff}"
)
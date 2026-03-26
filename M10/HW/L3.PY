def binary_search_logic(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        # Function logic happens here...
        return binary_search_logic(arr, low, mid - 1, x)

print("Recurrence Relation for Binary Search: T(n) = T(n/2) + 1")
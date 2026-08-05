# Function to calculate getting a 6 on every roll
def prob_all_sixes(num_rolls):
    # Probability of rolling a 6 on a single die is 1/6
    probability = (1 / 6) ** num_rolls
    return probability

# Change this to the number of rolls you want to check
rolls = 3

result = prob_all_sixes(rolls)
print(f"Probability of getting a 6 all {rolls} times: {result:.6f}")
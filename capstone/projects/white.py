import random

def conditional_prob_white(num_white, num_other):
    """
    Calculates P(2nd White | 1st White) analytically and via simulation.
    """
    # 1. Analytical Formula
    total = num_white + num_other
    if num_white < 1 or total < 2:
        return 0.0
    
    prob_analytical = (num_white - 1) / (total - 1)
    
    # 2. Simulation (Monte Carlo)
    trials = 100_000
    first_was_white_count = 0
    both_were_white_count = 0
    
    # Create the bag: 1s for white, 0s for other
    bag = [1] * num_white + [0] * num_other
    
    for _ in range(trials):
        # Draw 2 balls without replacement
        draw = random.sample(bag, 2)
        
        if draw[0] == 1:  # First ball was white
            first_was_white_count += 1
            if draw[1] == 1:  # Second ball was also white
                both_were_white_count += 1
                
    prob_simulated = both_were_white_count / first_was_white_count
    
    return prob_analytical, prob_simulated

# Example: 5 White balls and 3 Black balls
white_balls = 5
other_balls = 3

p_exact, p_sim = conditional_prob_white(white_balls, other_balls)

print(f"Bag composition: {white_balls} White, {other_balls} Other")
print(f"P(2nd White | 1st White) Exact:     {p_exact:.4f}")
print(f"P(2nd White | 1st White) Simulated: {p_sim:.4f}")
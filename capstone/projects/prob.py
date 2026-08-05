def conditional_prob(white, total):
    # P(2nd White | 1st White) = (white - 1) / (total - 1)
    return (white - 1) / (total - 1) if total > 1 and white > 0 else 0

# Example: 5 white balls out of 10 total balls
print(f"Probability: {conditional_prob(white=5, total=10):.2%}")
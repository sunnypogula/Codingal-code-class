from scipy.stats import poisson
lam = 10
prob_exact_6 = poisson.pmf(6,lam)

prob_12_to_14 = poisson.cdf(14,lam) - poisson.cdf(11,lam)

print("Prob of exactly 6 rainy days:",prob_exact_6)

print("Prob of 12 to 14 rainy days:",prob_12_to_14)

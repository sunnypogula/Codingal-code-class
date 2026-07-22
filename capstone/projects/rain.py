from scipy.stats import poisson
lam = 12
prob_exact_10 = poisson.pmf(10,lam)

prob_12_to_18 = poisson.cdf(18,lam) - poisson.cdf(11,lam)

print("Prob of exactly 6 rainy days:",prob_exact_10)

print("Prob of 12 to 14 rainy days:",prob_12_to_18)

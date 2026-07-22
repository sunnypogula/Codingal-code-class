from scipy.stats import poisson
lam = 15
prob_more_than_20 = 1 - poisson.cdf(20,lam)
prob_17_to_21 = poisson.cdf(21, lam) = poisson.cdf(16,lam)
print("Prob of more than 20 accidents:", prob_more_than_20)
print("Prob of 17 to 21 accidents:",prob_17_to_21)

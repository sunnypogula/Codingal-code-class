from scipy.stats import binom

n = 10
p = 0.5
prob_between_2_to_4 = binom.cdf(2,n,p)

print("Prob of getting between 2 and 4 heads:",prob_between_2_to_4)

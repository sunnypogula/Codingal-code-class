from scipy.stats import binom

n = 10
p = 0.5
prob_less_equal_6 = binom.cdf(6,n,p)
prob_more_than_6 = 1 - prob_less_equal_6

print("Prob of getting more than 6 heads:",prob_more_than_6)

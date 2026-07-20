from math import comb

n = 10
k = 3
p = 0.5
prob = comb(n , k) * (p ** k) * ((1 - p) ** (n - k))
print(prob)
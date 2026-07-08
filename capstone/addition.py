def prob_a_or_b(a,b,common,total):
    prob_a = a / total
    prob_b = b / total
    prob_common = common / total
    answer = prob_a + prob_b - prob_common
    return answer

a = 3
b = 4
common = 2
total = 6
result = prob_a_or_b(a,b,common,total)
print(result)

orange = 6
blue = 4
total =  orange + blue

prob_first_orange = orange / total

prob_second_blue = blue / (total - 1)

final_prob = prob_first_orange * prob_second_blue
print("Prob =",final_prob)

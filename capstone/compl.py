red = 2
blue = 4
white = 9
total = red + blue + white
prob_red_given_blue = red / total
prob_blue_first = blue / total
prob_red_second = red / total
prob_both = prob_blue_first * prob_red_second
print(prob_red_given_blue)
print(prob_both)

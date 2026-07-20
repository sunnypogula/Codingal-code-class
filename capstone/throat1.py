P_A = 0.20
P_notA = 0.80
P_B_given_A = 0.85
P_B_given_notA = 0.02
P_B = (P_B_given_A * P_A) * (P_B_given_notA * P_notA)
P_A_given_B = (P_B_given_A * P_A) / P_B
print("Prob of having strep throat after positive test = ", P_A_given_B)


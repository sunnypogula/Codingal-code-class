import random
def pick_ball_experiment():
    balls = ["red","red","blue","blue","green","green",]
    
    total_balls = len(balls)
    red_balls  = balls.count("red")
    probability = red_balls / total_balls
    print("Probability of picking a Red ball =",probability)
    picked_ball= random.choice(balls)
    print("Picked ball = ",picked_ball)
    if picked_ball == "red":
        print("Congratutlations you picked a red ball")
    else:
        print("The picked ball is not red.")
pick_ball_experiment()
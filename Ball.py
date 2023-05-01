def countBall(correct,user):
    ball = 0
    for i in range(4):
        if(correct[i]==user[i]):
            continue
        if user[i] in correct:
            ball+=1
    return ball

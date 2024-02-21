def groshi(A,B):
    procent = 0
    sumB=0
    for x in range(0, 10, 1):
        procent = B*0.05
        B += procent
        sumB += B
    return sumB - A * 10

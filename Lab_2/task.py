import math
def func(a):
    z = math.cos(a)**2 + math.cos(a)**4
    return z
def groshi(A,B):
    procent = 0
    sumB=0
    for x in range(0, 10, 1):
        procent = B*0.05
        B += procent
        sumB += B
    return sumB - A * 10
a = int(input("Введіть значення числа а: "))
print("Значення функції в точці = ", func(a))
print("Кількість грошей яку потрібно одноразово попросити у батьків = ", groshi(2000, 2500))
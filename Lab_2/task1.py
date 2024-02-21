from mod import groshi
import math
def func(a):
    z = math.cos(a)**2 + math.cos(a)**4
    return z
a = int(input("Введіть значення числа а: "))
print("Значення функції в точці = ", func(a))
print("Кількість грошей яку потрібно одноразово попросити у батьків = ", groshi(2000, 2500))

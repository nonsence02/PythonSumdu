a = int(input("Введіть а: "))

while a < 1 or a > 100:

    a = int(input("Введіть а: "))

b = int(input("Введіть b: "))

while b < 1 or b > 100:

    b = int(input("Введіть ще раз b: "))

if a < b:

    r = ((a / b) + 1)

elif a == b:

    r = -1

else:

    r = (a * b - 5) / a

print("Результат обчислення виразу: ", r)

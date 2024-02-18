n = int(input("Введіть кількість чисел: "))
number = -1
while (n < 1 or n > 9):
    n = int(input("Введіть ще раз кількість чисел: "))
for i i range(1, n + 1):
    print("")
    number += 1
    for j in range(n, number, -1):
        print(j, end=" ")

n = int(input("Введіть розмір масиву: "))
print("Введіть елементи масиву: ")
arr = [int(input()) for _ in range(n)]
l = len(arr)-1
while l >= 0:
    if arr[l] > 0:
        print(arr[l])
    l -= 1

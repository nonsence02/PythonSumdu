my_string = str(input("Введіть значення змінної:"))
while(len(my_string) <= 6):
    my_string = str(input("Довжина строки має бути більша за 5 символів, введіть ще раз:"))
lastfive = my_string[-5:]
print(lastfive)
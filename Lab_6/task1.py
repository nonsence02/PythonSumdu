def remove_duplicates(lst):
    return list(set(lst))
def get_list_from_user():
    try:
        lst = input("Введіть елементи списку через пробіл: ").split()
        lst = [int(x) for x in lst]
        return lst
    except ValueError:
        print("Будь ласка, введіть числа.")

user_list = get_list_from_user()
result = remove_duplicates(user_list)
print("Список без повторень:", result)

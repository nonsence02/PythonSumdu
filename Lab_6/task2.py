def find_first_five_min(lst):
    sorted_lst = sorted(lst)
    first_five_min = sorted_lst[:5]
    return first_five_min

def get_list_from_user():
    try:
        lst = input("Введіть елементи списку через пробіл: ").split()
        lst = [int(x) for x in lst]
        return lst
    except ValueError:
        print("Будь ласка, введіть числа.")

user_list = get_list_from_user()
result = find_first_five_min(user_list)
print("Перші п'ять мінімальних елементів:", result)

import pandas as pd

def remove_duplicates(lst):
    return list(set(lst))

def get_list_from_user():
    try:
        lst = input("Введіть елементи списку через пробіл: ").split()
        lst = [int(x) for x in lst]
        return lst
    except ValueError:
        print("Будь ласка, введіть числа.")
        return []

user_list = get_list_from_user()
result = remove_duplicates(user_list)
print("Список без повторень:", result)

# Перетворення на DataFrame
data_dict = {'Original List': user_list, 'Unique List': result}

# Додавання додаткових даних
data_dict['Category'] = ['A' if x % 2 == 0 else 'B' for x in data_dict['Original List']]
data_dict['Value'] = [x * 2 for x in data_dict['Original List']]

df = pd.DataFrame.from_dict(data_dict, orient='index').transpose()

print("\nDataFrame з даних користувача:")
print(df)

# Групування за категорією та агрегація за середнім значенням
grouped_df = df.groupby('Category')['Value'].mean().reset_index()
print("\nАгреговані дані (середнє значення 'Value' за 'Category'):")
print(grouped_df)

from datetime import datetime

def print_dict(dictionary):
    print("Значення словника:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def add_record(dictionary):
    surname = input("Введіть прізвище: ")
    name = input("Введіть ім'я: ")
    patronymic = input("Введіть по батькові: ")
    year = int(input("Введіть рік народження: "))
    month = int(input("Введіть місяць народження: "))
    day = int(input("Введіть день народження: "))
    birth_date = (year, month, day)
    dictionary[surname] = (name, patronymic, birth_date)
    print("Новий запис додано до словника.")

def remove_record(dictionary):
    key = input("Введіть ключ запису, який потрібно видалити: ")
    if key in dictionary:
        del dictionary[key]
        print("Запис успішно видалено.")
    else:
        print("Запис з таким ключем не знайдено.")

def sort_and_print(dictionary):
    sorted_keys = sorted(dictionary.keys())
    print("Вміст словника за відсортованими ключами:")
    for key in sorted_keys:
        print(f"{key}: {dictionary[key]}")

def check_birthday(students):
    today = datetime.now().date()
    birthday_students = []

    for surname, data in students.items():
        year, month, day = data[2]
        if (today.month, today.day) == (month, day):
            birthday_students.append((data[0], data[1], surname))

    return birthday_students

def main_menu():
    students = {
        "Іванов": ("Петро", "Олександрович", (2005, 4, 20)),
        "Петров": ("Іван", "Миколайович", (2006, 3, 15)),
        "Сидоренко": ("Марія", "Іванівна", (2005, 5, 10)),
        "Ковальчук": ("Олексій", "Володимирович", (2005, 6, 25)),
        "Мельник": ("Анна", "Сергіївна", (2006, 7, 30)),
        "Шевченко": ("Олег", "Петрович", (2005, 8, 5)),
        "Бондаренко": ("Олена", "Ігорівна", (2006, 9, 18)),
        "Козлов": ("Василь", "Андрійович", (2005, 10, 9)),
        "Мороз": ("Тетяна", "Вікторівна", (2006, 11, 12)),
        "Данилюк": ("Ігор", "Степанович", (2005, 3, 18))
    }

    while True:
        print("\nМеню:")
        print("1. Вивести на екран всі значення словника")
        print("2. Додати новий запис до словника")
        print("3. Видалити запис зі словника")
        print("4. Переглянути вміст словника за відсортованими ключами")
        print("5. Перевірити чи є у когось сьогодні день народження")
        print("6. Вийти з програми")

        choice = input("Виберіть опцію: ")
        if choice == '1':
            print_dict(students)
        elif choice == '2':
            add_record(students)
        elif choice == '3':
            remove_record(students)
        elif choice == '4':
            sort_and_print(students)
        elif choice == '5':
            birthday_students = check_birthday(students)
            if birthday_students:
                print("Сьогодні святкують день народження:")
                for student in birthday_students:
                    print(f"{student[0]} {student[1]} {student[2]}")
            else:
                print("Сьогодні ніхто не святкує день народження.")
        elif choice == '6':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()

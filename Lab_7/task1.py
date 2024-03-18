from datetime import datetime

def check_birthday(students):
    today = datetime.now().date()
    birthday_students = []

    for student in students:
        year, month, day = student[3]
        if (today.month, today.day) == (month, day):
            birthday_students.append((student[0], student[1]))

    return birthday_students

students = [
    ("Іванов", "Петро", "Олександрович", (2005, 4, 20)),
    ("Петров", "Іван", "Миколайович", (2006, 3, 15)),
    ("Сидоренко", "Марія", "Іванівна", (2005, 5, 10)),
    ("Ковальчук", "Олексій", "Володимирович", (2005, 6, 25)),
    ("Мельник", "Анна", "Сергіївна", (2006, 7, 30)),
    ("Шевченко", "Олег", "Петрович", (2005, 8, 5)),
    ("Бондаренко", "Олена", "Ігорівна", (2006, 9, 18)),
    ("Козлов", "Василь", "Андрійович", (2005, 10, 9)),
    ("Мороз", "Тетяна", "Вікторівна", (2006, 11, 12)),
    ("Данилюк", "Ігор", "Степанович", (2005, 3, 18))
]

birthday_students = check_birthday(students)
if birthday_students:
    print("Сьогодні святкують день народження:")
    for student in birthday_students:
        print(f"{student[0]} {student[1]}")
else:
    print("Сьогодні ніхто не святкує день народження.")

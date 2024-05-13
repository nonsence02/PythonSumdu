import json

def find_students_with_birthday(month, students):
    matching_students = []
    for student in students:
        birth_month = student['birth_date'][1]  # Місяць народження учня
        if birth_month == month:
            matching_students.append((student['last_name'], student['first_name']))
    return matching_students


def main():
    try:
        # Зчитуємо дані з JSON файлу
        with open('students.json', 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        print("File 'students.json' not found.")
        return
    except json.JSONDecodeError:
        print("Error parsing JSON file.")
        return

    # Запит користувача про місяць
    month = int(input("Enter the month number (1-12): "))

    # Пошук учнів з днем народження у вказаному місяці
    matching_students = find_students_with_birthday(month, students)

    # Виведення результатів
    if matching_students:
        print("Students with a birthday in the specified month:")
        for student in matching_students:
            print(f"{student[0]} {student[1]}")
    else:
        print("No students with a birthday in the specified month were found.")


# Виклик головної функції
if __name__ == "__main__":
    main()

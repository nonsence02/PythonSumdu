import matplotlib.pyplot as plt

students = [
    {"last_name": "Sidorenko", "first_name": "Oleg", "gender": "male", "birth_date": [2005, 5, 12]},
    {"last_name": "Oliynik", "first_name": "Ludmila", "gender": "female", "birth_date": [2006, 7, 24]},
    {"last_name": "Melnyk", "first_name": "Lilia", "gender": "female", "birth_date": [2005, 3, 18]},
    {"last_name": "Jackson", "first_name": "Michael", "gender": "male", "birth_date": [2005, 11, 3]}
]

# Підрахунок кількості хлопців та дівчат
male_count = sum(1 for student in students if student["gender"] == "male")
female_count = sum(1 for student in students if student["gender"] == "female")

# Дані для кругової діаграми
labels = ['Male', 'Female']
sizes = [male_count, female_count]
colors = ['blue', 'pink']

# Побудова кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Male and Female Students')
plt.show()

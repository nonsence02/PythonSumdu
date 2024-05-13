import csv

try:
    # Відкриття вихідного CSV файлу та зчитування даних
    with open('GDP_per_capita_Ukraine.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Зчитування даних та пошук найнижчого та найвищого значень показника
        gdp_values = []
        for row in reader:
            if row['Series Name'] == 'GDP per capita (current US$)':
                for year in range(1999, 2020):
                    gdp_values.append(float(row[str(year) + ' [YR' + str(year) + ']']))

        # Пошук найнижчого та найвищого значень показника
        min_value = min(gdp_values)
        max_value = max(gdp_values)

        # Виведення результатів на екран
        print(f"Найнижче значення GDP per capita: {min_value}")
        print(f"Найвище значення GDP per capita: {max_value}")

        # Збереження результатів у новий CSV файл
        with open('output_file.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Min GDP per capita", min_value])
            writer.writerow(["Max GDP per capita", max_value])

except FileNotFoundError:
    print("Помилка: файл не знайдено!")
except Exception as e:
    print("Помилка під час обробки файлу:", e)

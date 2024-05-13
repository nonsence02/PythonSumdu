import re

# а)
with open("TF7_1.txt", "w") as file:
    file.write("Hello world! This is a test file with some words.\n")
    file.write("Python programming language is awesome.\n")
    file.write("Regular expressions are very useful for text processing.\n")
    file.write("I love programming and solving problems.\n")
    file.write("Let's create a program to find duplicated letters in words.\n")

# б)
with open("TF7_1.txt", "r") as file1, open("TF7_2.txt", "w") as file2:
    duplicated_words = []
    for line in file1:
        words = line.split()
        for word in words:
            if re.search(r'(\w)\1', word):
                duplicated_words.append(word)
    if duplicated_words:
        file2.write("\n".join(duplicated_words))
    else:
        file2.write("Немає слів з подвоєнням букв.")

# в)
with open("TF7_2.txt", "r") as file2:
    print("Зміст файлу TF7_2:")
    for line in file2:
        print(line.strip())

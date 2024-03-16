stroka = "Once upon a time, in a forest far away, a curious explorer named Oliver stumbled upon an ancient treasure map. Determined to uncover its secrets, he embarked on a daring adventure. Along the way, he encountered a wise old wizard who offered guidance. Together, they traversed rivers, scaled mountains, and braved dark caverns. After many trials, they reached the treasure chamber. Amidst the glittering jewels and shimmering gold, Oliver found a mysterious orb. With a sense of wonder, he reached out and touched its surface, triggering a magical transformation that forever altered the course of his journey."
words = stroka.split()
count = 0
for word in words:
    if word.endswith('r'):
        count += 1
print("Кількість слів з останньою буквою r = ", count)
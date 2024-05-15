import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import matplotlib.pyplot as plt

# Завантаження необхідних ресурсів
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')

# Завантаження тексту
bible_text = gutenberg.raw('bible-kjv.txt')

# Розбивка тексту на слова
words = word_tokenize(bible_text)
word_count = len(words)
print(f'Кількість слів у тексті: {word_count}')

# Підрахунок частоти слів
word_freq = Counter(words)

# Отримання 10 найбільш вживаних слів
most_common_words = word_freq.most_common(10)
print(f'10 найбільш вживаних слів: {most_common_words}')

# Побудова стовпчастої діаграми
words, counts = zip(*most_common_words)
plt.bar(words, counts)
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('10 найбільш вживаних слів у тексті')
plt.show()

# Отримання списку стоп-слів англійської мови
stop_words = set(stopwords.words('english'))

# Видалення стоп-слів та пунктуації
filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

# Підрахунок частоти слів без стоп-слів та пунктуації
filtered_word_freq = Counter(filtered_words)

# Отримання 10 найбільш вживаних слів після видалення стоп-слів
filtered_most_common_words = filtered_word_freq.most_common(10)
print(f'10 найбільш вживаних слів після видалення стоп-слів: {filtered_most_common_words}')

# Побудова стовпчастої діаграми
filtered_words, filtered_counts = zip(*filtered_most_common_words)
plt.bar(filtered_words, filtered_counts)
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.title('10 найбільш вживаних слів у тексті після видалення стоп-слів')
plt.show()

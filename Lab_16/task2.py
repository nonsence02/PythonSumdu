import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Зберігаємо довільний текст у файл
input_text = """Werle’s House. Richly and comfortably furnished study. Book cases and upholstered furniture, a writing-table, with papers and ledgers in the center of the stage; lamps alight with green shades, so that the room is dimly lighted. Open folding-doors, with the curtain drawn at back. Beyond a large elegant room, brilliantly lighted with lamps and branched candlesticks. At the right lower entrance of the study a small baize door leads to the office. Left lower entrance a fireplace, with glowing coals, and beyond this a folding-door leading to the dining-room."""

with open('input_text.txt', 'w') as file:
    file.write(input_text)

# Читання тексту з файлу
with open('input_text.txt', 'r') as file:
    text = file.read()

# Токенізація по словам
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Ініціалізація лемматизатора та стеммера
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

# Лемматизація та стеммінг
lemmatized_words = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_words = [stemmer.stem(token) for token in tokens]

print("Lemmatized Words:", lemmatized_words)
print("Stemmed Words:", stemmed_words)

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word.lower() not in stop_words and word.isalnum()]

print("Filtered Words:", filtered_words)

# Запис обробленого тексту у інший файл
with open('processed_text.txt', 'w') as file:
    file.write(' '.join(filtered_words))

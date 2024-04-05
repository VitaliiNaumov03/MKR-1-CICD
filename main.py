import re
from collections import Counter

def find_top_words(file_path, n=10):
    #Відкриття файлу і зчитування вмісту
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    #Видалення знаків пунктуації та розділення тексту на слова
    words = re.findall(r'\b\w+\b', text.lower())

    #Обчислення кількості кожного слова
    word_counts = Counter(words)

    #Знаходження n найпопулярніших слів
    top_words = word_counts.most_common(n)

    return top_words
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

def write_to_file(top_words, output_file):
    #Запис результату у файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in top_words:
            file.write(f"{word}-{count}\n")

#Параметри скрипту
input_file = "input.txt"
output_file = "output.txt"
top_n = 10

#Знаходження та запис 10 найпопулярніших слів у файл
top_words = find_top_words(input_file, top_n)
write_to_file(top_words, output_file)
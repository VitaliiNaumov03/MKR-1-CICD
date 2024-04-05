import re
from collections import Counter

def read_text_from_file(file_path):
    """
    Зчитує текст з файлу.

    Параметри:
    - file_path (str): Шлях до файлу.

    Повертає:
    - str: Зчитаний текст з файлу.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def find_top_words(text, n=10):
    """
    Знаходить n найпопулярніших слів у тексті.

    Параметри:
    - text (str): Текст, у якому потрібно знайти популярні слова.
    - n (int): Кількість слів, які потрібно знайти.

    Повертає:
    - list: Список кортежів (слово, кількість входжень) для n найпопулярніших слів.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    top_words = word_counts.most_common(n)
    return top_words

def write_words_to_file(top_words, output_file):
    """
    Записує список популярних слів у файл.

    Параметри:
    - top_words (list): Список кортежів (слово, кількість входжень).
    - output_file (str): Шлях до вихідного файлу.
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in top_words:
            file.write(f"{word}-{count}\n")

# Знаходження та запис 10 найпопулярніших слів з файлу 'input.txt' у файл 'output.txt'
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    text = read_text_from_file(input_file)
    top_words = find_top_words(text, 10)
    write_words_to_file(top_words, output_file)
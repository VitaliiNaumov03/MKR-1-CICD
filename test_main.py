import pytest
import tempfile
from main import find_top_words, write_words_to_file

#Фікстура для створення вхідного тексту
@pytest.fixture
def input_text():
    return "hello world hello world world"

#Фікстура для очікуваних найпопулярніших слів
@pytest.fixture
def expected_top_words():
    return [('world', 3), ('hello', 2)]

#Фікстура для створення тимчасового файлу для запису результату
@pytest.fixture
def output_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as file:
        yield file.name  #Повертаємо шлях до тимчасового файлу
        file.close()  #Закриваємо тимчасовий файл

#Параметризований тест для функції find_top_words
@pytest.mark.parametrize("n", [1, 2])
def test_find_top_words(input_text, expected_top_words, n):
    """
    Цей тест перевіряє правильність роботи функції find_top_words.
    Виконується для різних значень параметру n.
    """
    result = find_top_words(input_text, n)
    assert result == expected_top_words[:n]

#Тест для функції write_words_to_file
def test_write_words_to_file(output_file, expected_top_words):
    """
    Цей тест перевіряє правильність роботи функції write_words_to_file.
    Спочатку записує список популярних слів у тимчасовий файл, а потім перевіряє, чи дані були записані коректно.
    """
    write_words_to_file(expected_top_words, output_file)

    #Зчитуємо дані з тимчасового файлу та перевіряємо, чи вони співпадають із очікуваними
    with open(output_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            word, count = line.strip().split('-')
            assert (word, int(count)) == expected_top_words[i]
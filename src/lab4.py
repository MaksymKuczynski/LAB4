"""
Лабораторна робота № 4: Обробка рядків та регулярні вирази
Варіант 13:
- Практичне завдання: Обробка погодних даних (витяг температури, вологості, швидкості вітру).
- Завдання на регулярні вирази: Вилучення назви крипто-валюти (NTCoin).
"""

import re
from collections import Counter


# === Функції для базових операцій з рядками ===

def find_substring(text, substring):
    """
    Пошук підрядка в тексті.
    Повертає індекс першого входження або -1, якщо підрядок не знайдено.
    """
    return text.find(substring)


def replace_substring(text, old, new):
    """
    Заміна підрядка в тексті.
    """
    return text.replace(old, new)


def split_text(text, delimiter=' '):
    """
    Розділення тексту за роздільником.
    """
    return text.split(delimiter)


def format_string_f(name, age):
    """
    Форматування рядка з використанням f-string.
    """
    return f"Мене звати {name} і мені {age} років."


def format_string_method(name, age):
    """
    Форматування рядка з використанням методу .format().
    """
    return "Мене звати {} і мені {} років.".format(name, age)


# === Функції для роботи з регулярними виразами ===

def extract_emails(text):
    """
    Витяг email адрес з тексту.
    """
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


def validate_phone_number(number):
    """
    Валідація українського телефонного номера.
    Формат: +380xxxxxxxxx (12 цифр + плюс на початку)
    """
    pattern = r'^\+380\d{9}$'
    return bool(re.match(pattern, number.strip()))


def extract_hashtags(text):
    """
    Витяг хештегів з тексту.
    """
    pattern = r'#[a-zA-Z0-9_а-яА-ЯіІїЇєЄґҐ]+'
    return re.findall(pattern, text)


def extract_mentions(text):
    """
    Витяг згадувань користувачів з тексту (напр. @user).
    """
    pattern = r'@[a-zA-Z0-9_]+'
    return re.findall(pattern, text)


# === Функції для аналізу тексту ===

def count_words(text):
    """
    Підрахунок кількості слів у тексті.
    """
    words = re.findall(r'\b[a-zA-Z0-9_а-яА-ЯіІїЇєЄґҐ-]+\b', text)
    return len(words)


def count_sentences(text):
    """
    Підрахунок кількості речень у тексті.
    """
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


def word_frequency(text):
    """
    Підрахунок частоти слів у тексті.
    Повертає об'єкт Counter.
    """
    words = re.findall(r'\b[a-zA-Z0-9_а-яА-ЯіІїЇєЄґҐ-]+\b', text.lower())
    return Counter(words)


def analyze_text(text):
    """
    Комплексний аналіз тексту.
    Повертає словник з результатами аналізу.
    """
    freq = word_frequency(text)
    return {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text),
        'top_words': freq.most_common(5),
        'emails': extract_emails(text),
        'hashtags': extract_hashtags(text),
    }


def format_analysis_results(results):
    """
    Форматування результатів аналізу для зручного виведення.
    """
    output = "\n=== Результати аналізу тексту ===\n"
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n"
    
    output += "Топ-5 найвживаніших слів:\n"
    for word, count in results['top_words']:
        output += f"  - {word}: {count}\n"
        
    output += f"Знайдені Email: {', '.join(results['emails']) if results['emails'] else 'не знайдено'}\n"
    output += f"Знайдені хештеги: {', '.join(results['hashtags']) if results['hashtags'] else 'не знайдено'}\n"
    return output


# === Функція для вилучення даних за варіантом ===

def extract_variant_data(text, variant_pattern):
    """
    Вилучає дані з тексту за допомогою патерну, специфічного для варіанту.
    """
    return re.findall(variant_pattern, text)


# === Практичне завдання (Варіант 13): Обробка погодних даних ===

def parse_weather_data(weather_text):
    """
    Витягує температуру, вологість та швидкість вітру із тексту погодного звіту.
    Приклад тексту: "Сьогодні за вікном +18°C, вологість 65%, вітер 12 км/год."
    """
    temp_match = re.search(r'([+-]?\d+(?:\.\d+)?)\s*°C', weather_text)
    humidity_match = re.search(r'вологість\s*(\d+)%', weather_text, re.IGNORECASE)
    wind_match = re.search(r'вітер\s*(\d+(?:\.\d+)?)\s*км/год', weather_text, re.IGNORECASE)

    temp = float(temp_match.group(1)) if temp_match else None
    humidity = int(humidity_match.group(1)) if humidity_match else None
    wind_speed = float(wind_match.group(1)) if wind_match else None

    return {
        'temperature_celsius': temp,
        'humidity_percent': humidity,
        'wind_speed_kmh': wind_speed
    }


# === Головна частина програми ===

def read_file_content(filepath):
    """
    Читає вміст файлу.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {filepath}")
        return None


def main():
    """
    Головна функція, що керує виконанням програми.
    """
    print("Ласкаво просимо до аналізатора тексту!")

    text_filepath = 'src/data/neoterra_text.txt'
    text_to_analyze = read_file_content(text_filepath)
    if not text_to_analyze:
        return

    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту 'NeoTerra 3000'")
            print("2. Валідація телефонного номера")
            print("3. Вилучення даних за варіантом 13 (Назва криптовалюти)")
            print("4. Обробка погодних даних (Практичне завдання В-13)")
            print("5. Вихід")
            choice = input("Ваш вибір: ").strip()

            if choice == '1':
                results = analyze_text(text_to_analyze)
                print(format_analysis_results(results))

            elif choice == '2':
                phone = input("Введіть номер телефону для валідації (+380XXXXXXXXX): ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")

            elif choice == '3':
                # Патерн для пошуку криптовалюти NTCoin (та її абревіатури NTC)
                crypto_pattern = r'\b[A-Z]{2,6}Coin\b|\bNTC\b'
                matches = extract_variant_data(text_to_analyze, crypto_pattern)
                print(f"Знайдена назва криптовалюти / позначення: {set(matches)}")

            elif choice == '4':
                sample_weather = input("Введіть рядок з погодними даними (або натисніть Enter для тестового): ")
                if not sample_weather.strip():
                    sample_weather = "Сьогодні температура +20°C, відносна вологість 20%, північно-західний вітер 5 км/год."
                    print(f"Використовуємо тестовий рядок: \"{sample_weather}\"")
                parsed = parse_weather_data(sample_weather)
                print(f"Результат парсингу погоди:\n  - Температура: {parsed['temperature_celsius']} °C\n  - Вологість: {parsed['humidity_percent']} %\n  - Швидкість вітру: {parsed['wind_speed_kmh']} км/год")

            elif choice == '5':
                print("Дякуємо за використання аналізатора!")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Виникла помилка: {e}")


if __name__ == '__main__':
    main()
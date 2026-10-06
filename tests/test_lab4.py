import unittest
import sys
import os

# Додаємо шлях до папки src, щоб можна було імпортувати lab4
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab4 import (
    find_substring,
    replace_substring,
    split_text,
    format_string_f,
    format_string_method,
    extract_emails,
    validate_phone_number,
    extract_hashtags,
    extract_mentions,
    count_words,
    count_sentences,
    word_frequency,
    extract_variant_data,
    parse_weather_data
)


class TestTextAnalyzer(unittest.TestCase):

    def test_find_substring(self):
        """Тест для функції find_substring."""
        self.assertEqual(find_substring("Hello, world!", "world"), 7)
        self.assertEqual(find_substring("NeoTerra 3000", "Python"), -1)

    def test_replace_substring(self):
        """Тест для функції replace_substring."""
        self.assertEqual(replace_substring("Hello, world!", "world", "Python"), "Hello, Python!")

    def test_split_text(self):
        """Тест для функції split_text."""
        self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])
        self.assertEqual(split_text("apple banana orange"), ["apple", "banana", "orange"])

    def test_format_string_f(self):
        """Тест для функції format_string_f."""
        self.assertEqual(format_string_f("Alice", 30), "Мене звати Alice і мені 30 років.")

    def test_format_string_method(self):
        """Тест для функції format_string_method."""
        self.assertEqual(format_string_method("Bob", 25), "Мене звати Bob і мені 25 років.")

    def test_extract_emails(self):
        """Тест для функції extract_emails."""
        text = "Contact us at info@example.com or support@test.com"
        expected = ["info@example.com", "support@test.com"]
        self.assertEqual(extract_emails(text), expected)

    def test_validate_phone_number(self):
        """Тест для функції validate_phone_number."""
        self.assertTrue(validate_phone_number("+380123456789"))
        self.assertTrue(validate_phone_number("+380971112233"))
        self.assertFalse(validate_phone_number("12345"))
        self.assertFalse(validate_phone_number("+38012345678"))  # Занадто короткий
        self.assertFalse(validate_phone_number("0971234567"))    # Без +38

    def test_extract_hashtags(self):
        """Тест для функції extract_hashtags."""
        text = "I love #Python and #Programming"
        expected = ["#Python", "#Programming"]
        self.assertEqual(extract_hashtags(text), expected)

    def test_extract_mentions(self):
        """Тест для функції extract_mentions."""
        text = "Hello @admin and @john_doe!"
        expected = ["@admin", "@john_doe"]
        self.assertEqual(extract_mentions(text), expected)

    def test_count_words(self):
        """Тест для функції count_words."""
        text = "Це тест для перевірки кількості слів у тексті."
        self.assertEqual(count_words(text), 8)

    def test_count_sentences(self):
        """Тест для функції count_sentences."""
        text = "Перше речення. Друге речення! І третє речення?"
        self.assertEqual(count_sentences(text), 3)

    # === Власні тести для Варіанту 13 ===

    def test_parse_weather_data_variant_13(self):
        """Тест для практичного завдання Варіанту 13 (погодні дані)."""
        weather_text = "Сьогодні температура +18°C, вологість 65%, вітер 12.5 км/год."
        result = parse_weather_data(weather_text)
        
        self.assertEqual(result['temperature_celsius'], 18.0)
        self.assertEqual(result['humidity_percent'], 65)
        self.assertEqual(result['wind_speed_kmh'], 12.5)

    def test_extract_crypto_variant_13(self):
        """Тест для пошуку криптовалюти згідно з Варіантом 13."""
        text = "Курс NTCoin становив 1 NTC = 1000 USD."
        pattern = r'\b[A-Z]{2,6}Coin\b|\bNTC\b'
        extracted = extract_variant_data(text, pattern)
        
        self.assertIn("NTCoin", extracted)
        self.assertIn("NTC", extracted)


if __name__ == '__main__':
    # Запуск тестів
    unittest.main(verbosity=2)
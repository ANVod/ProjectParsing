#PS03 - Words game Парсинг HTML-данных с помощью BeautifulSoup и DeepTranslator

import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import random

def get_english_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешность запроса

        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except requests.RequestException as e:
        print("Ошибка запроса:", e)
        return None
    except AttributeError as e:
        print("Ошибка парсинга:", e)
        return None

def translate_to_russian(text):
    try:
        translator = Translator()
        translation = translator.translate(text, src='en', dest='ru').text
        return translation
    except Exception as e:
        print("Ошибка перевода:", e)
        return None

def play_game(rounds=5):
    score = 0
    for _ in range(rounds):
        result = get_english_word()
        if result:
            english_word = result['english_word']
            translated_word = translate_to_russian(english_word)
            if translated_word:
                print(f"Try to translate the word: {english_word}")
                user_translation = input("Your translation: ").strip()

                if user_translation.lower() == translated_word.lower():
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct translation is: {translated_word}")
            else:
                print("Failed to get the translation.")
        else:
            print("Failed to get a new word.")

    print(f"Game over! Your score: {score}/{rounds}")

if __name__ == "__main__":
    print("Welcome to the translation game!")
    play_game()
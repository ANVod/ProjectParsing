import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешность запроса

        soup = BeautifulSoup(response.content, 'html.parser')
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
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
        translation = GoogleTranslator(source='en', target='ru').translate(text)
        return translation
    except Exception as e:
        print("Ошибка перевода:", e)
        return None

def word_game():
    print("Добро пожаловать в игру 'Слова'")
    while True:
        word_dict = get_english_words()
        if word_dict is None:
            print("Не удалось получить слово. Попробуйте позже.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        translated_word = translate_to_russian(word)
        translated_definition = translate_to_russian(word_definition)

        if not translated_word or not translated_definition:
            print("Не удалось перевести слово или его определение. Попробуйте позже.")
            break

        print(f"Значение слова: {translated_definition}")
        user_guess = input("Что это за слово? ")

        if user_guess.lower() == translated_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово: {translated_word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    word_game()
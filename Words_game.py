#PS03 - Words game Парсинг HTML-данных с помощью BeautifulSoup и DeepTranslator

import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def get_english_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status() # Проверка на успеваемость запроса

        soop = BeautifulSoup(response)
        
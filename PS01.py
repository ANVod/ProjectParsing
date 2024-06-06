#PS01 - Парсинг HTML-данных с помощью BeautifulSoup
from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url) # Запрос
html = response.text # Текст

soup = BeautifulSoup(html, "html.parser") # Парсинг
text = soup.find_all("span", class_="text") # Поиск

author = soup.find_all("small", class_="author") # Поиск
print(text) # Вывод
for i in range(len(text)): # Цикл
    print(f"Цитата номер -{i + 1}") # Вывод
    print(text[i].text) # Вывод
    print(f"Автор цитаты - {author[i].text}\n") # Вывод


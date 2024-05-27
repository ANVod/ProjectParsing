# Wikipedia Selenium Scraper

Этот проект представляет собой скрипт на языке Python, который использует библиотеку Selenium для взаимодействия с русской версией Википедии. Скрипт позволяет искать статьи, листать параграфы статьи и переходить по ссылкам на связанные страницы.

## Требования

Для работы скрипта необходимо установить следующие зависимости:

- Python 3.x
- Selenium
- WebDriver для вашего браузера (в данном случае используется Firefox)

## Установка

1. Установите Python 3.x, если он еще не установлен. Скачайте и установите его с официального сайта Python: https://www.python.org/

2. Установите библиотеку Selenium с помощью pip:

    ```bash
    pip install selenium
    ```

3. Скачайте WebDriver для вашего браузера. В данном проекте используется Firefox, поэтому скачайте GeckoDriver с официального сайта: https://github.com/mozilla/geckodriver/releases

4. Убедитесь, что GeckoDriver находится в вашем `PATH`.

## Использование

1. Сохраните скрипт в файл, например, `wikipedia_scraper.py`.

2. Запустите скрипт:

    ```bash
    python wikipedia_scraper.py
    ```

3. Следуйте инструкциям в консоли:
   - Введите запрос для поиска статьи.
   - Выберите действие: листать параграфы, перейти на связанную страницу или выйти из программы.

## Пример кода

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def search_wikipedia(query):
    browser.get("https://ru.wikipedia.org")
    search_box = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "searchInput")))
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "firstHeading")))

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i+1}:\n{paragraph.text}\n")
        if (i + 1) % 5 == 0:
            cont = input("Нажмите Enter для продолжения или введите 'q' для выхода: ")
            if cont.lower() == 'q':
                break

def list_links():
    links = browser.find_elements(By.XPATH, "//div[@id='bodyContent']//a[starts-with(@href, '/wiki/') and not(contains(@href, ':'))]")
    for i, link in enumerate(links):
        print(f"{i+1}. {link.text} ({link.get_attribute('href')})")
    return links

def main():
    initial_query = input("Введите запрос: ")
    search_wikipedia(initial_query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи.")
        print("2. Перейти на одну из связанных страниц.")
        print("3. Выйти из программы.")
        choice = input("Введите номер действия: ")

        if choice == '1':
            list_paragraphs()
        elif choice == '2':
            links = list_links()
            link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
            if 0 <= link_choice < len(links):
                browser.get(links[link_choice].get_attribute('href'))
            else:
                print("Неверный номер ссылки.")
        elif choice == '3':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

    browser.quit()

# Инициализация браузера
browser = webdriver.Firefox()

try:
    main()
finally:
    browser.quit()

Python.org (https://www.python.org/?utm_source=Python)
Welcome to Python.org
The official home of the Python Programming Language
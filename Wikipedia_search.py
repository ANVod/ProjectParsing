#Лекция
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